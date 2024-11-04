from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.handlers.router import router
from config.settings import settings
from src.templates.env import render
from src.states.profile import Profile
from src.states.public_busket import PublicBusket
from src.keyboards.profile import KEYBOARD


@router.message(Command('profile'))
@router.message(F.text == settings.PROFILE_BUTTON)
async def profile_message(message: Message, state: FSMContext) -> None:
    user_data = {
        'full_name': message.from_user.full_name,
        'username': message.from_user.username,
        'uploaded_memes_count': 0,
        'personal_memes_count': 0,
    }
    await state.set_state(Profile.showing_profile)
    await message.answer(
        text=render('profile.jinja2', **user_data),
        reply_markup=KEYBOARD,
    )
    await message.delete()


@router.callback_query(PublicBusket.showing_popular, F.data == settings.RETURN_BACK_QUERY)
@router.callback_query(PublicBusket.showing_random, F.data == settings.RETURN_BACK_QUERY)
async def profile_query(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer()
    await profile_message(query.message, state)
