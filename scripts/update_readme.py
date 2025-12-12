#!/usr/bin/env python3
# coding: utf-8
"""
Robust updater for README.md:
- If README.md missing or markers absent, inserts a sane bilingual template with markers.
- Scans blueprints/** for YAML, extracts `blueprint.name`, `blueprint.description`, `domain`.
- Builds bilingual entries (Категория / Category) and two <details> blocks (RU/EN) that
  contain the full description exactly as in YAML (but strip contact blocks for README).
- Replaces slice between <!-- BLUEPRINTS_START --> and <!-- BLUEPRINTS_END -->.
- Writes README.md only when changed and prints clear logs for GitHub Actions.
"""

import os
import re
import sys
import yaml
from urllib.parse import quote_plus

ROOT = "."
BLUEPRINTS_ROOT = "blueprints"
README_FILE = "README.md"
REPO_URL = "https://github.com/smirnowegor/HomeAssistant_blueprints"
BRANCH = "main"

START_MARKER = "<!-- BLUEPRINTS_START -->"
END_MARKER   = "<!-- BLUEPRINTS_END -->"

# Allow PyYAML to ignore HA tags like !input
def default_ctor(loader, tag_suffix, node):
    try:
        return node.value
    except Exception:
        return ""
yaml.add_multi_constructor('!', default_ctor, Loader=yaml.SafeLoader)

# remove author contact blocks (only for README output)
CONTACTS_RE = re.compile(
    r'(?:^|\n)\s*Контакты автора:.*?(?=\n\s*\n|$)|'    # "Контакты автора:" block
    r'(?:^|\n).*?(?:Telegram|YouTube|Яндекс\.Дзен|Dzen|Teletype).*?(?=\n\s*\n|$)',
    flags=re.IGNORECASE | re.DOTALL
)

def strip_contacts(text: str) -> str:
    if not text:
        return text
    cleaned = CONTACTS_RE.sub('\n', text)
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    return cleaned.strip()

def read_yaml_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
        data = yaml.safe_load(raw)
        return data, raw
    except Exception as e:
        print(f"❌ YAML load error for {path}: {e}")
        # still return raw for regex extraction
        try:
            with open(path, "r", encoding="utf-8") as f:
                raw = f.read()
            return None, raw
        except Exception:
            return None, ""

def extract_description_from_raw(raw_text: str) -> str:
    if not raw_text:
        return ""
    # Try parsed style: description: | or > or inline quotes
    m = re.search(r'^[ \t]*description:\s*(?:\|\-?|>\-?)\s*\n((?:[ \t]+.*\n)+)', raw_text, flags=re.IGNORECASE | re.MULTILINE)
    if m:
        block = m.group(1)
        lines = [re.sub(r'^[ \t]+', '', ln.rstrip()) for ln in block.splitlines()]
        return "\n".join(lines).strip()
    m2 = re.search(r'^[ \t]*description:\s*[\'"](.+?)[\'"]\s*$', raw_text, flags=re.IGNORECASE | re.MULTILINE)
    if m2:
        return m2.group(1).strip()
    # liberal fallback: everything after 'description:' until next top-level key (line without indent) or EOF
    m3 = re.search(r'^[ \t]*description:\s*\n((?:[ \t].*\n)+)', raw_text, flags=re.IGNORECASE | re.MULTILINE)
    if m3:
        block = m3.group(1)
        lines = [re.sub(r'^[ \t]+', '', ln.rstrip()) for ln in block.splitlines()]
        return "\n".join(lines).strip()
    return ""

def ensure_readme_template():
    """If README missing or markers not present, insert bilingual template with markers at top."""
    base_template = """# 🏠 Home Assistant Blueprints by Egor Smirnov / 🇷🇺 Русская версия

Привет! Это коллекция моих автоматизаций для умного дома.
Вся документация создаётся из кода — описания хранятся прямо в YAML-файлах.

## 📥 Как установить (без HACS)

**Способ 1 — Кнопка "Import"**  
Нажмите на синюю кнопку `Import` в карточке нужного блупринта — она откроет диалог импорта в вашей Home Assistant и подставит raw URL шаблона.

**Способ 2 — Ручная установка (через raw URL)**  
1. Откройте страницу нужного YAML (Raw) — ссылка рядом с карточкой.  
2. Скопируйте raw URL и вставьте в `Configuration -> Blueprints -> Import blueprint` в Home Assistant.

---

# 🏠 Home Assistant Blueprints by Egor Smirnov / 🇬🇧 English version

Welcome! This is my collection of Home Assistant blueprints.
Docs are generated from code — the descriptions live inside YAML files.

## 📥 How to install (no HACS)

**Method 1 — Import button**  
Click the blue `Import` badge in a blueprint card — it opens the import dialog in your Home Assistant with the raw URL prefilled.

**Method 2 — Manual (via raw URL)**  
1. Open the blueprint's Raw file (link near the card).  
2. Copy raw URL and go to `Configuration -> Blueprints -> Import blueprint` in Home Assistant.

---

## 📋 Collection / Коллекция

<!-- BLUEPRINTS_START -->
<!-- BLUEPRINTS_END -->

---
## ☕ Support / Поддержка
Если мои работы помогли — вы можете поддержать автора.
* Telegram: https://t.me/u2smart4home
"""
    if not os.path.exists(README_FILE):
        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write(base_template)
        print(f"ℹ️ README.md не найден. Создан шаблон с маркерами.")
        return

    with open(README_FILE, "r", encoding="utf-8") as f:
        txt = f.read()
    if START_MARKER in txt and END_MARKER in txt:
        print("ℹ️ README.md уже содержит маркеры.")
        return
    # Insert template above existing
