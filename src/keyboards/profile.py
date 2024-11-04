from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config.settings import settings

KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=settings.ADD_MEME_BUTTON,
                callback_data=settings.ADD_MEME_QUERY,
            ),
        ],
        [
            InlineKeyboardButton(
                text=settings.RANDOM_MEME_BUTTON,
                callback_data=settings.RANDOM_MEME_QUERY,
            ),
        ],
        [
            InlineKeyboardButton(
                text=settings.MOST_POPUAR_MEME_BUTTON,
                callback_data=settings.MOST_POPUAR_MEME_QUERY,
            )
        ],
        [
            InlineKeyboardButton(
                text=settings.PERSONAL_MEMES_BUTTON,
                callback_data=settings.PERSONAL_MEMES_QUERY,
            ),
        ],
        [
            InlineKeyboardButton(
                text=settings.RANDOM_PERSONAL_MEME_BUTTON,
                callback_data=settings.RANDOM_PERSONAL_MEME_QUERY,
            ),
        ],
    ],
)