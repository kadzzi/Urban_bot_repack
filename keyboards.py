from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.Products_DB import get_all_products


kb = ReplyKeyboardMarkup(resize_keyboard=True)
calc_button = KeyboardButton(text="Рассчитать")
info_button = KeyboardButton(text="Информация")
reg_button = KeyboardButton(text="Регистрация")
buy_button = KeyboardButton(text="Купить")
kb.row(calc_button, info_button)
kb.add(reg_button)
kb.add(buy_button)

inl_kb = InlineKeyboardMarkup()
inl_calc_button = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
inl_form_button = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
inl_kb.row(inl_calc_button, inl_form_button)

gender_kb = InlineKeyboardMarkup()
male_button = InlineKeyboardButton(text="Муж.", callback_data="male")
female_button = InlineKeyboardButton(text="Жен.", callback_data="female")
gender_kb.row(male_button, female_button)

purchase_kb = InlineKeyboardMarkup()
for item in get_all_products():
    purchase_kb.add(InlineKeyboardButton(text=item[0], callback_data="product_buying"))
