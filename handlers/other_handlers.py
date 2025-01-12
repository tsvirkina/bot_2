from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from aiogram import Router
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButtonPollType
from aiogram import F


router=Router()

@router.message()
async def send_echo(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])
    