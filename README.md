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

### 🤖 Стиральная машина: уведомления и напоминания (универсальный Blueprint)!
<details>
  <summary><b>📖 Развернуть описание и установку</b></summary>
  
  **Категория:** automation | [📂 Исходный код](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/washingMachine.yaml)

  [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint url pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/washingMachine.yaml)

  ---

  <details>
    <summary><b>Подробное описание</b></summary>
    <strong>Универсальное решение. Уведомляет о старте/финише, считает стоимость, напоминает о белье.</strong>

<details>
<summary>💡 Главная идея (Нажмите, чтобы раскрыть) 👈</summary>
<p>Этот шаблон решает три основные проблемы:</p>
<ol>
  <li><strong>Забытое белье</strong> — напоминания не дадут вещам «задохнуться» в машине.</li>
  <li><strong>Контроль расходов</strong> — вы узнаёте стоимость конкретной стирки с учётом дневных/ночных тарифов.</li>
  <li><strong>Гибкость</strong> — днём можно использовать голосовые уведомления (Алиса/Google), ночью — тихие уведомления в Telegram.</li>
</ol>
</details>

<details>
<summary>⚙️ Как это работает (Нажмите, чтобы раскрыть) 👈</summary>
<p>Алгоритм:</p>
<ol>
  <li><strong>Старт:</strong> мониторим мощность розетки. Если мощность &gt; порога (например, 10 Вт) в течение заданного времени — считаем, что стирка началась.</li>
  <li><strong>Процесс:</strong> при старте опционально отправляется уведомление «Стирка началась».</li>
  <li><strong>Финиш:</strong> если мощность опускается ниже порога (напр., 5 Вт) и держится указанное время — считаем стирку завершённой.</li>
  <li><strong>Расчёт:</strong> разница показаний utility meter (кВт·ч) умножается на соответствующий тариф (день/ночь).</li>
  <li><strong>Напоминания:</strong> Telegram-уведомление содержит кнопки «Напомнить через...». Если пользователь не реагирует — система будет напоминать автоматически.</li>
</ol>
</details>

<details>
<summary>⚠️ Настройки (Helpers) 👈</summary>
<p>Для работы всех функций создайте или укажите существующие helpers в Home Assistant:</p>
<ul>
  <li><code>input_text.stirka_end_time</code> — хранит время завершения (опционально).</li>
  <li><code>input_number.stirka_start_energy</code> — helper для записи показания energy meter при старте.</li>
  <li><code>input_number.dnevnoi_tarif</code> и <code>input_number.nochnoy_tarif</code> — тарифы (ваша валюта за 1 кВт·ч).</li>
  <li><strong>Utility Meter / sensor</strong> — сенсор, который переводит W → kW·h (обязателен для расчёта стоимости).</li>
  <li><strong>Telegram Bot</strong> — должен быть настроен и доступен через notify-сервис в HA.</li>
</ul>
</details>

<details>
<summary>💰 Поддержать автора 👈</summary>
<p>Если шаблон оказался полезен, поддержите автора:</p>
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
  <li><a href="https://t.me/u2smart4home">Telegram канал (RU with auto-translate)</a></li>
  <li><a href="https://www.youtube.com/@udobni_dom">YouTube: Удобный дом</a></li>
  <li><a href="https://dzen.ru/id/5e32d0969929ba40059b5892">Dzen Profile</a></li>
</ul>
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

### 🤖 Стиральная машина: уведомления и напоминания (универсальный Blueprint)!
<details>
  <summary><b>📖 Expand Description and Installation</b></summary>
  
  **Category:** automation | [📂 Source Code](https://github.com/smirnowegor/HomeAssistant_blueprints/blob/main/blueprints/automation/smirnowegor/washingMachine.yaml)

  [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint url pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smirnowegor/HomeAssistant_blueprints/main/blueprints/automation/smirnowegor/washingMachine.yaml)

  ---

  <details>
    <summary><b>Detailed Description</b></summary>
    <strong>Универсальное решение. Уведомляет о старте/финише, считает стоимость, напоминает о белье.</strong>

<details>
<summary>💡 Главная идея (Нажмите, чтобы раскрыть) 👈</summary>
<p>Этот шаблон решает три основные проблемы:</p>
<ol>
  <li><strong>Забытое белье</strong> — напоминания не дадут вещам «задохнуться» в машине.</li>
  <li><strong>Контроль расходов</strong> — вы узнаёте стоимость конкретной стирки с учётом дневных/ночных тарифов.</li>
  <li><strong>Гибкость</strong> — днём можно использовать голосовые уведомления (Алиса/Google), ночью — тихие уведомления в Telegram.</li>
</ol>
</details>

<details>
<summary>⚙️ Как это работает (Нажмите, чтобы раскрыть) 👈</summary>
<p>Алгоритм:</p>
<ol>
  <li><strong>Старт:</strong> мониторим мощность розетки. Если мощность &gt; порога (например, 10 Вт) в течение заданного времени — считаем, что стирка началась.</li>
  <li><strong>Процесс:</strong> при старте опционально отправляется уведомление «Стирка началась».</li>
  <li><strong>Финиш:</strong> если мощность опускается ниже порога (напр., 5 Вт) и держится указанное время — считаем стирку завершённой.</li>
  <li><strong>Расчёт:</strong> разница показаний utility meter (кВт·ч) умножается на соответствующий тариф (день/ночь).</li>
  <li><strong>Напоминания:</strong> Telegram-уведомление содержит кнопки «Напомнить через...». Если пользователь не реагирует — система будет напоминать автоматически.</li>
</ol>
</details>

<details>
<summary>⚠️ Настройки (Helpers) 👈</summary>
<p>Для работы всех функций создайте или укажите существующие helpers в Home Assistant:</p>
<ul>
  <li><code>input_text.stirka_end_time</code> — хранит время завершения (опционально).</li>
  <li><code>input_number.stirka_start_energy</code> — helper для записи показания energy meter при старте.</li>
  <li><code>input_number.dnevnoi_tarif</code> и <code>input_number.nochnoy_tarif</code> — тарифы (ваша валюта за 1 кВт·ч).</li>
  <li><strong>Utility Meter / sensor</strong> — сенсор, который переводит W → kW·h (обязателен для расчёта стоимости).</li>
  <li><strong>Telegram Bot</strong> — должен быть настроен и доступен через notify-сервис в HA.</li>
</ul>
</details>

<details>
<summary>💰 Поддержать автора 👈</summary>
<p>Если шаблон оказался полезен, поддержите автора:</p>
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
  <li><a href="https://t.me/u2smart4home">Telegram канал (RU with auto-translate)</a></li>
  <li><a href="https://www.youtube.com/@udobni_dom">YouTube: Удобный дом</a></li>
  <li><a href="https://dzen.ru/id/5e32d0969929ba40059b5892">Dzen Profile</a></li>
</ul>
</details>

  </details>
  
</details>
<hr>

<!-- END_BLUEPRINTS_EN -->

## ☕ Support
If my work helped you:  
* [Support on Zen](https://dzen.ru/id/5e32d0969929ba40059b5892?donate=true)  
* [Telegram channel](https://t.me/u2smart4home)
