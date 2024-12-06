from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from aiogram import Router
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButtonPollType
from aiogram import F


router=Router()
button_1 = KeyboardButton(text='Собака')
button_2 = KeyboardButton(text='Огурец')
keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]], resize_keyboard=True, one_time_keyboard=True)

@router.message(F.text=='?')
async def question_answer(message: Message):
    await message.answer(
        text = "Чего кошки боятся больше?",
        reply_markup=keyboard
    )

@router.message(F.text=='Собака')
async def process_dog_answer(message: Message):
    await message.answer(
        text = 'Да, несомненно, кошки боятся собак. '
             'Но вы видели как они боятся огурцов?',
    )

@router.message(F.text=='Огурец')
async def process_cucumber_answer(message: Message):
    await message.answer(
        text='Да, иногда кажется, что огурцов '
             'кошки боятся больше',
      
    )

@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])