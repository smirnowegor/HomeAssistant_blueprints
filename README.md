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

### 🤖 Стиральная машина: уведомления и напоминания (универсальный Blueprint) \ Smart laundry
<details>
  <summary><b>📖 Развернуть описание и установку</b></summary>
  
  **Категория:** automation | [📂 Исходный код](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/washingMachine.yaml)

  [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint url pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/washingMachine.yaml)

  ---

  <details>
    <summary><b>Подробное описание</b></summary>
    Version: 2.1

**Умная Стирка: Уведомления, Энергия и Telegram**

Универсальное решение. Уведомляет о старте/финише, считает стоимость, напоминает о белье.

<details>
<summary>Еще мои блупринты</summary>
d
</details>

<details>
<summary>💡 Главная идея (Нажмите, чтобы раскрыть) 👈</summary>
Этот шаблон решает три проблемы:
1. **Забытое белье:** Напоминания не дадут вещам "задохнуться" в машине.
2. **Контроль расходов:** Вы точно знаете, сколько стоила конкретная стирка (с учетом дневных/ночных тарифов).
3. **Гибкость:** Можно настроить, чтобы днем говорила Алиса/Google, а ночью приходило только тихое уведомление в Телеграм.
</details>

<details>
<summary>⚙️ Как это работает (Нажмите, чтобы раскрыть) 👈</summary>
1. **Старт:** Автоматизация следит за умной розеткой. Если мощность выше порога (например, 10Вт) более 3 минут — стирка началась.
2. **Процесс:** Если настроено, приходит уведомление "Стирка началась".
3. **Финиш:** Когда мощность падает (ниже 5Вт) и держится так 5 минут — стирка завершена.
4. **Расчет:** Скрипт считает потребленную энергию и умножает на тариф.
5. **Напоминания:** В Телеграм приходят кнопки "Напомнить через...". Если вы не отреагировали, система напомнит сама.
</details>

<details>
<summary>⚠️ Настройки (Helpers) 👈</summary>
Для работы всех функций **нужно создать** (Settings -> Devices -> Helpers):
1. `input_text.stirka_end_time` — для времени завершения.
2. `input_number.stirka_start_energy` — для показаний на старте.
3. `input_number.dnevnoi_tarif` и `input_number.nochnoy_tarif` — тарифы.
4. **Utility Meter** — сенсор, который переводит Вт в кВт*ч. *Без него расчет стоимости невозможен.*
5. **Telegram Bot** — должен быть настроен в HA.
</details>

