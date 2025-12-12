#!/usr/bin/env python3
# coding: utf-8

"""
Update README.md with blueprint entries.

Changes vs previous version:
- Produce bilingual description block (RU + EN).
- Duplicate "Категория / Category" line in RU and EN.
- Strip "Контакты автора" (Telegram/YouTube/Дзен/Teletype) from README output only.
- Sanitize description for README: remove Version:, leading !! headers, repeated title lines, and internal '---' / '* * *' separators.
- Keep <details> from blueprint descriptions intact (don't double-wrap).
- Use a single <hr> between entries (no multiple '---').
"""

import os
import re
import yaml
from urllib.parse import quote_plus

# --- CONFIG ---
REPO_URL = "https://github.com/smirnowegor/HomeAssistant_blueprints"
BRANCH = "main"
BLUEPRINTS_ROOT = "blueprints"
README_FILE = "README.md"

START_MARKER = "<!-- BLUEPRINTS_START -->"
END_MARKER   = "<!-- BLUEPRINTS_END -->"

# Allow PyYAML to ignore Home Assistant tags like !input
def default_ctor(loader, tag_suffix, node):
    try:
        return node.value
    except Exception:
        return ""
yaml.add_multi_constructor('!', default_ctor, Loader=yaml.SafeLoader)

def read_yaml_safe(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        data = yaml.safe_load(text)
        return data
    except Exception:
        return None

def fallback_parse(path):
    """Simple fallback: try to extract name and description heuristically"""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    name = None
    desc = None
    m = re.search(r'blueprint:\s*(?:\n|\s).*?name:\s*["\']?(.*)', text, re.IGNORECASE)
    if m:
        name = m.group(1).strip()
    m2 = re.search(r'description:\s*\|\s*\n((?:\s+.*\n)+)', text)
    if m2:
        block = m2.group(1)
        lines = [re.sub(r'^\s+', '', ln) for ln in block.splitlines()]
        desc = "\n".join(lines).strip()
    return {"blueprint": {"name": name or "Unnamed Blueprint", "description": desc or ""}}

# ---------- Sanitize / split helpers ----------

CONTACTS_RE = re.compile(
    r'(?:^|\n)\s*Контакты автора:.*?(?=\n\s*\n|$)|'    # "Контакты автора:" block
    r'(?:^|\n).*?(?:Telegram|YouTube|Яндекс\.Дзен|Dzen|Teletype).*?(?=\n\s*\n|$)',
    flags=re.IGNORECASE | re.DOTALL
)

LEADING_VERSION_RE = re.compile(r'^\s*Version:\s*.*$', flags=re.IGNORECASE | re.MULTILINE)
LEADING_BANGS_RE = re.compile(r'^\s*!!.*$', flags=re.MULTILINE)
MULTI_HR_RE = re.compile(r'(?:(?:^-{3,}\s*$)|(?:^\*\s*\*\s*\*\s*$))', flags=re.MULTILINE)
REPEATED_TITLE_RE = re.compile(r'^(?:!!)?\s*[\w\W]{1,120}\s*[:\-–—]\s*.*$', flags=re.MULTILINE)  # heuristic

def strip_contacts(text: str) -> str:
    """Remove author contacts from text (only for README output)."""
    # remove explicit 'Контакты автора' blocks and lines containing known platform names
    cleaned = CONTACTS_RE.sub('\n', text)
    return cleaned

def sanitize_description_for_readme(text: str, blueprint_name: str) -> str:
    """Sanitize description that will go into README:
       - remove Version: lines
       - remove lines starting with !!
       - remove multiple internal HRs
       - remove obvious repeated title lines (heuristic)
       - collapse excessive blank lines
    """
    if not text:
        return ""

    s = text

    # 1) Remove the 'Контакты автора' related chunk(s)
    s = strip_contacts(s)

    # 2) Remove leading Version: lines (common in your templates)
    s = LEADING_VERSION_RE.sub('', s)

    # 3) Remove lines that start with !! (those are titles repeated inside description)
    s = LEADING_BANGS_RE.sub('', s)

    # 4) Remove sequences of '---' or '* * *' that create visual clutter
    s = MULTI_HR_RE.sub('', s)

    # 5) Try to remove repeated heading equal to blueprint name (exact or partial)
    # If the blueprint_name appears alone on a line, remove that line.
    try:
        name_pattern = re.escape(blueprint_name.strip())
        s = re.sub(r'(?m)^\s*' + name_pattern + r'\s*$\n?', '', s)
    except Exception:
        pass

    # 6) Collapse 3+ blank lines into 2
    s = re.sub(r'\n{3,}', '\n\n', s)

    # 7) Trim
    s = s.strip()

    return s

def split_ru_en(description: str):
    """
    Heuristics to split a bilingual description into RU and EN parts.
    Returns (ru_text, en_text).
    Rules:
    - If description contains ' / ' on the first line and looks like 'RU / EN', split there (first occurrence).
    - If description contains a line starting with 'en ' or 'en:' or 'en ' on a new line, split at that marker.
    - If description contains ' / ' often used in many templates, split by first ' / '.
    - Otherwise return (description, description) (same text in both languages).
    """
    if not description:
        return ("", "")

    text = description.strip()

    # 1) If there's an explicit 'en ' marker at line start
    m = re.search(r'(?mi)^\s*en(?:\b|:)\s*', text)
    if m:
        # split at that marker
        idx = m.start()
        ru = text[:idx].strip()
        en = text[idx:].strip()
        # remove leading 'en' token from en
        en = re.sub(r'(?i)^\s*en(?:\b|:)\s*', '', en, count=1).strip()
        return (ru, en)

    # 2) If there is an inline ' / ' separator and both sides contain words of reasonable length,
    #    split at the first ' / ' occurrence (common pattern in your blueprints).
    if ' / ' in text:
        # only split the first paragraph (to avoid splitting many times)
        first_para, *rest = text.split('\n\n', 1)
        if ' / ' in first_para:
            left, right = first_para.split(' / ', 1)
            ru = left.strip()
            en_candidate = right.strip()
            # If there is more content after the first paragraph, append it to both sides (but sanitized)
            tail = rest[0].strip() if rest else ''
            if tail:
                ru = (ru + "\n\n" + tail).strip()
                en_candidate = (en_candidate + "\n\n" + tail).strip()
            return (ru, en_candidate)

    # 3) Fallback: attempt to find " / " anywhere and split into two halves by first separator,
    #    but only if both halves are non-trivial lengths.
    if ' / ' in text:
        left, right = text.split(' / ', 1)
        if len(left) > 30 and len(right) > 20:
            return (left.strip(), right.strip())

    # 4) Otherwise: return same text for both languages
    return (text, text)

# ---------- Entry generation ----------

def generate_entry(file_path: str, data: dict):
    bp = data.get("blueprint", {}) if isinstance(data, dict) else {}
    name = bp.get("name") or bp.get("title") or "Unnamed Blueprint"
    description = bp.get("description") or ""
    domain = bp.get("domain") or "automation"

    rel_path = os.path.relpath(file_path, ".").replace("\\", "/")
    file_url = f"{REPO_URL}/blob/{BRANCH}/{rel_path}"
    raw_url  = f"https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/{BRANCH}/{rel_path}"
    import_link = f"https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url={quote_plus(raw_url)}"

    icon = "🤖"
    if domain == "script": icon = "📜"
    elif domain == "scene": icon = "🎬"

    # Prepare RU / EN description parts (raw from YAML)
    ru_raw, en_raw = split_ru_en(description)

    # Sanitize versions for README (strip contacts, version lines, repeated titles etc.)
    ru_for_readme = sanitize_description_for_readme(ru_raw, name)
    en_for_readme = sanitize_description_for_readme(en_raw, name)

    # If either is empty after sanitize, fallback to original raw halves
    if not ru_for_readme:
        ru_for_readme = ru_raw.strip()
    if not en_for_readme:
        en_for_readme = en_raw.strip()

    # Decide whether to wrap in <details> — don't double-wrap if <details> already present
    def wrap_if_needed(text: str, summary_label: str):
        if "<details" in text.lower():
            # ensure there is a top-level header 'summary' for clarity: we will not wrap
            return text
        else:
            return f"<details>\n  <summary><b>{summary_label}</b></summary>\n\n  {text}\n\n</details>"

    # Make bilingual block: RU then EN
    ru_block = wrap_if_needed(ru_for_readme, "📖 Описание (RU) — развернуть")
    en_block = wrap_if_needed(en_for_readme, "📖 Description (EN) — expand")

    # Category lines duplicate RU + EN
    category_ru = f"Категория: **{domain}** — [Исходник]({file_url}) • [Raw]({raw_url})"
    category_en = f"Category: **{domain}** — [Source]({file_url}) • [Raw]({raw_url})"

    # Compose the entry. Avoid blockquote and avoid adding extra '---' inside description.
    entry = f"""
### {icon} {name}

{category_ru}  
{category_en}

[![Import blueprint badge](https://my.home-assistant.io/badges/blueprint_import.svg)]({import_link})

{ru_block}

{en_block}

<hr />
"""
    # Trim leading/trailing whitespace
    entry = entry.strip() + "\n"
    return name, entry

# ---------- Main ----------

def main():
    entries = []

    for root, dirs, files in os.walk(BLUEPRINTS_ROOT):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                full_path = os.path.join(root, file)
                data = read_yaml_safe(full_path)
                if data is None:
                    data = fallback_parse(full_path)
                if not data or "blueprint" not in data:
                    print(f"⚠️ Пропускаю (не найден ключ blueprint): {full_path}")
                    continue
                try:
                    name, entry = generate_entry(full_path, data)
                    entries.append((name.lower(), entry))
                    print(f"OK: {full_path}")
                except Exception as e:
                    print(f"❌ Ошибка при обработке {full_path}: {e}")

    # Sort entries by name
    entries.sort(key=lambda x: x[0])
    new_content = "\n".join(e[1] for e in entries)

    # Update README between markers
    try:
        with open(README_FILE, "r", encoding="utf-8") as f:
            readme_text = f.read()
    except FileNotFoundError:
        print("❌ README.md не найден в корне репозитория.")
        return

    if START_MARKER not in readme_text or END_MARKER not in readme_text:
        print("❌ Маркеры не найдены в README.md. Пожалуйста, вставьте шаблон README с маркерами.")
        return

    start_idx = readme_text.find(START_MARKER) + len(START_MARKER)
    end_idx = readme_text.find(END_MARKER)

    final_readme = readme_text[:start_idx] + "\n\n" + new_content + "\n\n" + readme_text[end_idx:]
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(final_readme)

    print("✅ README.md обновлён успешно.")

if __name__ == "__main__":
    main()
