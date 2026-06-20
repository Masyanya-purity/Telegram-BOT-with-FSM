import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


bot = Bot(token="")
dp = Dispatcher()

class answers(StatesGroup):
    hau = State()
    old = State()

@dp.message(CommandStart())
async def start_up(message: types.Message, state: FSMContext):
    await message.answer("Привет как у тебя дела?")

    await state.set_state(answers.hau)

@dp.message(answers.hau)
async def hau_answer(message: types.Message, state: FSMContext):
    await state.update_data(dela=message.text)
    if message.text.lower() == "хорошо" or message.text.lower() == "отлично" or message.text.lower() == "превосходно" :
        await message.answer("Раз дела у тебя идут отлично значит скажи мне сколько тебе лет?")
    elif message.text.lower() == "плохо" or message.text.lower() == "ужасно":
        await message.answer("Ну раз плохо значит покеда")
        await state.clear()
        return
    else:
        await message.answer("я незнаю что ты сказал")
        await state.clear()

    await state.set_state(answers.old)
@dp.message(answers.old)
async def old_answer(message: types.Message, state: FSMContext):
    try:
        await state.update_data(old=message.text)
        if float(message.text) <= 15:
            await message.answer("Ты еще молод")
        elif float(message.text) <= 28:
            await message.answer("Ты уже взрослый")
        else:
            await message.answer("Ты уже стареешь или даже уже слишком стар")
        
        user = await state.get_data()

        hau = user.get("dela")
        old = user.get("old")

        await message.answer(
            f"Тебе лет {old}\n\n"
            f"А дела у тебя {hau}\n"
            "Удачи!"
        )

        await state.clear()
    except ValueError:
        await message.answer('Введи возраст цифрами')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    await main()
