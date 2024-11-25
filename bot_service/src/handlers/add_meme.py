from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from src.templates.env import render
from src.states.add_meme import AddMeme
from src.handlers.router import router
from src.handlers.profile import profile_message
from src.keyboards.add_meme import KEYBOARD


@router.callback_query()
async def add_meme(query: CallbackQuery, state: FSMContext) -> None:
    await query.message.edit_text(
        text=render('add_meme.jinja2'),
        reply_markup=KEYBOARD,
    )
    await state.set_state(AddMeme.waiting_meme)


@router.message(AddMeme.waiting_meme)
async def waiting_meme(message: Message, state: FSMContext) -> None:
    try:
        image = message.photo[0].file_id
    except TypeError:
        await message.answer(
            text=render('no_photo.jinja2'),
            reply_markup=KEYBOARD,
        )
        return
    text = message.caption
    await message.answer(
        text=render('meme_loaded.jinja2', photo_id=image, text=text),
        reply_markup=KEYBOARD,
    )
    await profile_message(message, state)