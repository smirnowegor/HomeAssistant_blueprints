# 🏠 Home Assistant Blueprints by Egor Smirnov / 🇷🇺 Русская версия

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


### 🤖 Умная Вытяжка Pro Max: Динамика, Таймер, Условия!!!!
Категория: **automation** — [Исходник](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/humidFanSmart.yaml) • [Raw](https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/humidFanSmart.yaml)

[![Import blueprint badge](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fsmirnowegor%2FHomeAssistant_blueprints%2Fmain%2Fblueprints%2Fautomation%2Fsmirnowegor%2FhumidFanSmart.yaml)

---
<details>
  <summary><b>📖 Описание (развернуть)</b></summary>

  **Профессиональная и отказоустойчивая автоматизация для ванной комнаты.**
Эта логика решает главную проблему: она не ждет фиксированного порога влажности (например, 70%), а постоянно сравнивает влажность в помещении с **динамической нормой** (эталоном/медианой дома). 
### 💡 Ключевые особенности
1.  **Динамическое сравнение:** Работает корректно и зимой (когда влажность в доме низкая), и летом (когда влажность везде высокая).
2.  **Умный Гистерезис:** Выключение происходит не после достижения абсолютной нормы, а когда влажность упала на половину критической разницы. Это экономит энергию и ресурс.
3.  **Ручной режим:** Если включить вытяжку кнопкой, она отработает заданный таймер проветривания (например, 15 мин) и не будет зависеть от влажности.
4.  **Защита (Safety Timeout):** Аварийный таймер принудительно выключит вытяжку, если влажность не падает слишком долго.
5.  **Блокирующие Условия (v2):** Возможность запретить авто-запуск, если открыто окно или включен ночной режим.
6.  **Пост-Действия (v2):** Выполнение дополнительных команд после выключения (например, выключить свет, отправить уведомление).
</details>

  **Контакты автора:**
- [Telegram канал про автоматизацию домов](https://t.me/u2smart4home) - [YouTube: Удобный дом](https://www.youtube.com/@udobni_dom) - [Яндекс.Дзен: Мой профиль](https://dzen.ru/id/5e32d0969929ba40059b5892) - [Teletype](https://teletype.in/@godisblind)

</details>
<hr>


<!-- BLUEPRINTS_END -->

---

## ☕ Support / Поддержка
Если мои работы помогли — вы можете поддержать автора.
* Telegram: https://t.me/u2smart4home
