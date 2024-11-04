from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.handlers.router import router
from config.settings import settings
from src.templates.env import render
from src.states.profile import Profile
from src.states.public_busket import PublicBusket
from src.keyboards.random_meme import KEYBOARD


@router.message(Command('random'))
async def random_meme_message(message: Message, state: FSMContext) -> None:
    await state.set_state(PublicBusket.showing_random)
    await message.answer(
        text=render('random_meme.jinja2', text='random'),
        reply_markup=KEYBOARD,
    )
    await message.delete()


@router.callback_query(PublicBusket.showing_random, F.data == settings.RANDOM_MEME_QUERY)
@router.callback_query(Profile.showing_profile, F.data == settings.RANDOM_MEME_QUERY)
async def random_meme_query(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer()
    await random_meme_message(query.message, state)
