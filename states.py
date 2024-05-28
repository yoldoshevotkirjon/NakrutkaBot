from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage


class States(StatesGroup):
    phone_number = State()
    follow_username = State()
    send_check = State()
    likes_username = State()
