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

### 🤖 Стиральная машина: уведомления и напоминания (универсальный Blueprint) \ Washing machine: notifications and reminders (universal Blueprint)
<details>
  <summary><b>📖 Развернуть описание и установку</b></summary>
  
  **Категория:** automation | [📂 Исходный код](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/washingMachine.yaml)

  [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint url pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/washingMachine.yaml)

  ---

  <details>
    <summary><b>Подробное описание</b></summary>
    <strong>Version: 2.1</strong><br><br>

<strong>Умная Стирка: Уведомления, Энергия и Telegram</strong><br>
Универсальное решение: уведомляет о старте/финише, считает стоимость, напоминает о белье.

<details>
<summary>Еще мои блупринты</summary>
<ul>
  <li><a href="https://github.com/smirnowegor/HomeAssistant_blueprints">Git</a></li>
</ul>
</details>

<details>
<summary>💡 Главная идея (Нажмите, чтобы раскрыть) 👈</summary>
<p>Этот шаблон решает три основные проблемы:</p>
<ol>
  <li><strong>Забытое белье</strong> — напоминания не дадут вещам «задохнуться».</li>
  <li><strong>Контроль расходов</strong> — узнаёте точную стоимость конкретной стирки с учётом дневных/ночных тарифов.</li>
  <li><strong>Гибкость</strong> — днём голосовые уведомления, ночью — тихие уведомления в Telegram.</li>
</ol>
</details>

<details>
<summary>⚙️ Как это работает (Нажмите, чтобы раскрыть) 👈</summary>
<p>Алгоритм:</p>
<ol>
  <li><strong>Старт:</strong> если мощность розетки &gt; порога (например 10 Вт) указанное время — стирка началась.</li>
  <li><strong>Процесс:</strong> опционально отправляется сообщение «Стирка началась».</li>
  <li><strong>Финиш:</strong> если мощность ниже порога (например 5 Вт) указанное время — стирка закончена.</li>
  <li><strong>Расчёт:</strong> разница utility meter × дневной/ночной тариф.</li>
  <li><strong>Напоминания:</strong> Telegram-кнопки «Напомнить через...», плюс авто-напоминания.</li>
</ol>
</details>

<details>
<summary>⚠️ Настройки (Helpers) 👈</summary>
<p>Для работы создайте или укажите существующие helpers:</p>
<ul>
  <li><code>input_text.stirka_end_time</code> — хранит время завершения.</li>
  <li><code>input_number.stirka_start_energy</code> — энергия в момент старта.</li>
  <li><code>input_number.dnevnoi_tarif</code> и <code>input_number.nochnoy_tarif</code> — тарифы.</li>
  <li><strong>Utility Meter</strong> — сенсор W → kWh (обязателен для расчёта).</li>
  <li><strong>Telegram Bot</strong> — должен быть настроен.</li>
</ul>
</details>

<details>
<summary>💰 Поддержать автора 👈</summary>
<ul>
  <li>Дзен: <a href="https://dzen.ru/id/5e32d0969929ba40059b5892?donate=true">Поддержать на Дзен</a></li>
  <li>Donat: <a href="https://donate.stream/yoomoney410013774736621">donate.stream</a></li>
  <li>Telegram: <a href="https://t.me/tribute/app?startapp=dvHM">Связаться через Telegram</a></li>
  <li>Криптокошелек (USDT TRC20): <code>TCHekdJZFndXpDrHZGuTmqFNcqhWBTTzPr</code></li>
</ul>
</details>

<details>
<summary>💬 Контакты 👈</summary>
<ul>
  <li><a href="https://t.me/u2smart4home">Telegram канал</a></li>
  <li><a href="https://www.youtube.com/@udobni_dom">YouTube: Удобный дом</a></li>
  <li><a href="https://dzen.ru/id/5e32d0969929ba40059b5892">Dzen Profile</a></li>
</ul>
</details>

<hr>

<strong>Smart Washing Machine: Notifications, Energy & Telegram</strong><br>
Universal solution: notifies about start/finish, calculates cost, reminds about laundry.

<details>
<summary>More blueprints</summary>
<ul>
  <li><a href="https://github.com/smirnowegor/HomeAssistant_blueprints">Git</a></li>
