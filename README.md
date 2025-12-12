# 🏠 Home Assistant Blueprints by Egor Smirnov

Привет! Это коллекция моих автоматизаций для Умного Дома.

## 📥 Как установить

**Способ 1: Через кнопку импорта (Рекомендуемый)**  
Просто нажмите на синюю кнопку "Import" под нужным блупринтом ниже.

**Способ 2: Ручная установка**  
1. Откройте Home Assistant.  
2. Перейдите в "Настройки" > "Автоматизации и сцены" > "Шаблоны".  
3. Нажмите "Импорт шаблона".  
4. Вставьте raw-ссылку на файл с GitHub (например, `https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/your_blueprint.yaml`).

---

## 📋 Коллекция Блупринтов

<!-- START_BLUEPRINTS -->

### 🤖 Умная Вытяжка Pro Max: Динамика, Таймер, Условия \ Smart Exhaust Fan Pro Max: Dynamics, Timer, Conditions
<details>
  <summary><b>📖 Развернуть описание и установку</b></summary>
  
  **Категория:** automation | [📂 Исходный код](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/humidFanSmart.yaml)

  [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint url pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/humidFanSmart.yaml)

  ---

  <details>
    <summary><b>Подробное описание</b></summary>
    Version: 0.1

**Профессиональная и отказоустойчивая автоматизация для ванной комнаты.**

<details>
<summary>💡 Главная идея (Нажмите, чтобы раскрыть) 👈</summary>
Эта логика решает главную проблему: она не ждет фиксированного порога влажности (например, 70%), а постоянно сравнивает влажность в помещении с **динамической нормой** (эталоном/медианой дома). 

### 💡 Ключевые особенности

1.  **Динамическое сравнение:** Работает корректно и зимой (когда влажность в доме низкая), и летом (когда влажность везде высокая).

2.  **Умный Гистерезис:** Выключение происходит не после достижения абсолютной нормы, а когда влажность упала на половину критической разницы. Это экономит энергию и ресурс.

3.  **Ручной режим:** Если включить вытяжку кнопкой, она отработает заданный таймер проветривания (например, 15 мин) и не будет зависеть от влажности.

4.  **Защита (Safety Timeout):** Аварийный таймер принудительно выключит вытяжку, если влажность не падает слишком долго.

5.  **Блокирующие Условия (v2):** Возможность запретить авто-запуск, если открыто окно или включен ночной режим.

6.  **Пост-Действия (v2):** Выполнение дополнительных команд после выключения (например, выключить свет, отправить уведомление).
</details>

