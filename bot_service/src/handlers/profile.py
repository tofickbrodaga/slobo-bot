from aiogram import F
from aiogram.types import Message, CallbackQuery, User
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.handlers.router import router
from config.settings import settings
from src.templates.env import render
from src.states import add_meme, profile, public_busket
from src.keyboards.profile import KEYBOARD


@router.message(Command('profile'))
@router.message(F.text == settings.PROFILE_BUTTON)
async def profile_message(message: Message, state: FSMContext, user: User = None) -> None:
    if user is None:
        user = message.from_user
    user_data = {
        'full_name': user.full_name,
        'username': user.username,
        'uploaded_memes_count': 0,
        'personal_memes_count': 0,
    }
    await state.set_state(profile.Profile.showing_profile)
    await message.answer(
        text=render('profile.jinja2', **user_data),
        reply_markup=KEYBOARD,
    )
    await message.delete()


@router.callback_query(add_meme.AddMeme.waiting_meme, F.data == settings.RETURN_BACK_QUERY)
@router.callback_query(public_busket.PublicBusket.showing_popular, F.data == settings.RETURN_BACK_QUERY)
@router.callback_query(public_busket.PublicBusket.showing_random, F.data == settings.RETURN_BACK_QUERY)
async def profile_query(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer()
    await profile_message(query.message, state, query.from_user)