</ul>
</details>

<details>
<summary>💡 Main idea (Click to expand) 👈</summary>
<ol>
  <li><strong>Forgotten laundry</strong> — reminders prevent musty clothes.</li>
  <li><strong>Cost control</strong> — precise cycle cost with day/night tariffs.</li>
  <li><strong>Flexibility</strong> — voice alerts during day, silent Telegram at night.</li>
</ol>
</details>

<details>
<summary>⚙️ How it works (Click to expand) 👈</summary>
<ol>
  <li><strong>Start:</strong> Power &gt; threshold (e.g. 10W) → cycle started.</li>
  <li><strong>Process:</strong> Optional “Wash started” message.</li>
  <li><strong>Finish:</strong> Power &lt; threshold (e.g. 5W) → cycle finished.</li>
  <li><strong>Calculation:</strong> utility meter delta × tariff.</li>
  <li><strong>Reminders:</strong> Inline Telegram buttons + auto reminders.</li>
</ol>
</details>

<details>
<summary>⚠️ Requirements (Helpers) 👈</summary>
<ul>
  <li><code>input_text.stirka_end_time</code> — finish time.</li>
  <li><code>input_number.stirka_start_energy</code> — energy at start.</li>
  <li><code>input_number.day_tariff</code> &amp; <code>input_number.night_tariff</code> — tariffs.</li>
  <li><strong>Utility Meter</strong> — turning Watts → kWh.</li>
  <li><strong>Telegram Bot</strong> — must be configured.</li>
</ul>
</details>

<details>
<summary>💰 Support the author 👈</summary>
<ul>
  <li><a href="https://dzen.ru/id/5e32d0969929ba40059b5892?donate=true">Support via Dzen</a></li>
  <li><a href="https://donate.stream/yoomoney410013774736621">donate.stream</a></li>
  <li><a href="https://t.me/tribute/app?startapp=dvHM">Telegram</a></li>
  <li>Crypto (USDT TRC20): <code>TCHekdJZFndXpDrHZGuTmqFNcqhWBTTzPr</code></li>
</ul>
</details>

<details>
<summary>💬 Contacts 👈</summary>
<ul>
  <li><a href="https://t.me/u2smart4home">Telegram channel</a></li>
  <li><a href="https://www.youtube.com/@udobni_dom">YouTube channel</a></li>
  <li><a href="https://dzen.ru/id/5e32d0969929ba40059b5892">Dzen profile</a></li>
</ul>
</details>

  </details>
  
</details>
<hr>


### 🤖 Универсальная автоматизация управления светом (движение + дверь + таймер) / Universal light automation (motion + door + timer)
<details>
  <summary><b>📖 Развернуть описание и установку</b></summary>
  
  **Категория:** automation | [📂 Исходный код](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/DDmoveFullcontrol.yaml)

  [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint url pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/DDmoveFullcontrol.yaml)

  ---

  <details>
    <summary><b>Подробное описание</b></summary>
    <strong>Version: 1.0</strong><br><br>

<strong>Русский — Универсальная автоматизация света</strong><br>
Это готовый шаблон для включения/выключения света на основе датчиков движения, открытия двери и таймера. Подходит для коридоров, лестниц, санузлов и любых зон, где нужен автоматический свет с задержкой выключения.<br><br>

<details>
<summary>💡 Главная идея (Нажмите чтобы раскрыть) 👈</summary>
<ol>
  <li><strong>Включение при движении</strong> — свет включается сразу при детекции движения.</li>
  <li><strong>Задержка и таймер</strong> — при исчезновении движения запускается таймер (длительность из input_number). По таймеру свет отключается.</li>
  <li><strong>Открытие двери</strong> — можно отдельно включать свет при открытии двери и перезапускать таймер.</li>
  <li><strong>Глобальные условия</strong> — выполняется только если заданы дополнительные условия (например, только ночью или если кто-то дома).</li>
  <li><strong>Доп. действия</strong> — после выключения света можно запускать дополнительные сценарии (например сцены или уведомления).</li>
</ol>
</details>

