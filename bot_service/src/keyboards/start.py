from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config.settings import settings

KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=settings.PROFILE_BUTTON)],
    ],
    resize_keyboard=True,
)
