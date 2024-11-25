from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config.settings import settings


KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=settings.RETURN_BACK_BUTTON,
                callback_data=settings.RETURN_BACK_QUERY,
            ),
        ],
    ],
)