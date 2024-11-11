from aiogram.fsm.state import StatesGroup, State


class AddMeme(StatesGroup):
    waiting_meme = State()