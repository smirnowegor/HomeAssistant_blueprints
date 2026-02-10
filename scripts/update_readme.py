import os
import re
import yaml
import logging
from collections import defaultdict

# --- НАСТРОЙКИ ---
REPO_URL = "https://github.com/smirnowegor/HomeAssistant_blueprints"
BRANCH = "main"
BLUEPRINTS_ROOT = "blueprints"
README_FILE = "README.md"

# Маркеры в README (для RU и EN)
START_MARKER_RU = "<!-- START_BLUEPRINTS -->"
END_MARKER_RU = "<!-- END_BLUEPRINTS -->"
START_MARKER_EN = "<!-- START_BLUEPRINTS_EN -->"
END_MARKER_EN = "<!-- END_BLUEPRINTS_EN -->"

# Хак для PyYAML (!input)
def default_ctor(loader, tag_suffix, node):
    return tag_suffix + " " + str(node.value)
yaml.add_multi_constructor('!', default_ctor, Loader=yaml.SafeLoader)

# Logging setup
LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "update_readme.log")
logger = logging.getLogger("update_readme")
logger.setLevel(logging.INFO)
if not logger.handlers:
    fh = logging.FileHandler(LOG_FILE, encoding="utf-8")
    fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s"))
    logger.addHandler(fh)

def generate_entry(file_path, data, lang="ru"):
    bp_data = data.get("blueprint", {})
    name = bp_data.get("name", "Unnamed Blueprint")
    # Description can be a string, a dict with language keys, or separate keys like description_ru/description_en
    desc_field = bp_data.get("description", "")
    if isinstance(desc_field, dict):
        description = desc_field.get(lang) or desc_field.get("ru") or desc_field.get("en") or ""
    else:
        description = bp_data.get(f"description_{lang}", desc_field) or desc_field
    domain = bp_data.get("domain", "automation")
    # Optional metadata
    version = bp_data.get("version") or bp_data.get("blueprint_version") or ""
    author = bp_data.get("author", "")
    tags = bp_data.get("tags", [])
    
    # Normalize relative path for URLs (use forward slashes)
    rel_path = os.path.relpath(file_path, ".").replace(os.sep, "/")
    file_url = f"{REPO_URL}/blob/{BRANCH}/{rel_path}"
    # Build raw URL from REPO_URL to avoid hard-coding repository path
    repo_path = REPO_URL.rstrip("/").replace("https://github.com/", "")
    raw_url = f"https://raw.githubusercontent.com/{repo_path}/{BRANCH}/{rel_path}"
    import_link = f"https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url={raw_url}"  # Исправил на raw_url для импорта

    icon = "🤖" if domain == "automation" else "📜" if domain == "script" else "🎬"

    # Двуязычные заголовки
    if lang == "ru":
        summary_title = "<b>📖 Развернуть описание и установку</b>"
        category_text = f"**Категория:** {domain} | [📂 Исходный код]({file_url})"
        details_title = "Подробное описание"
    else:
        summary_title = "<b>📖 Expand Description and Installation</b>"
        category_text = f"**Category:** {domain} | [📂 Source Code]({file_url})"
        details_title = "Detailed Description"

    # metadata line
    meta_parts = []
    if version:
        meta_parts.append(f"**Version:** {version}")
    if author:
        meta_parts.append(f"**Author:** {author}")
    if tags:
        if isinstance(tags, (list, tuple)):
            meta_parts.append("**Tags:** " + ", ".join(tags))
        else:
            meta_parts.append(f"**Tags:** {tags}")
    meta_line = " | ".join(meta_parts)

    entry = f"""
### {icon} {name}
<details>
  <summary>{summary_title}</summary>
  
  {category_text}
  
  {meta_line}

  [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint url pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)]({import_link})

  ---

  <details>
    <summary><b>{details_title}</b></summary>
    {description}
  </details>
  
</details>
<hr>
"""
    return entry


def collect_blueprints(blueprints_root=BLUEPRINTS_ROOT):
    """Collect blueprints supporting multi-document YAML and grouping by domain.

    Returns: dict domain -> list of (name_lower, entry_ru, entry_en)
    """
    groups = defaultdict(list)
    for root, dirs, files in os.walk(blueprints_root):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        docs = list(yaml.safe_load_all(f))
                        for doc in docs:
                            if not doc or not isinstance(doc, dict):
                                logger.info(f"Skipping empty/invalid doc in {full_path}")
                                continue
                            if "blueprint" in doc:
                                bp = doc.get("blueprint", {})
                                name = bp.get("name", os.path.basename(full_path))
                                domain = bp.get("domain", "automation")
                                groups[domain].append((name.lower(), generate_entry(full_path, doc, "ru"), generate_entry(full_path, doc, "en")))
                except Exception as e:
                    logger.error(f"Error processing {full_path}: {e}")

    # sort entries in each group
    for domain in groups:
        groups[domain].sort(key=lambda x: x[0])

    return groups

def main():
    # Collect blueprints (support multi-document YAML and grouping)
    groups = defaultdict(list)  # domain -> list of (name_lower, entry_ru, entry_en)

    for root, dirs, files in os.walk(BLUEPRINTS_ROOT):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        docs = list(yaml.safe_load_all(f))
                        for doc in docs:
                            if not doc or not isinstance(doc, dict):
                                logger.info(f"Skipping empty/invalid doc in {full_path}")
                                continue
                            if "blueprint" in doc:
                                bp = doc.get("blueprint", {})
                                name = bp.get("name", os.path.basename(full_path))
                                domain = bp.get("domain", "automation")
                                logger.info(f"Processing: {full_path} ({name})")
                                groups[domain].append((name.lower(), generate_entry(full_path, doc, "ru"), generate_entry(full_path, doc, "en")))
                except Exception as e:
                    logger.error(f"❌ Error processing {full_path}: {e}")

    # Build grouped content
    parts_ru = []
    parts_en = []
    for domain, items in groups.items():
        # sort by name
        items.sort(key=lambda x: x[0])
        parts_ru.append(f"\n#### {domain}\n")
        parts_en.append(f"\n#### {domain}\n")
        for _, entry_ru, entry_en in items:
            parts_ru.append(entry_ru)
            parts_en.append(entry_en)

    new_content_ru = "\n".join(parts_ru)
    new_content_en = "\n".join(parts_en)

    # Обновляем README
    try:
        with open(README_FILE, "r", encoding="utf-8") as f:
            readme_text = f.read()

        # Replace RU block with regex to be safer
        pattern_ru = re.compile(r"(?s)(<!-- START_BLUEPRINTS -->).*?(<!-- END_BLUEPRINTS -->)")
        if pattern_ru.search(readme_text):
            readme_text = pattern_ru.sub(lambda m: f"{m.group(1)}\n{new_content_ru}\n{m.group(2)}", readme_text)
            logger.info("Replaced RU blueprint block in README")
        else:
            logger.warning("RU markers not found in README")

        # Replace EN block
        pattern_en = re.compile(r"(?s)(<!-- START_BLUEPRINTS_EN -->).*?(<!-- END_BLUEPRINTS_EN -->)")
        if pattern_en.search(readme_text):
            readme_text = pattern_en.sub(lambda m: f"{m.group(1)}\n{new_content_en}\n{m.group(2)}", readme_text)
            logger.info("Replaced EN blueprint block in README")
        else:
            logger.warning("EN markers not found in README")

        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write(readme_text)
        logger.info("✅ README.md updated successfully!")
    except FileNotFoundError:
        logger.error("⚠️ README.md not found!")

if __name__ == "__main__":
    main()
