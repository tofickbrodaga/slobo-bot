from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.utils.json_storage import JsonStorage


async def keyboard(section: str) -> InlineKeyboardMarkup:
    json_storage = JsonStorage()
    builder = InlineKeyboardBuilder()
    buttons = json_storage.storage['keyboards'][section]
    for row in buttons:
        row_buttons = [InlineKeyboardButton(**json_storage.format_object(button)) for button in row]
        builder.row(*row_buttons)
    return builder.as_markup()
