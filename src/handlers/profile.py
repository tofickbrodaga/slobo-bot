from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.handlers.router import router
from config.settings import settings
from src.templates.env import render

@router.message(F.text == settings.PROFILE_BUTTON_TEXT)
async def profile(message: Message, state: FSMContext) -> None:
    user_data = {
        'full_name': message.from_user.full_name,
        'username': message.from_user.username,
        'uploaded_memes_count': 0,
        'personal_memes_count': 0,

    }
    await message.answer(
        text=render('profile.jinja2', **user_data),
    )