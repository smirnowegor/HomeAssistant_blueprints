import os
import yaml

# --- НАСТРОЙКИ ---
REPO_URL = "https://github.com/smirnowegor/HomeAssistant_blueprints"
BRANCH = "main"
BLUEPRINTS_ROOT = "blueprints"
README_FILE = "README.md"

# Маркеры в README
START_MARKER = ""
END_MARKER = ""

# Хак, чтобы PyYAML не ругался на теги Home Assistant (!input)
def default_ctor(loader, tag_suffix, node):
    return tag_suffix + " " + str(node.value)
yaml.add_multi_constructor('!', default_ctor, Loader=yaml.SafeLoader)

def generate_entry(file_path, data):
    # Получаем информацию из YAML
    bp_data = data.get("blueprint", {})
    name = bp_data.get("name", "Unnamed Blueprint")
    description = bp_data.get("description", "")
    domain = bp_data.get("domain", "automation")
    
    # Формируем ссылки
    rel_path = os.path.relpath(file_path, ".")
    # Ссылка на исходный код (GitHub Blob)
    file_url = f"{REPO_URL}/blob/{BRANCH}/{rel_path}"
    # Ссылка для кнопки импорта (Raw Main Branch)
    raw_url = f"https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/{BRANCH}/{rel_path}"
    import_link = f"https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url={file_url}"

    # Определяем иконку по домену
    icon = "🤖"
    if domain == "script": icon = "📜"
    elif domain == "scene": icon = "🎬"

    # HTML ШАБЛОН КАРТОЧКИ
    # Мы берем ВАШЕ описание (которое уже содержит details) 
    # и оборачиваем его в еще один details для компактности списка.
    entry = f"""
### {icon} {name}
<details>
  <summary><b>📖 Развернуть описание и установку</b></summary>
  
  > **Категория:** {domain} | [📂 Исходный код]({file_url})

  [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint url pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)]({import_link})

  ---
  
  {description}
  
</details>
<hr>
"""
    return entry

def main():
    entries = []
    
    # Рекурсивный обход папок blueprints/
    for root, dirs, files in os.walk(BLUEPRINTS_ROOT):
        for file in files:
            if file.endswith(".yaml"):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        # Читаем YAML
                        data = yaml.safe_load(f)
                        if "blueprint" in data:
                            print(f"Processing: {file}")
                            entries.append(generate_entry(full_path, data))
                except Exception as e:
                    print(f"❌ Error processing {file}: {e}")

    # Сортируем по алфавиту
    entries.sort()
    new_content = "\n".join(entries)

    # Обновляем README
    try:
        with open(README_FILE, "r", encoding="utf-8") as f:
            readme_text = f.read()

        if START_MARKER in readme_text and END_MARKER in readme_text:
            start_idx = readme_text.find(START_MARKER) + len(START_MARKER)
            end_idx = readme_text.find(END_MARKER)
            
            final_readme = (
                readme_text[:start_idx] + 
                "\n" + new_content + "\n" + 
                readme_text[end_idx:]
            )
            
            with open(README_FILE, "w", encoding="utf-8") as f:
                f.write(final_readme)
            print("✅ README.md updated successfully!")
        else:
            print("⚠️ Markers not found in README.md")
    except FileNotFoundError:
        print("⚠️ README.md not found!")

if __name__ == "__main__":
    main()
