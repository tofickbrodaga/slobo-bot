from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.handlers.router import router
from config.settings import settings
from src.templates.env import render
from src.states.profile import Profile
from src.states.public_busket import PublicBusket
from src.keyboards.popular_meme import keyboard


@router.message(Command('popular'))
async def popular_meme_message(message: Message, state: FSMContext) -> None:
    await state.set_state(PublicBusket.showing_popular)
    number = (await state.get_data()).get('number')
    await message.answer(
        text=render('popular_meme.jinja2', text='popular', top_number=number+1),
        reply_markup=keyboard(number),
    )
    await message.delete()


@router.callback_query(Profile.showing_profile, F.data == settings.POPULAR_MEME_QUERY)
async def popular_meme_query(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer()
    number = (await state.get_data()).get('number')
    if not number:
        await state.update_data(number=0)
    await popular_meme_message(query.message, state)


@router.callback_query(PublicBusket.showing_popular, F.data == settings.NEXT_PAGE_QUERY)
async def next_popular_meme_query(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer()
    number = (await state.get_data())['number'] + 1
    await state.update_data(number=number)
    await query.message.edit_text(
        text=render('popular_meme.jinja2', text='popular', top_number=number+1),
        reply_markup=keyboard(number),
    )


@router.callback_query(PublicBusket.showing_popular, F.data == settings.PREVIOUS_PAGE_QUERY)
async def previous_popular_meme_query(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer()
    number = (await state.get_data())['number'] - 1
    await state.update_data(number=number)
    await query.message.edit_text(
        text=render('popular_meme.jinja2', text='popular', top_number=number+1),
        reply_markup=keyboard(number),
    )
