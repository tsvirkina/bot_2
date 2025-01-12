from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU


key_builder = ReplyKeyboardBuilder()

button_yes = KeyboardButton(
    text=LEXICON_RU['yes_button']
)

button_no = KeyboardButton(
    text=LEXICON_RU['no_button']
)

key_builder.row(button_yes, button_no, width=1)
kb_builder: ReplyKeyboardMarkup = key_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)


"""Клавиатура для игры"""
button_rock = KeyboardButton(text=LEXICON_RU['rock'])
button_scissors = KeyboardButton(text=LEXICON_RU['scissors'])
button_paper = KeyboardButton(text=LEXICON_RU['paper'])

game_kb = ReplyKeyboardMarkup(
    keyboard=
    [[button_rock],
     [button_scissors],
     [button_paper]],
     resize_keyboard=True
)

inline_button_1 = InlineKeyboardButton(
    text = "Кнопка 1",
    callback_data="b1"
)

inline_button_2 = InlineKeyboardButton(
    text = "Кнопка 2",
    callback_data="b2"
)

inline_key = InlineKeyboardMarkup(
    inline_keyboard=[[inline_button_1],[inline_button_2]]
)
