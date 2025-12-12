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

### 🤖 Умная Вытяжка Pro Max: Динамика, Таймер, Условия

Категория: **automation** — [Исходник](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/humidFanSmart.yaml) • [Raw](https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/humidFanSmart.yaml)  
Category: **automation** — [Source](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/humidFanSmart.yaml) • [Raw](https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/humidFanSmart.yaml)

[![Import blueprint badge](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fsmirnowegor%2FHomeAssistant_blueprints%2Fmain%2Fblueprints%2Fautomation%2Fsmirnowegor%2FhumidFanSmart.yaml)

<details>
  <summary><b>📖 Описание (RU) — развернуть</b></summary>

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

<details>
  <summary><b>📖 Description (EN) — expand</b></summary>

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

<hr />

### 🤖 Умная Стирка: Уведомления, Энергия и Telegram / Smart Washing Machine: Notifications, Energy & Telegram

Категория: **automation** — [Исходник](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/washingMachine.yaml) • [Raw](https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/washingMachine.yaml)  
Category: **automation** — [Source](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/washingMachine.yaml) • [Raw](https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/washingMachine.yaml)

[![Import blueprint badge](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fsmirnowegor%2FHomeAssistant_blueprints%2Fmain%2Fblueprints%2Fautomation%2Fsmirnowegor%2FwashingMachine.yaml)

<details>
  <summary><b>📖 Описание (RU) — развернуть</b></summary>

  Version: 2.1

**!!Умная Стирка: Уведомления, Энергия и Telegram

</details>

Smart Washing Machine: Notifications, Energy & Telegram**

Универсальное решение. Уведомляет о старте/финише, считает стоимость, напоминает о белье. / Universal solution. Notifies about start/finish, calculates cost, reminds about laundry.


---

<details>
<summary>💡 Главная идея / Main idea (Click to expand) 👈</summary>

<details>
<summary>🇷🇺 Главная идея</summary>

Этот шаблон решает три проблемы:
1. **Забытое белье:** Напоминания не дадут вещам "задохнуться" в машине.
2. **Контроль расходов:** Вы точно знаете, сколько стоила конкретная стирка (с учетом дневных/ночных тарифов).
3. **Гибкость:** Можно настроить, чтобы днем говорила Алиса/Google, а ночью приходило только тихое уведомление в Телеграм.
</details>

<details>
<summary>en Main idea</summary>

This blueprint solves three problems:
1. **Forgotten laundry:** Reminders ensure clothes don't get musty inside the machine.
2. **Cost control:** You know exactly how much a specific wash cycle cost (considering day/night tariffs).
3. **Flexibility:** Configure it to speak via Alexa/Google during the day, but send silent Telegram messages at night.
</details>
</details>

<details>
<summary>⚙️ Как это работает / How it works 👈</summary>

<details>
<summary>🇷🇺 Принцип работы</summary>

1. **Старт:** Автоматизация следит за умной розеткой. Если мощность выше порога (например, 10Вт) более 3 минут — стирка началась.
2. **Процесс:** Если настроено, приходит уведомление "Стирка началась".
3. **Финиш:** Когда мощность падает (ниже 5Вт) и держится так 5 минут — стирка завершена.
4. **Расчет:** Скрипт считает потребленную энергию и умножает на тариф.
5. **Напоминания:** В Телеграм приходят кнопки "Напомнить через...". Если вы не отреагировали, система напомнит сама.
</details>

<details>
<summary>en How it works</summary>

1. **Start:** Automation monitors the smart plug. If power > threshold (e.g., 10W) for > 3 mins — cycle started.
2. **Process:** If configured, a "Wash started" notification is sent.
3. **Finish:** When power drops (below 5W) and stays there for 5 mins — cycle finished.
4. **Calculation:** Script calculates energy used * tariff.
5. **Reminders:** Telegram sends buttons. If ignored, the system will remind you automatically.
</details>
</details>

<details>
<summary>⚠️ Настройки / Requirements (Helpers) 👈</summary>

<details>
<summary> Необходимые настройки (Helpers)</summary>

Для работы всех функций **нужно создать** (Settings -> Devices -> Helpers):
1. `input_text.stirka_end_time` — для времени завершения.
2. `input_number.stirka_start_energy` — для показаний на старте.
3. `input_number.dnevnoi_tarif` и `input_number.nochnoy_tarif` — тарифы.
4. **Utility Meter** — сенсор, который переводит Вт в кВт*ч. *Без него расчет стоимости невозможен.*
5. **Telegram Bot** — должен быть настроен в HA.
</details>

<details>
<summary> Requirements (Helpers)</summary>

For full functionality, you **must create** (Settings -> Devices -> Helpers):
1. `input_text.stirka_end_time` — stores finish time.
2. `input_number.stirka_start_energy` — stores energy at start.
3. `input_number.day_tariff` & `input_number.night_tariff` — tariffs.
4. **Utility Meter** — converts Watts to kWh. *Cost calculation won't work without it.*
5. **Telegram Bot** — must be configured in HA.
</details>
</details>

<details>
<summary>💰 Поддержать автора / Support the author 👈</summary>

<details>
<summary> Поддержать автора</summary>
Если шаблон оказался полезен, вы можете поддержать меня, выбрав любой удобный способ:

* **Способ 1 (Дзен):** [Поддержать на Дзен 😀](https://dzen.ru/id/5e32d0969929ba40059b5892?donate=true)
* **Способ 2 (Донат-сервис):** [donate.stream](http://donate.stream/) (Замените на свою ссылку!)
* **Способ 3 (Telegram):** Связаться через [Telegram канал](https://t.me/u2smart4home)
* **Криптокошелек (Только USDT - Tron TRC20):** `TCHekdJZFndXpDrHZGuTmqFNcqhWBTTzPr`
</details>

<details>
<summary> Support the author (EN)</summary>
If you find this blueprint useful, you can support the author through various methods:

* **Method 1 (Dzen):** [Support via Dzen 😀](https://dzen.ru/id/5e32d0969929ba40059b5892?donate=true)
* **Method 2 (Donation Service):** [donate.stream](http://donate.stream/) (Replace with your personal link!)
* **Method 3 (Telegram):** Contact via [Telegram Channel](https://t.me/u2smart4home)
* **Crypto Wallet (USDT - Tron TRC20 Only):** `TCHekdJZFndXpDrHZGuTmqFNcqhWBTTzPr`
</details>
</details>

<details>
<summary>💬 Контакты / Contacts 👈</summary>

* [Telegram канал (RU with auto-translate)](https://t.me/u2smart4home)
* [YouTube: Удобный дом](https://www.youtube.com/@udobni_dom)
* [Dzen Profile](https://dzen.ru/id/5e32d0969929ba40059b5892)
</details>

<hr />


<!-- BLUEPRINTS_END -->

---

## ☕ Support / Поддержка
Если мои работы помогли — вы можете поддержать автора.
* Telegram: https://t.me/u2smart4home
