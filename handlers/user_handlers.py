from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from aiogram import Router, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from services.services import get_bot_choice, get_winner
from keyboards.keyboards import game_kb, kb_builder, inline_key

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start_play']
                         , reply_markup=inline_key)

@router.callback_query(F.data=='b1')
async def process_buttons_1_press(callback: CallbackQuery):
    if callback.message.text != "change 1":
        await callback.message.edit_text(
            text='change 1',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer()

@router.callback_query(F.data=='b2')
async def process_button_2_press(callback: CallbackQuery):
    if callback.message.text != "change 2":
        await callback.message.edit_text(
            text="change 2",
            reply_markup=callback.message.reply_markup
        )
    await callback.answer()

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'],
                         reply_markup=kb_builder)

@router.message(F.text == LEXICON_RU['yes_button'])
async def play_yes(message: Message):
    await message.answer(
        text = LEXICON_RU['yes'],
        reply_markup=game_kb
    )

@router.message(F.text==LEXICON_RU['no_button'])
async def play_no(message: Message):
    await message.answer(
        text=LEXICON_RU['no']
    )

@router.message(F.text.in_( [LEXICON_RU['rock'], LEXICON_RU['scissors'], LEXICON_RU['paper']]) )
async def process_dame_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU['bot_choice']}'
                         f' - {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=kb_builder)