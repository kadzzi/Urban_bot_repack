from aiogram.dispatcher.filters.state import State, StatesGroup
from database.Products_DB import get_all_products
from keyboards import kb, purchase_kb


async def get_buying_list(message):
    product_list = get_all_products()
    for i, item_ in enumerate(product_list):
        await message.answer(f'Название: {item_[0]} | Описание: {item_[1]} | Цена: {item_[2]}')
        with open(f'product_imgs/prod_{i + 1}.webp', 'rb') as img:
            await message.answer_photo(img)

    await message.answer('Выберите продукт для покупки:', reply_markup=purchase_kb)


async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!", reply_markup=kb)
    await call.answer()