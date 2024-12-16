from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
    ],
    resize_keyboard=True
)

#ДЗ-1
links_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Новости", url="https://ru.wikipedia.org/wiki/Новости")],
        [InlineKeyboardButton(text="Музыка", url="https://ru.wikipedia.org/wiki/Музыка")],
        [InlineKeyboardButton(text="Видео", url="https://ru.wikipedia.org/wiki/Видео")]
    ]
)

dynamic_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
    ]
)

dynamic_options = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Опция 1", callback_data="option_1"), InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
    ]
)
