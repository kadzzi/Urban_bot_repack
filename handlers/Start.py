from keyboards import kb


async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


async def get_info(message):
    await message.answer("У нас Вы можете приобрести полезные продукты и подобрать для себя оптимальную диету", reply_markup=kb)
