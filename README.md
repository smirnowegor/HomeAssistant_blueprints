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

## 📋 Коллекция Блупринтов!!!

<!-- START_BLUEPRINTS -->

#### automation


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


### 🤖 Универсальная автоматизация управления светом (движение + дверь + таймер) / Universal light control (motion + door + timer)
<details>
  <summary><b>📖 Развернуть описание и установку</b></summary>
  
  **Категория:** automation | [📂 Исходный код](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/DDmoveFullcontrol.yaml)
  
  

  [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint url pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/DDmoveFullcontrol.yaml)

  ---

  <details>
    <summary><b>Подробное описание</b></summary>
    <strong>Version: 1.2</strong><br>
<strong>Change Log (v1.2):</strong> Фильтрация «дребезга» датчиков (0.5с на вкл / 2с на выкл) и фикс опциональности датчика двери. / Added sensor anti-bounce filtering and fixed optional door sensor issue.<br><br>

<strong>Основное что делает блупринт:</strong><br>
Универсальная автоматизация для управления светом: включает свет при движении или открытии двери, запускает таймер при отсутствии движения и выключает свет по его завершении. Содержит встроенную защиту от «дребезга» датчиков и ложных срабатываний. Поддерживает глобальные условия и дополнительные действия после выключения.<br><br>

<details>
<summary>Еще мои блупринты</summary>
<ul>
  <li><a href="https://github.com/smirnowegor/HomeAssistant_blueprints">Git</a></li>
</ul>
</details>

<details>
<summary>💡 Главная идея</summary>
<p>Шаблон объединяет несколько источников триггеров и даёт гибкие настройки тайм-аута. Удобен для мест с нестабильно работающими датчиками благодаря программной фильтрации сигналов.</p>
<ol>
  <li><strong>Надежность</strong> — игнорирует кратковременные ложные срабатывания датчиков движения.</li>
  <li><strong>Гибкость</strong> — длительность через input_number, поддержка условий и пост-действий.</li>
  <li><strong>Интеграция</strong> — выполнение любых действий (сцены, шторы) после выключения света.</li>
</ol>
</details>

<details>
<summary>⚙️ Как это работает (кратко)</summary>
<ol>
  <li><strong>Старт:</strong> движение (длительностью >0.5с) или дверь → включаем свет, отменяем таймер.</li>
  <li><strong>Остановка движения:</strong> если движения нет более 2с → запускаем таймер на X минут.</li>
  <li><strong>Защита:</strong> блокировка повторного срабатывания на 4 секунды для предотвращения «петли».</li>
  <li><strong>Финиш:</strong> по завершении таймера — выключаем свет и выполняем доп. действия.</li>
</ol>
</details>

<hr>

<strong>What the blueprint does:</strong><br>
Universal automation for lighting: turns lights on on motion or door open, starts a timer on motion off and turns lights off when finished. Features built-in sensor anti-bounce and loop protection. Supports global conditions and additional post-off actions.<br><br>

<details>
<summary>More blueprints</summary>
<ul>
  <li><a href="https://github.com/smirnowegor/HomeAssistant_blueprints">Git</a></li>
</ul>
</details>

<details>
<summary>💡 Main idea (Click to expand)</summary>
<p>This blueprint combines multiple trigger sources and provides flexible timeout settings. It is ideal for areas with "noisy" sensors thanks to software signal filtering.</p>
<ol>
  <li><strong>Reliability</strong> — ignores short false motion signals (anti-bounce).</li>
  <li><strong>Flexibility</strong> — duration via input_number, supports conditions and post-actions.</li>
  <li><strong>Integration</strong> — run any actions (scripts, covers) after lights turn off.</li>
</ol>
</details>

<details>
<summary>⚙️ How it works (short)</summary>
<ol>
  <li><strong>Start:</strong> motion (>0.5s) or door open → turn lights on and cancel timer.</li>
  <li><strong>Motion off:</strong> if no motion for >2s → start timer for X minutes.</li>
  <li><strong>Protection:</strong> 4-second cooldown to prevent re-triggering loops.</li>
  <li><strong>Finish:</strong> when timer finishes → turn lights off and run additional actions.</li>
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

