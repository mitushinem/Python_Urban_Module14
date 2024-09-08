from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(UserState):
    username = State()
    email = State()
    age = State()
    balance = State()
