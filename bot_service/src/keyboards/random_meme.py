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
        [
            InlineKeyboardButton(
                text=settings.SAVE_MEME_BUTTON,
                callback_data=settings.SAVE_MEME_QUERY,
            )
        ],
        [
            InlineKeyboardButton(
                text=settings.LIKE_BUTTON,
                callback_data=settings.LIKE_QUERY,
            ),
            InlineKeyboardButton(
                text=settings.DISLIKE_BUTTON,
                callback_data=settings.DISLIKE_QUERY,
            ),
        ],
        [
            InlineKeyboardButton(
                text=settings.NEXT_RANDOM_MEME_BUTTON,
                callback_data=settings.NEXT_RANDOM_MEME_QUERY,
            )
        ]
    ],
)