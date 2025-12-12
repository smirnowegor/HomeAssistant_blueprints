#!/usr/bin/env python3
# coding: utf-8

"""
Simple updater: put full `description:` under two toggles (RU and EN).
- Does NOT split description.
- Removes "Контакты автора" only for README output.
- Duplicates category line in RU and EN.
- Keeps original YAML files intact.
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
        return data, text  # return raw text too (we will use raw description if present)
    except Exception:
        return None, None

def fallback_parse(path):
    """Fallback: try to extract name and description heuristically from raw text"""
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
    return {"blueprint": {"name": name or "Unnamed Blueprint", "description": desc or ""}}, text

# ---------- Helpers ----------

CONTACTS_RE = re.compile(
    r'(?:^|\n)\s*Контакты автора:.*?(?=\n\s*\n|$)|'    # "Контакты автора:" block
    r'(?:^|\n).*?(?:Telegram|YouTube|Яндекс\.Дзен|Dzen|Teletype).*?(?=\n\s*\n|$)',
    flags=re.IGNORECASE | re.DOTALL
)

def strip_contacts(text: str) -> str:
    """Remove author contacts from text (only for README output)."""
    if not text:
        return text
    cleaned = CONTACTS_RE.sub('\n', text)
    # collapse multiple blank lines
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    return cleaned.strip()

def extract_description_from_yaml(data: dict, raw_text: str):
    """
    Prefer structured parsed YAML description; if not available,
    try to extract from raw text (fallback).
    """
    if isinstance(data, dict):
        bp = data.get("blueprint", {})
        desc = bp.get("description")
        if desc is not None:
            # YAML loader will return a python string (with newlines); keep as-is
            return str(desc)
    # fallback: attempt regex on raw_text
    if raw_text:
        m = re.search(r'description:\s*\|\s*\n((?:\s+.*\n)+)', raw_text, flags=re.IGNORECASE)
        if m:
            block = m.group(1)
            lines = [re.sub(r'^\s+', '', ln) for ln in block.splitlines()]
            return "\n".join(lines).strip()
    return ""

# ---------- Entry generation ----------

def generate_entry(file_path: str, data: dict, raw_text: str):
    bp = data.get("blueprint", {}) if isinstance(data, dict) else {}
    name = bp.get("name") or bp.get("title") or "Unnamed Blueprint"
    domain = bp.get("domain") or "automation"

    # get description full (raw from YAML)
    description_raw = extract_description_from_yaml(data, raw_text) or ""

    # For README output we strip contacts; for YAML files we keep original files untouched.
    description_for_readme = strip_contacts(description_raw)

    rel_path = os.path.relpath(file_path, ".").replace("\\", "/")
    file_url = f"{REPO_URL}/blob/{BRANCH}/{rel_path}"
    raw_url  = f"https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/{BRANCH}/{rel_path}"
    import_link = f"https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url={quote_plus(raw_url)}"

    icon = "🤖"
    if domain == "script": icon = "📜"
    elif domain == "scene": icon = "🎬"

    # Prepare two toggles (both show full description_for_readme)
    # If description is empty, show placeholder
    if not description_for_readme.strip():
        description_for_readme = "_Описание отсутствует в YAML_"

    # We always wrap in our <details> blocks with the required labels.
    ru_block = f"<details>\n  <summary><b>📖 Описание (RU) — развернуть</b></summary>\n\n{description_for_readme}\n\n</details>"
    en_block = f"<details>\n  <summary><b>📖 Description (EN) — expand</b></summary>\n\n{description_for_readme}\n\n</details>"

    # Category lines duplicate RU + EN
    category_ru = f"Категория: **{domain}** — [Исходник]({file_url}) • [Raw]({raw_url})"
    category_en = f"Category: **{domain}** — [Source]({file_url}) • [Raw]({raw_url})"

    entry = f"""
### {icon} {name}

{category_ru}  
{category_en}

[![Import blueprint badge](https://my.home-assistant.io/badges/blueprint_import.svg)]({import_link})

{ru_block}

{en_block}

<hr />
"""
    return name, entry.strip() + "\n"

# ---------- Main ----------

def main():
    entries = []

    for root, dirs, files in os.walk(BLUEPRINTS_ROOT):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                full_path = os.path.join(root, file)
                data, raw_text = read_yaml_safe(full_path)
                if data is None:
                    data, raw_text = fallback_parse(full_path)
                if not data or "blueprint" not in data:
                    print(f"⚠️ Пропускаю (не найден ключ blueprint): {full_path}")
                    continue
                try:
                    name, entry = generate_entry(full_path, data, raw_text)
                    entries.append((name.lower(), entry))
                    print(f"OK: {full_path}")
                except Exception as e:
                    print(f"❌ Ошибка при обработке {full_path}: {e}")

    entries.sort(key=lambda x: x[0])
    new_content = "\n".join(e[1] for e in entries)

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
