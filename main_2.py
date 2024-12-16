import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery


from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! Выберите действие:",
        reply_markup=kb.main_menu
    )

@dp.message(F.text == "Привет")
async def greet(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")


@dp.message(F.text == "Пока")
async def goodbye(message: Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")

@dp.message(Command("links"))
async def links(message: Message):
    await message.answer("Вот ссылки, которые могут вас заинтересовать:", reply_markup=kb.links_menu)


import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! Выберите действие:",
        reply_markup=kb.main_menu
    )


@dp.message(F.text == "Привет")
async def greet(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")


@dp.message(F.text == "Пока")
async def goodbye(message: Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")


@dp.message(Command("links"))
async def links(message: Message):
    await message.answer("Вот ссылки, которые могут вас заинтересовать:", reply_markup=kb.links_menu)


@dp.message(Command("dynamic"))
async def dynamic_keyboard(message: Message):
    await message.answer("Вот динамическая кнопка:", reply_markup=kb.dynamic_start)


@dp.callback_query(F.data == "show_more")
async def show_more(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=kb.dynamic_options)


@dp.callback_query(F.data.in_({"option_1", "option_2"}))
async def choose_option(callback: CallbackQuery):
    selected_option = "Опция 1" if callback.data == "option_1" else "Опция 2"
    await callback.answer(f"Вы выбрали: {selected_option}", show_alert=True)
    await callback.message.edit_reply_markup()  # Убираем кнопки после выбора


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())



async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())