<details>
<summary>💬 Контакты 👈</summary>
* [Telegram канал (RU with auto-translate)](https://t.me/u2smart4home)
* [YouTube: Удобный дом](https://www.youtube.com/@udobni_dom)
* [Dzen Profile](https://dzen.ru/id/5e32d0969929ba40059b5892)
</details>

---

Version: 0.1

**Professional and fault-tolerant automation for the bathroom.**

<details>
<summary>💡 Main Idea (Click to expand) 👈</summary>
This logic solves the main problem: it does not wait for a fixed humidity threshold (e.g., 70%), but constantly compares the room humidity with a **dynamic norm** (reference/median of the house). 

### 💡 Key Features

1.  **Dynamic Comparison:** Works correctly in winter (when house humidity is low) and summer (when humidity is high everywhere).

2.  **Smart Hysteresis:** Shutdown occurs not after reaching the absolute norm, but when humidity drops by half the critical difference. This saves energy and resources.

3.  **Manual Mode:** If the exhaust fan is turned on manually, it runs for the specified ventilation timer (e.g., 15 min) independent of humidity.

4.  **Protection (Safety Timeout):** Emergency timer forcibly turns off the fan if humidity doesn't drop for too long.

5.  **Blocking Conditions (v2):** Option to prevent auto-start if window is open or night mode is enabled.

6.  **Post-Actions (v2):** Execute additional commands after shutdown (e.g., turn off light, send notification).
</details>

<details>
<summary>💬 Contacts 👈</summary>
* [Telegram channel (RU with auto-translate)](https://t.me/u2smart4home)
* [YouTube: Удобный дом](https://www.youtube.com/@udobni_dom)
* [Dzen Profile](https://dzen.ru/id/5e32d0969929ba40059b5892)
</details>

  </details>
  
</details>
<hr>

<!-- END_BLUEPRINTS -->

## ☕ Поддержка
Если вам помогли мои работы:  
* [Поддержать на Дзен](https://dzen.ru/id/5e32d0969929ba40059b5892?donate=true)  
* [Telegram канал](https://t.me/u2smart4home)

---

# 🏠 Home Assistant Blueprints by Egor Smirnov (English)

Hello! This is a collection of my automations for Smart Home.

## 📥 How to Install

**Method 1: Via Import Button (Recommended)**  
Just click the blue "Import" button under the desired blueprint below.

**Method 2: Manual Installation**  
1. Open Home Assistant.  
2. Go to "Settings" > "Automations & Scenes" > "Blueprints".  
3. Click "Import Blueprint".  
4. Paste the raw GitHub link to the file (e.g., `https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/your_blueprint.yaml`).

---

## 📋 Blueprint Collection

<!-- START_BLUEPRINTS_EN -->

### 🤖 Умная Вытяжка Pro Max: Динамика, Таймер, Условия \ Smart Exhaust Fan Pro Max: Dynamics, Timer, Conditions
<details>
  <summary><b>📖 Expand Description and Installation</b></summary>
  
  **Category:** automation | [📂 Source Code](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/humidFanSmart.yaml)

  [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint url pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/humidFanSmart.yaml)

  ---

  <details>
    <summary><b>Detailed Description</b></summary>
    Version: 0.1

**Профессиональная и отказоустойчивая автоматизация для ванной комнаты.**

<details>
<summary>💡 Главная идея (Нажмите, чтобы раскрыть) 👈</summary>
Эта логика решает главную проблему: она не ждет фиксированного порога влажности (например, 70%), а постоянно сравнивает влажность в помещении с **динамической нормой** (эталоном/медианой дома). 

### 💡 Ключевые особенности

1.  **Динамическое сравнение:** Работает корректно и зимой (когда влажность в доме низкая), и летом (когда влажность везде высокая).

2.  **Умный Гистерезис:** Выключение происходит не после достижения абсолютной нормы, а когда влажность упала на половину критической разницы. Это экономит энергию и ресурс.

3.  **Ручной режим:** Если включить вытяжку кнопкой, она отработает заданный таймер проветривания (например, 15 мин) и не будет зависеть от влажности.

4.  **Защита (Safety Timeout):** Аварийный таймер принудительно выключит вытяжку, если влажность не падает слишком долго.

5.  **Блокирующие Условия (v2):** Возможность запретить авто-запуск, если открыто окно или включен ночной режим.

6.  **Пост-Действия (v2):** Выполнение дополнительных команд после выключения (например, выключить свет, отправить уведомление).
</details>

<details>
<summary>💬 Контакты 👈</summary>
* [Telegram канал (RU with auto-translate)](https://t.me/u2smart4home)
* [YouTube: Удобный дом](https://www.youtube.com/@udobni_dom)
* [Dzen Profile](https://dzen.ru/id/5e32d0969929ba40059b5892)
</details>

---

Version: 0.1

**Professional and fault-tolerant automation for the bathroom.**

<details>
<summary>💡 Main Idea (Click to expand) 👈</summary>
This logic solves the main problem: it does not wait for a fixed humidity threshold (e.g., 70%), but constantly compares the room humidity with a **dynamic norm** (reference/median of the house). 

### 💡 Key Features

1.  **Dynamic Comparison:** Works correctly in winter (when house humidity is low) and summer (when humidity is high everywhere).

2.  **Smart Hysteresis:** Shutdown occurs not after reaching the absolute norm, but when humidity drops by half the critical difference. This saves energy and resources.

3.  **Manual Mode:** If the exhaust fan is turned on manually, it runs for the specified ventilation timer (e.g., 15 min) independent of humidity.

4.  **Protection (Safety Timeout):** Emergency timer forcibly turns off the fan if humidity doesn't drop for too long.

5.  **Blocking Conditions (v2):** Option to prevent auto-start if window is open or night mode is enabled.

6.  **Post-Actions (v2):** Execute additional commands after shutdown (e.g., turn off light, send notification).
</details>

<details>
<summary>💬 Contacts 👈</summary>
* [Telegram channel (RU with auto-translate)](https://t.me/u2smart4home)
* [YouTube: Удобный дом](https://www.youtube.com/@udobni_dom)
* [Dzen Profile](https://dzen.ru/id/5e32d0969929ba40059b5892)
</details>

  </details>
  
</details>
<hr>

<!-- END_BLUEPRINTS_EN -->

## ☕ Support
If my work helped you:  
* [Support on Zen](https://dzen.ru/id/5e32d0969929ba40059b5892?donate=true)  
* [Telegram channel](https://t.me/u2smart4home)
