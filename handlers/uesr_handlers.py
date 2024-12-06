from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from aiogram import Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

kb_builder = ReplyKeyboardBuilder()
contact_btn = KeyboardButton(
    text="Отправить телефон",
    request_contact=True
)
location_btn = KeyboardButton(
    text="Отправить геолокацию",
    request_location=True
)
pool_btn = KeyboardButton(
    text="Создать опрос/викторину",
    request_poll = KeyboardButtonPollType()
)

kb_builder.row(contact_btn, location_btn, pool_btn, width=1)
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)
router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start']
                         , reply_markup=keyboard)

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])