<details>
<summary>⚙️ Как это работает (Нажмите чтобы раскрыть) 👈</summary>
<ol>
  <li>Триггер: включение одного из выбранных датчиков движения → сервис <code>light.turn_on</code>, отмена таймера.</li>
  <li>Триггер: датчик движения вернулся в <code>off</code> → старт выбранного <code>timer.*</code> на время из указанного <code>input_number</code>.</li>
  <li>Триггер: открытие двери (опционально) → включить свет и запустить таймер.</li>
  <li>Триггер: событие <code>timer.finished</code> → выключить свет и выполнить опциональные действия.</li>
  <li>Глобальные условия в начале: если в input заданы условия, автоматизация выполнится только когда они истинны.</li>
</ol>
</details>

<details>
<summary>⚠️ Требования (Helpers / Setup) 👈</summary>
<ul>
  <li>Данные: хотя бы один binary_sensor с классом occupancy (датчик движения) и один light/zone.</li>
  <li>timer.* — таймер Home Assistant, который будет использоваться для отсчёта времени выключения.</li>
  <li>input_number — хранит длительность ожидания в минутах (используется для формирования duration таймера).</li>
  <li>Опционально: датчик двери (binary_sensor) и дополнительные действия (action), которые выполнятся после выключения света.</li>
</ul>
</details>

<details>
<summary>💬 Контакты и поддержка 👈</summary>
<ul>
  <li><a href="https://t.me/u2smart4home">Telegram канал про автоматизацию домов</a></li>
  <li><a href="https://www.youtube.com/@udobni_dom">YouTube: Удобный дом</a></li>
  <li><a href="https://dzen.ru/id/5e32d0969929ba40059b5892">Яндекс.Дзен: Мой профиль</a></li>
  <li><a href="https://teletype.in/@godisblind">Teletype</a></li>
  <li>Если нужна помощь с настройкой — пишите в Telegram канал (ссылки выше).</li>
</ul>
</details>

<hr>

<strong>English — Universal light automation</strong><br>
Ready-to-use blueprint to automatically turn lights on/off based on motion sensors, door opening and a timer. Ideal for hallways, stairs, bathrooms — any area where you need automatic light with delayed turn-off.<br><br>

<details>
<summary>💡 Main idea (Click to expand) 👈</summary>
<ol>
  <li><strong>Motion-based On</strong> — lights turn on immediately when motion is detected.</li>
  <li><strong>Delay & Timer</strong> — when motion stops the selected <code>timer.*</code> starts (duration from <code>input_number</code>). On timer finish lights turn off.</li>
  <li><strong>Door opening</strong> — optionally turn lights on when a door opens and restart the timer.</li>
  <li><strong>Global conditions</strong> — automation runs only if extra conditions are met (e.g. night mode or someone at home).</li>
  <li><strong>Post-actions</strong> — run extra actions after lights are turned off (scenes, notifications, etc.).</li>
</ol>
</details>

<details>
<summary>⚙️ How it works (Click to expand) 👈</summary>
<ol>
  <li>Trigger: motion sensor → <code>light.turn_on</code>, cancel timer.</li>
  <li>Trigger: motion sensor → <code>off</code> → start <code>timer.*</code> for minutes from <code>input_number</code>.</li>
  <li>Trigger: door sensor opens (optional) → turn on lights and start timer.</li>
  <li>Trigger: <code>timer.finished</code> → turn off lights and run optional actions.</li>
  <li>Automation respects global conditions defined in inputs.</li>
</ol>
</details>

  </details>
  
</details>
<hr>

<!-- END_BLUEPRINTS -->

