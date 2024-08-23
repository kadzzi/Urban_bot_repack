from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import handlers.Start
import handlers.Registration
import handlers.PurchaseProduct
import handlers.Calories

from config import api


bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


dp.message_handler(commands=['start'])(handlers.Start.start)
dp.message_handler(text=["Информация"])(handlers.Start.get_info)

dp.message_handler(text=['Регистрация'])(handlers.Registration.sing_up)
dp.message_handler(state=handlers.Registration.RegistrationState.username)(handlers.Registration.set_username)
dp.message_handler(state=handlers.Registration.RegistrationState.email)(handlers.Registration.set_email)
dp.message_handler(state=handlers.Registration.RegistrationState.age)(handlers.Registration.set_age_db)

dp.message_handler(text=['Купить'])(handlers.PurchaseProduct.get_buying_list)
dp.callback_query_handler(text="product_buying")(handlers.PurchaseProduct.send_confirm_message)

dp.message_handler(text=["Рассчитать"])(handlers.Calories.main_calc_menu)
dp.callback_query_handler(text="formulas")(handlers.Calories.get_formulas)
dp.callback_query_handler(text="calories")(handlers.Calories.set_age_cal)
dp.message_handler(state=handlers.Calories.UserState.age)(handlers.Calories.set_growth)
dp.message_handler(state=handlers.Calories.UserState.growth)(handlers.Calories.set_weight)
dp.message_handler(state=handlers.Calories.UserState.weight)(handlers.Calories.set_gender)
dp.callback_query_handler(state=handlers.Calories.UserState.gender, text="male")(handlers.Calories.send_calories_male)
dp.callback_query_handler(state=handlers.Calories.UserState.gender, text="female")(handlers.Calories.send_calories_female)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)