from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config.settings import settings


def keyboard(page_number: int, max_page: int = 9) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=settings.RETURN_BACK_BUTTON,
        callback_data=settings.RETURN_BACK_QUERY,
    )
    builder.button(
        text=settings.SAVE_MEME_BUTTON,
        callback_data=settings.SAVE_MEME_QUERY,
    )
    builder.button(
        text=settings.LIKE_BUTTON,
        callback_data=settings.LIKE_QUERY,
    )
    builder.button(
        text=settings.DISLIKE_BUTTON,
        callback_data=settings.DISLIKE_QUERY,
    )
    if page_number > 0:
        builder.button(
            text=settings.PREVIOUS_PAGE_BUTTON,
            callback_data=settings.PREVIOUS_PAGE_QUERY,
        )
    if page_number < max_page:
        builder.button(
            text=settings.NEXT_PAGE_BUTTON,
            callback_data=settings.NEXT_PAGE_QUERY,
        )
    builder.adjust(1, 1, 2, 2)
    return builder.as_markup()
