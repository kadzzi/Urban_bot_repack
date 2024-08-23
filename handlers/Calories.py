from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import kb, inl_kb, gender_kb


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()


async def main_calc_menu(message):
    await message.answer("Выбери опцию:", reply_markup=inl_kb)


async def get_formulas(call):
    await call.message.answer("Муж.: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n"
                              + "Жен.: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()


async def set_age_cal(call):
    await call.message.answer("Введите свой возраст (полных лет):")
    await call.answer()
    await UserState.age.set()


async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост (см.):")
    await UserState.growth.set()


async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес (кг.):")
    await UserState.weight.set()


async def set_gender(message, state):
    await state.update_data(weight=message.text)
    await message.answer("Ваш пол:", reply_markup=gender_kb)
    await UserState.gender.set()


async def send_calories_male(call, state):
    data = await state.get_data()
    result = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await call.message.answer(f"Оптимальное количество калорий: {result}", reply_markup=kb)
    await call.answer()
    await state.finish()


async def send_calories_female(call, state):
    data = await state.get_data()
    result = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161
    await call.message.answer(f"Оптимальное количество калорий: {result}", reply_markup=kb)
    await call.answer()
    await state.finish()