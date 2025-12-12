import os
import yaml

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

def generate_entry(file_path, data, lang="ru"):
    bp_data = data.get("blueprint", {})
    name = bp_data.get("name", "Unnamed Blueprint")
    description = bp_data.get("description", "")
    domain = bp_data.get("domain", "automation")
    
    rel_path = os.path.relpath(file_path, ".")
    file_url = f"{REPO_URL}/blob/{BRANCH}/{rel_path}"
    raw_url = f"https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/{BRANCH}/{rel_path}"
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

    entry = f"""
### {icon} {name}
<details>
  <summary>{summary_title}</summary>
  
  {category_text}

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

def main():
    entries_ru = []
    entries_en = []
    
    for root, dirs, files in os.walk(BLUEPRINTS_ROOT):
        for file in files:
            if file.endswith(".yaml"):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        data = yaml.safe_load(f)
                        if "blueprint" in data:
                            print(f"Processing: {file}")
                            entries_ru.append(generate_entry(full_path, data, "ru"))
                            entries_en.append(generate_entry(full_path, data, "en"))  # Если нужно перевести description, добавь логику здесь
                except Exception as e:
                    print(f"❌ Error processing {file}: {e}")

    entries_ru.sort()
    entries_en.sort()
    new_content_ru = "\n".join(entries_ru)
    new_content_en = "\n".join(entries_en)

    # Обновляем README
    try:
        with open(README_FILE, "r", encoding="utf-8") as f:
            readme_text = f.read()

        # RU блок
        if START_MARKER_RU in readme_text and END_MARKER_RU in readme_text:
            start_idx_ru = readme_text.find(START_MARKER_RU) + len(START_MARKER_RU)
            end_idx_ru = readme_text.find(END_MARKER_RU)
            readme_text = readme_text[:start_idx_ru] + "\n" + new_content_ru + "\n" + readme_text[end_idx_ru:]

        # EN блок
        if START_MARKER_EN in readme_text and END_MARKER_EN in readme_text:
            start_idx_en = readme_text.find(START_MARKER_EN) + len(START_MARKER_EN)
            end_idx_en = readme_text.find(END_MARKER_EN)
            readme_text = readme_text[:start_idx_en] + "\n" + new_content_en + "\n" + readme_text[end_idx_en:]

        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write(readme_text)
        print("✅ README.md updated successfully!")
    except FileNotFoundError:
        print("⚠️ README.md not found!")

if __name__ == "__main__":
    main()