#### automation


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


### 🤖 Универсальная автоматизация управления светом (движение + дверь + таймер) / Universal light control (motion + door + timer)
<details>
  <summary><b>📖 Expand Description and Installation</b></summary>
  
  **Category:** automation | [📂 Source Code](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/DDmoveFullcontrol.yaml)
  
  

  [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint url pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/DDmoveFullcontrol.yaml)

  ---

  <details>
    <summary><b>Detailed Description</b></summary>
    <strong>Version: 1.2</strong><br>
<strong>Change Log (v1.2):</strong> Фильтрация «дребезга» датчиков (0.5с на вкл / 2с на выкл) и фикс опциональности датчика двери. / Added sensor anti-bounce filtering and fixed optional door sensor issue.<br><br>

<strong>Основное что делает блупринт:</strong><br>
Универсальная автоматизация для управления светом: включает свет при движении или открытии двери, запускает таймер при отсутствии движения и выключает свет по его завершении. Содержит встроенную защиту от «дребезга» датчиков и ложных срабатываний. Поддерживает глобальные условия и дополнительные действия после выключения.<br><br>

<details>
<summary>Еще мои блупринты</summary>
<ul>
  <li><a href="https://github.com/smirnowegor/HomeAssistant_blueprints">Git</a></li>
</ul>
</details>

<details>
<summary>💡 Главная идея</summary>
<p>Шаблон объединяет несколько источников триггеров и даёт гибкие настройки тайм-аута. Удобен для мест с нестабильно работающими датчиками благодаря программной фильтрации сигналов.</p>
<ol>
  <li><strong>Надежность</strong> — игнорирует кратковременные ложные срабатывания датчиков движения.</li>
  <li><strong>Гибкость</strong> — длительность через input_number, поддержка условий и пост-действий.</li>
  <li><strong>Интеграция</strong> — выполнение любых действий (сцены, шторы) после выключения света.</li>
</ol>
</details>

<details>
<summary>⚙️ Как это работает (кратко)</summary>
<ol>
  <li><strong>Старт:</strong> движение (длительностью >0.5с) или дверь → включаем свет, отменяем таймер.</li>
  <li><strong>Остановка движения:</strong> если движения нет более 2с → запускаем таймер на X минут.</li>
  <li><strong>Защита:</strong> блокировка повторного срабатывания на 4 секунды для предотвращения «петли».</li>
  <li><strong>Финиш:</strong> по завершении таймера — выключаем свет и выполняем доп. действия.</li>
</ol>
</details>

<hr>

<strong>What the blueprint does:</strong><br>
Universal automation for lighting: turns lights on on motion or door open, starts a timer on motion off and turns lights off when finished. Features built-in sensor anti-bounce and loop protection. Supports global conditions and additional post-off actions.<br><br>

<details>
<summary>More blueprints</summary>
<ul>
  <li><a href="https://github.com/smirnowegor/HomeAssistant_blueprints">Git</a></li>
</ul>
</details>

<details>
<summary>💡 Main idea (Click to expand)</summary>
<p>This blueprint combines multiple trigger sources and provides flexible timeout settings. It is ideal for areas with "noisy" sensors thanks to software signal filtering.</p>
<ol>
  <li><strong>Reliability</strong> — ignores short false motion signals (anti-bounce).</li>
  <li><strong>Flexibility</strong> — duration via input_number, supports conditions and post-actions.</li>
  <li><strong>Integration</strong> — run any actions (scripts, covers) after lights turn off.</li>
</ol>
</details>

<details>
<summary>⚙️ How it works (short)</summary>
<ol>
  <li><strong>Start:</strong> motion (>0.5s) or door open → turn lights on and cancel timer.</li>
  <li><strong>Motion off:</strong> if no motion for >2s → start timer for X minutes.</li>
  <li><strong>Protection:</strong> 4-second cooldown to prevent re-triggering loops.</li>
  <li><strong>Finish:</strong> when timer finishes → turn lights off and run additional actions.</li>
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