<details>
<summary>💰 Поддержать автора 👈</summary>
Если шаблон оказался полезен, вы можете поддержать меня, выбрав любой удобный способ:
* **Способ 1 (Дзен):** [Поддержать на Дзен 😀](https://dzen.ru/id/5e32d0969929ba40059b5892?donate=true)
* **Способ 2 (Донат-сервис):** [donate.stream](https://donate.stream/yoomoney410013774736621)
* **Способ 3 (Telegram):** Связаться через [Telegram канал](https://t.me/tribute/app?startapp=dvHM)
* **Криптокошелек (Только USDT - Tron TRC20):** `TCHekdJZFndXpDrHZGuTmqFNcqhWBTTzPr`
</details>

<details>
<summary>💬 Контакты 👈</summary>
* [Telegram канал (RU with auto-translate)](https://t.me/u2smart4home)
* [YouTube: Удобный дом](https://www.youtube.com/@udobni_dom)
* [Dzen Profile](https://dzen.ru/id/5e32d0969929ba40059b5892)
</details>

---
**Smart Washing Machine: Notifications, Energy & Telegram**

Universal solution. Notifies about start/finish, calculates cost, reminds about laundry.

<details>
<summary>More blueprints</summary>
d
</details>

<details>
<summary>💡 Main idea (Click to expand) 👈</summary>
This blueprint solves three problems:
1. **Forgotten laundry:** Reminders ensure clothes don't get musty inside the machine.
2. **Cost control:** You know exactly how much a specific wash cycle cost (considering day/night tariffs).
3. **Flexibility:** Configure it to speak via Alexa/Google during the day, but send silent Telegram messages at night.
</details>

<details>
<summary>⚙️ How it works (Click to expand) 👈</summary>
1. **Start:** Automation monitors the smart plug. If power > threshold (e.g., 10W) for > 3 mins — cycle started.
2. **Process:** If configured, a "Wash started" notification is sent.
3. **Finish:** When power drops (below 5W) and stays there for 5 mins — cycle finished.
4. **Calculation:** Script calculates energy used * tariff.
5. **Reminders:** Telegram sends buttons. If ignored, the system will remind you automatically.
</details>

<details>
<summary>⚠️ Requirements (Helpers) 👈</summary>
For full functionality, you **must create** (Settings -> Devices -> Helpers):
1. `input_text.stirka_end_time` — stores finish time.
2. `input_number.stirka_start_energy` — stores energy at start.
3. `input_number.day_tariff` & `input_number.night_tariff` — tariffs.
4. **Utility Meter** — converts Watts to kWh. *Cost calculation won't work without it.*
5. **Telegram Bot** — must be configured in HA.
</details>

<details>
<summary>💰 Support the author 👈</summary>
If you find this blueprint useful, you can support the author through various methods:
* **Method 1 (Dzen):** [Support via Dzen 😀](https://dzen.ru/id/5e32d0969929ba40059b5892?donate=true)
* **Method 2 (Donation Service):** [donate.stream](https://donate.stream/yoomoney410013774736621)
* **Method 3 (Telegram):** Contact via [Telegram Channel](https://t.me/tribute/app?startapp=dvHM)
* **Crypto Wallet (USDT - Tron TRC20 Only):** `TCHekdJZFndXpDrHZGuTmqFNcqhWBTTzPr`
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
<summary>💬 Contacts 👈</summary>
* [Telegram channel (RU with auto-translate)](https://t.me/u2smart4home)
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

### 🤖 Стиральная машина: уведомления и напоминания (универсальный Blueprint) \ Smart laundry
<details>
  <summary><b>📖 Expand Description and Installation</b></summary>
  
  **Category:** automation | [📂 Source Code](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/washingMachine.yaml)

  [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint url pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/washingMachine.yaml)

  ---

  <details>
    <summary><b>Detailed Description</b></summary>
    Version: 2.1

**Умная Стирка: Уведомления, Энергия и Telegram**

Универсальное решение. Уведомляет о старте/финише, считает стоимость, напоминает о белье.

<details>
<summary>Еще мои блупринты</summary>
d
</details>

<details>
<summary>💡 Главная идея (Нажмите, чтобы раскрыть) 👈</summary>
Этот шаблон решает три проблемы:
1. **Забытое белье:** Напоминания не дадут вещам "задохнуться" в машине.
2. **Контроль расходов:** Вы точно знаете, сколько стоила конкретная стирка (с учетом дневных/ночных тарифов).
3. **Гибкость:** Можно настроить, чтобы днем говорила Алиса/Google, а ночью приходило только тихое уведомление в Телеграм.
</details>

<details>
<summary>⚙️ Как это работает (Нажмите, чтобы раскрыть) 👈</summary>
1. **Старт:** Автоматизация следит за умной розеткой. Если мощность выше порога (например, 10Вт) более 3 минут — стирка началась.
2. **Процесс:** Если настроено, приходит уведомление "Стирка началась".
3. **Финиш:** Когда мощность падает (ниже 5Вт) и держится так 5 минут — стирка завершена.
4. **Расчет:** Скрипт считает потребленную энергию и умножает на тариф.
5. **Напоминания:** В Телеграм приходят кнопки "Напомнить через...". Если вы не отреагировали, система напомнит сама.
</details>

<details>
<summary>⚠️ Настройки (Helpers) 👈</summary>
Для работы всех функций **нужно создать** (Settings -> Devices -> Helpers):
1. `input_text.stirka_end_time` — для времени завершения.
2. `input_number.stirka_start_energy` — для показаний на старте.
3. `input_number.dnevnoi_tarif` и `input_number.nochnoy_tarif` — тарифы.
4. **Utility Meter** — сенсор, который переводит Вт в кВт*ч. *Без него расчет стоимости невозможен.*
5. **Telegram Bot** — должен быть настроен в HA.
</details>

<details>
<summary>💰 Поддержать автора 👈</summary>
Если шаблон оказался полезен, вы можете поддержать меня, выбрав любой удобный способ:
* **Способ 1 (Дзен):** [Поддержать на Дзен 😀](https://dzen.ru/id/5e32d0969929ba40059b5892?donate=true)
* **Способ 2 (Донат-сервис):** [donate.stream](https://donate.stream/yoomoney410013774736621)
* **Способ 3 (Telegram):** Связаться через [Telegram канал](https://t.me/tribute/app?startapp=dvHM)
* **Криптокошелек (Только USDT - Tron TRC20):** `TCHekdJZFndXpDrHZGuTmqFNcqhWBTTzPr`
</details>

<details>
<summary>💬 Контакты 👈</summary>
* [Telegram канал (RU with auto-translate)](https://t.me/u2smart4home)
* [YouTube: Удобный дом](https://www.youtube.com/@udobni_dom)
* [Dzen Profile](https://dzen.ru/id/5e32d0969929ba40059b5892)
</details>

---
**Smart Washing Machine: Notifications, Energy & Telegram**

Universal solution. Notifies about start/finish, calculates cost, reminds about laundry.

<details>
<summary>More blueprints</summary>
d
</details>

<details>
<summary>💡 Main idea (Click to expand) 👈</summary>
This blueprint solves three problems:
1. **Forgotten laundry:** Reminders ensure clothes don't get musty inside the machine.
2. **Cost control:** You know exactly how much a specific wash cycle cost (considering day/night tariffs).
3. **Flexibility:** Configure it to speak via Alexa/Google during the day, but send silent Telegram messages at night.
</details>

<details>
<summary>⚙️ How it works (Click to expand) 👈</summary>
1. **Start:** Automation monitors the smart plug. If power > threshold (e.g., 10W) for > 3 mins — cycle started.
2. **Process:** If configured, a "Wash started" notification is sent.
3. **Finish:** When power drops (below 5W) and stays there for 5 mins — cycle finished.
4. **Calculation:** Script calculates energy used * tariff.
5. **Reminders:** Telegram sends buttons. If ignored, the system will remind you automatically.
</details>

<details>
<summary>⚠️ Requirements (Helpers) 👈</summary>
For full functionality, you **must create** (Settings -> Devices -> Helpers):
1. `input_text.stirka_end_time` — stores finish time.
2. `input_number.stirka_start_energy` — stores energy at start.
3. `input_number.day_tariff` & `input_number.night_tariff` — tariffs.
4. **Utility Meter** — converts Watts to kWh. *Cost calculation won't work without it.*
5. **Telegram Bot** — must be configured in HA.
</details>

<details>
<summary>💰 Support the author 👈</summary>
If you find this blueprint useful, you can support the author through various methods:
* **Method 1 (Dzen):** [Support via Dzen 😀](https://dzen.ru/id/5e32d0969929ba40059b5892?donate=true)
* **Method 2 (Donation Service):** [donate.stream](https://donate.stream/yoomoney410013774736621)
* **Method 3 (Telegram):** Contact via [Telegram Channel](https://t.me/tribute/app?startapp=dvHM)
* **Crypto Wallet (USDT - Tron TRC20 Only):** `TCHekdJZFndXpDrHZGuTmqFNcqhWBTTzPr`
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
<summary>💬 Contacts 👈</summary>
* [Telegram channel (RU with auto-translate)](https://t.me/u2smart4home)
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