## ☕ Поддержка
Если вам помогли мои работы:  
* [Поддержать на Дзен](https://dzen.ru/id/5e32d0969929ba40059b5892?donate=true)  
* [Telegram канал](https://t.me/tribute/app?startapp=dvHM)
* [Донат](https://donate.stream/yoomoney410013774736621)
* Криптокошелек (USDT TRC20)  <code>TCHekdJZFndXpDrHZGuTmqFNcqhWBTTzPr</code>

## Связаться / мои каналы
* [YouTube](https://www.youtube.com/@udobni_dom)
* [Telegram канал](https://t.me/u2smart4home)
* [Яндекс Дзен](https://dzen.ru/id/5e32d0969929ba40059b5892)


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

### 🤖 Стиральная машина: уведомления и напоминания (универсальный Blueprint) \ Washing machine: notifications and reminders (universal Blueprint)
<details>
  <summary><b>📖 Expand Description and Installation</b></summary>
  
  **Category:** automation | [📂 Source Code](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/washingMachine.yaml)

  [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint url pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/washingMachine.yaml)

  ---

  <details>
    <summary><b>Detailed Description</b></summary>
    <strong>Version: 2.1</strong><br><br>

<strong>Умная Стирка: Уведомления, Энергия и Telegram</strong><br>
Универсальное решение: уведомляет о старте/финише, считает стоимость, напоминает о белье.

<details>
<summary>Еще мои блупринты</summary>
<ul>
  <li><a href="https://github.com/smirnowegor/HomeAssistant_blueprints">Git</a></li>
</ul>
</details>

<details>
<summary>💡 Главная идея (Нажмите, чтобы раскрыть) 👈</summary>
<p>Этот шаблон решает три основные проблемы:</p>
<ol>
  <li><strong>Забытое белье</strong> — напоминания не дадут вещам «задохнуться».</li>
  <li><strong>Контроль расходов</strong> — узнаёте точную стоимость конкретной стирки с учётом дневных/ночных тарифов.</li>
  <li><strong>Гибкость</strong> — днём голосовые уведомления, ночью — тихие уведомления в Telegram.</li>
</ol>
</details>

<details>
<summary>⚙️ Как это работает (Нажмите, чтобы раскрыть) 👈</summary>
<p>Алгоритм:</p>
<ol>
  <li><strong>Старт:</strong> если мощность розетки &gt; порога (например 10 Вт) указанное время — стирка началась.</li>
  <li><strong>Процесс:</strong> опционально отправляется сообщение «Стирка началась».</li>
  <li><strong>Финиш:</strong> если мощность ниже порога (например 5 Вт) указанное время — стирка закончена.</li>
  <li><strong>Расчёт:</strong> разница utility meter × дневной/ночной тариф.</li>
  <li><strong>Напоминания:</strong> Telegram-кнопки «Напомнить через...», плюс авто-напоминания.</li>
</ol>
</details>

<details>
<summary>⚠️ Настройки (Helpers) 👈</summary>
<p>Для работы создайте или укажите существующие helpers:</p>
<ul>
  <li><code>input_text.stirka_end_time</code> — хранит время завершения.</li>
  <li><code>input_number.stirka_start_energy</code> — энергия в момент старта.</li>
  <li><code>input_number.dnevnoi_tarif</code> и <code>input_number.nochnoy_tarif</code> — тарифы.</li>
  <li><strong>Utility Meter</strong> — сенсор W → kWh (обязателен для расчёта).</li>
  <li><strong>Telegram Bot</strong> — должен быть настроен.</li>
</ul>
</details>

<details>
<summary>💰 Поддержать автора 👈</summary>
<ul>
  <li>Дзен: <a href="https://dzen.ru/id/5e32d0969929ba40059b5892?donate=true">Поддержать на Дзен</a></li>
  <li>Donat: <a href="https://donate.stream/yoomoney410013774736621">donate.stream</a></li>
  <li>Telegram: <a href="https://t.me/tribute/app?startapp=dvHM">Связаться через Telegram</a></li>
  <li>Криптокошелек (USDT TRC20): <code>TCHekdJZFndXpDrHZGuTmqFNcqhWBTTzPr</code></li>
</ul>
</details>

<details>
<summary>💬 Контакты 👈</summary>
<ul>
  <li><a href="https://t.me/u2smart4home">Telegram канал</a></li>
  <li><a href="https://www.youtube.com/@udobni_dom">YouTube: Удобный дом</a></li>
  <li><a href="https://dzen.ru/id/5e32d0969929ba40059b5892">Dzen Profile</a></li>
</ul>
</details>

<hr>

<strong>Smart Washing Machine: Notifications, Energy & Telegram</strong><br>
Universal solution: notifies about start/finish, calculates cost, reminds about laundry.

<details>
<summary>More blueprints</summary>
<ul>
  <li><a href="https://github.com/smirnowegor/HomeAssistant_blueprints">Git</a></li>
</ul>
</details>

<details>
<summary>💡 Main idea (Click to expand) 👈</summary>
<ol>
  <li><strong>Forgotten laundry</strong> — reminders prevent musty clothes.</li>
  <li><strong>Cost control</strong> — precise cycle cost with day/night tariffs.</li>
  <li><strong>Flexibility</strong> — voice alerts during day, silent Telegram at night.</li>
</ol>
</details>

<details>
<summary>⚙️ How it works (Click to expand) 👈</summary>
<ol>
  <li><strong>Start:</strong> Power &gt; threshold (e.g. 10W) → cycle started.</li>
  <li><strong>Process:</strong> Optional “Wash started” message.</li>
  <li><strong>Finish:</strong> Power &lt; threshold (e.g. 5W) → cycle finished.</li>
  <li><strong>Calculation:</strong> utility meter delta × tariff.</li>
  <li><strong>Reminders:</strong> Inline Telegram buttons + auto reminders.</li>
</ol>
</details>

<details>
<summary>⚠️ Requirements (Helpers) 👈</summary>
<ul>
  <li><code>input_text.stirka_end_time</code> — finish time.</li>
  <li><code>input_number.stirka_start_energy</code> — energy at start.</li>
  <li><code>input_number.day_tariff</code> &amp; <code>input_number.night_tariff</code> — tariffs.</li>
  <li><strong>Utility Meter</strong> — turning Watts → kWh.</li>
  <li><strong>Telegram Bot</strong> — must be configured.</li>
</ul>
</details>

<details>
<summary>💰 Support the author 👈</summary>
<ul>
  <li><a href="https://dzen.ru/id/5e32d0969929ba40059b5892?donate=true">Support via Dzen</a></li>
  <li><a href="https://donate.stream/yoomoney410013774736621">donate.stream</a></li>
  <li><a href="https://t.me/tribute/app?startapp=dvHM">Telegram</a></li>
  <li>Crypto (USDT TRC20): <code>TCHekdJZFndXpDrHZGuTmqFNcqhWBTTzPr</code></li>
</ul>
</details>

<details>
<summary>💬 Contacts 👈</summary>
<ul>
  <li><a href="https://t.me/u2smart4home">Telegram channel</a></li>
  <li><a href="https://www.youtube.com/@udobni_dom">YouTube channel</a></li>
  <li><a href="https://dzen.ru/id/5e32d0969929ba40059b5892">Dzen profile</a></li>
</ul>
</details>

  </details>
  
</details>
<hr>


### 🤖 Универсальная автоматизация управления светом (движение + дверь + таймер) / Universal light automation (motion + door + timer)
<details>
  <summary><b>📖 Expand Description and Installation</b></summary>
  
  **Category:** automation | [📂 Source Code](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/DDmoveFullcontrol.yaml)

  [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint url pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/DDmoveFullcontrol.yaml)

  ---

  <details>
    <summary><b>Detailed Description</b></summary>
    <strong>Version: 1.0</strong><br><br>

<strong>Русский — Универсальная автоматизация света</strong><br>
Это готовый шаблон для включения/выключения света на основе датчиков движения, открытия двери и таймера. Подходит для коридоров, лестниц, санузлов и любых зон, где нужен автоматический свет с задержкой выключения.<br><br>

<details>
<summary>💡 Главная идея (Нажмите чтобы раскрыть) 👈</summary>
<ol>
  <li><strong>Включение при движении</strong> — свет включается сразу при детекции движения.</li>
  <li><strong>Задержка и таймер</strong> — при исчезновении движения запускается таймер (длительность из input_number). По таймеру свет отключается.</li>
  <li><strong>Открытие двери</strong> — можно отдельно включать свет при открытии двери и перезапускать таймер.</li>
  <li><strong>Глобальные условия</strong> — выполняется только если заданы дополнительные условия (например, только ночью или если кто-то дома).</li>
  <li><strong>Доп. действия</strong> — после выключения света можно запускать дополнительные сценарии (например сцены или уведомления).</li>
</ol>
</details>

<details>
<summary>⚙️ Как это работает (Нажмите чтобы раскрыть) 👈</summary>
<ol>
  <li>Триггер: включение одного из выбранных датчиков движения → сервис <code>light.turn_on</code>, отмена таймера.</li>
  <li>Триггер: датчик движения вернулся в <code>off</code> → старт выбранного <code>timer.*</code> на время из указанного <code>input_number</code>.</li>
  <li>Триггер: открытие двери (опционально) → включить свет и запустить таймер.</li>
  <li>Триггер: событие <code>timer.finished</code> → выключить свет и выполнить опциональные действия.</li>
  <li>Глобальные условия в начале: если в input заданы условия, автоматизация выполнится только когда они истинны.</li>
</ol>
</details>

<details>
<summary>⚠️ Требования (Helpers / Setup) 👈</summary>
<ul>
  <li>Данные: хотя бы один binary_sensor с классом occupancy (датчик движения) и один light/zone.</li>
  <li>timer.* — таймер Home Assistant, который будет использоваться для отсчёта времени выключения.</li>
  <li>input_number — хранит длительность ожидания в минутах (используется для формирования duration таймера).</li>
  <li>Опционально: датчик двери (binary_sensor) и дополнительные действия (action), которые выполнятся после выключения света.</li>
</ul>
</details>

<details>
<summary>💬 Контакты и поддержка 👈</summary>
<ul>
  <li><a href="https://t.me/u2smart4home">Telegram канал про автоматизацию домов</a></li>
  <li><a href="https://www.youtube.com/@udobni_dom">YouTube: Удобный дом</a></li>
  <li><a href="https://dzen.ru/id/5e32d0969929ba40059b5892">Яндекс.Дзен: Мой профиль</a></li>
  <li><a href="https://teletype.in/@godisblind">Teletype</a></li>
  <li>Если нужна помощь с настройкой — пишите в Telegram канал (ссылки выше).</li>
</ul>
</details>

<hr>

<strong>English — Universal light automation</strong><br>
Ready-to-use blueprint to automatically turn lights on/off based on motion sensors, door opening and a timer. Ideal for hallways, stairs, bathrooms — any area where you need automatic light with delayed turn-off.<br><br>

<details>
<summary>💡 Main idea (Click to expand) 👈</summary>
<ol>
  <li><strong>Motion-based On</strong> — lights turn on immediately when motion is detected.</li>
  <li><strong>Delay & Timer</strong> — when motion stops the selected <code>timer.*</code> starts (duration from <code>input_number</code>). On timer finish lights turn off.</li>
  <li><strong>Door opening</strong> — optionally turn lights on when a door opens and restart the timer.</li>
  <li><strong>Global conditions</strong> — automation runs only if extra conditions are met (e.g. night mode or someone at home).</li>
  <li><strong>Post-actions</strong> — run extra actions after lights are turned off (scenes, notifications, etc.).</li>
</ol>
</details>

<details>
<summary>⚙️ How it works (Click to expand) 👈</summary>
<ol>
  <li>Trigger: motion sensor → <code>light.turn_on</code>, cancel timer.</li>
  <li>Trigger: motion sensor → <code>off</code> → start <code>timer.*</code> for minutes from <code>input_number</code>.</li>
  <li>Trigger: door sensor opens (optional) → turn on lights and start timer.</li>
  <li>Trigger: <code>timer.finished</code> → turn off lights and run optional actions.</li>
  <li>Automation respects global conditions defined in inputs.</li>
</ol>
</details>

  </details>
  
</details>
<hr>

<!-- END_BLUEPRINTS_EN -->

## ☕ Support
If my work has been helpful to you:  
* [Support on Zen](https://dzen.ru/id/5e32d0969929ba40059b5892?donate=true)  
* [Telegram Channel](https://t.me/tribute/app?startapp=dvHM)  
* [Donate](https://donate.stream/yoomoney410013774736621)  
* **Crypto Wallet (USDT TRC20):**  
  <code>TCHekdJZFndXpDrHZGuTmqFNcqhWBTTzPr</code>

## Contact Me & My Channels
* [YouTube](https://www.youtube.com/@udobni_dom)  
* [Telegram Channel](https://t.me/u2smart4home)  
* [Yandex Zen](https://dzen.ru/id/5e32d0969929ba40059b5892)

