from aiogram.dispatcher.filters.state import State, StatesGroup
from database.Users_DB import is_included, add_user
from keyboards import kb


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


async def set_username(message, state):
    if is_included(message.text):
        await message.answer(f"Пользователь {message.text} существует, введите другое имя")
        await RegistrationState.username.set()
    else:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()


async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


async def set_age_db(message, state):
    await state.update_data(age=int(message.text))
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    if is_included(data['username']):
        await message.answer(f"Вы успешно зарегистрированы под ником {data['username']}", reply_markup=kb)
    else:
        await message.answer("Что-то пошло не так. Попробуйте повторить регистрацию чуть позже.", reply_markup=kb)
    await state.finish()
