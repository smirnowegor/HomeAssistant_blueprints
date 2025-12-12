#!/usr/bin/env python3
# coding: utf-8

import os
import re
import yaml
from urllib.parse import quote_plus

# --- НАСТРОЙКИ ---
REPO_URL = "https://github.com/smirnowegor/HomeAssistant_blueprints"
BRANCH = "main"
BLUEPRINTS_ROOT = "blueprints"
README_FILE = "README.md"

START_MARKER = "<!-- BLUEPRINTS_START -->"
END_MARKER   = "<!-- BLUEPRINTS_END -->"

# Позволяем PyYAML читать файлы с нестандартными тегами (!input ...)
def default_ctor(loader, tag_suffix, node):
    # Возвращаем узел как строку — ничего не парсим
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
    """
    Простейший fallback: ищем name: и description: | ... (многострочный) вручную
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    name = None
    desc = None
    m = re.search(r'blueprint:\s*(?:\n|\s).*?name:\s*["\']?(.*)', text, re.IGNORECASE)
    if m:
        name = m.group(1).strip()
    m2 = re.search(r'description:\s*\|\s*\n((?:\s+.*\n)+)', text)
    if m2:
        # убираем общий отступ
        block = m2.group(1)
        lines = [re.sub(r'^\s+', '', ln) for ln in block.splitlines()]
        desc = "\n".join(lines).strip()
    return {"blueprint": {"name": name or "Unnamed Blueprint", "description": desc or ""}}

def generate_entry(file_path, data):
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

    # Если описание уже содержит <details>, не оборачиваем его снова
    needs_wrap = "<details" not in description.lower()

    desc_block = description.strip()
    if not desc_block:
        desc_block = "_Описание отсутствует в YAML_"

    if needs_wrap:
        # аккуратно делаем сворачиваемый блок
        desc_block = f"<details>\n  <summary><b>📖 Описание (развернуть)</b></summary>\n\n  {desc_block}\n\n</details>"

    # Формируем карточку (без blockquote, чтобы HTML внутри описания корректно рендерился)
    entry = f"""
### {icon} {name}
Категория: **{domain}** — [Исходник]({file_url}) • [Raw]({raw_url})

[![Import blueprint badge](https://my.home-assistant.io/badges/blueprint_import.svg)]({import_link})

---
{desc_block}
<hr>
"""
    return name, entry

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

    # Сортируем по имени (кейс-insensitive)
    entries.sort(key=lambda x: x[0])
    new_content = "\n".join(e[1] for e in entries)

    # Обновляем README между маркерами
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
