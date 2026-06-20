# Telegram-BOT-with-FSM


English Version:

# Telegram Quiz Bot with FSM Branching Logic

An asynchronous Telegram bot built on Python that implements a dynamic step-by-step branching quiz using Finite State Machine (FSM). 

## 🛠 Tech Stack:
* **Python 3.12+**
* **Aiogram 3.x** — The leading asynchronous framework for the Telegram Bot API.

## ⚙️ Key Features:
1. **FSM Branching Dialogues:** The bot changes its next question state based on the user's previous answer. If the user feels "good", the bot asks for their age; if they feel "bad", the bot automatically ends the conversation.
2. **Text Normalization:** Uses `.lower()` methods to handle incoming string filters seamlessly regardless of the user's text casing.
3. **Data Validation:** Age input is wrapped in a secure `try/except` block to catch `ValueError` exceptions, preventing the backend from crashing when users enter text instead of digits.
4. **State Lifecycle Management:** Dynamically invokes `state.clear()` at the end of each independent workflow to release user sessions and avoid stuck states.

## 🚀 How to Run:
1. Put your custom bot token from BotFather inside the `bot = Bot(token="...")` object.
2. Run the main script execution.


Russian Version:

# Telegram-бот опросник с логикой ветвления FSM

Асинхронный Telegram-бот на Python, который реализует динамический пошаговый опрос с ветвлением сюжета при помощи конечных автоматов (FSM).

## 🛠 Технологический стек:
* **Python 3.12+**
* **Aiogram 3.x** — ведущий асинхронный фреймворк для Telegram Bot API.

## ⚙️ Основные фичи:
1. **Диалоги с ветвлением FSM:** бот меняет состояние следующего вопроса в зависимости от предыдущего ответа пользователя. Если пользователю «хорошо», бот спрашивает возраст; если «плохо» — бот автоматически завершает диалог.
2. **Нормализация текста:** использует методы `.lower()` для бесшовной обработки входящих строк независимо от регистра букв, введенных пользователем.
3. **Валидация данных:** ввод возраста завернут в безопасный блок `try/except` для отлова исключений `ValueError`. Это защищает бэкенд от падений, если пользователь введет буквы вместо цифр.
4. **Управление жизненным циклом состояний:** динамически вызывает `state.clear()` в конце каждого независимого сценария, чтобы сбросить сессию пользователя и избежать «залипания» кнопок и стейтов.

## 🚀 Как запустить:
1. Вставьте ваш токен от BotFather в объект `bot = Bot(token="...")`.
2. Запустите выполнение скрипта.
