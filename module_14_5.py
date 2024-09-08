from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import asyncio
from aiogram.types import ReplyKeyboardRemove

from crud_functions import initiate_db, is_included, add_user
import state
from config import API_KEY
from kb import kb_inline, kb, kb_product_inline
from other import absoluteFilePaths
from crud_functions import get_all_products, initiate_db
from state import UserState, RegistrationState

bot = Bot(token=API_KEY)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text='Регистрация')
async def sing_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    if not is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer(f'Пользователь {message.text} существует, введите другое имя')
        await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)

    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer('Регистрация выполнена успешно!')
    await state.finish()


@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=kb_inline)


@dp.message_handler(text='Информация')
async def info(message: types.Message):
    await message.answer('Информация о боте', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(text=['Купить', 'купить'])
async def get_buying_list(message: types.Message):
    await message.answer('Загрузка прайс-листа', reply_markup=types.ReplyKeyboardRemove())
    all_products = get_all_products()

    img = [i for i in absoluteFilePaths('./img/')]

    for i in range(1, len(img) + 1):
        with open(img[i - 1], 'rb') as f_img:
            await message.answer_photo(
                photo=f_img,
                caption=f'Название: {all_products[i - 1][1]} | Описание: {all_products[i - 1][2]} | Цена: {all_products[i - 1][3]}')
    await message.answer('Выберите продукт для покупки', reply_markup=kb_product_inline)


@dp.callback_query_handler(lambda query: query.data.split('|')[0] == 'product_buying')
async def send_confirm_message(query: types.CallbackQuery):
    data = query.data.split('|')
    await query.message.answer(f'Вы успешно приобрели продукт {data[1]}! ')
    await query.answer()


@dp.callback_query_handler(lambda query: query.data == 'formulas')
async def get_formulas(query: types.CallbackQuery):
    await query.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await query.message.answer('для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await query.answer()


@dp.callback_query_handler(lambda query: query.data == 'calories')
async def set_age(query: types.CallbackQuery):
    await query.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await query.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = (10 * int(data['weight'])) + (6.25 * int(data['growth'])) - (5 * int(data['age'])) + 5
    await message.answer(f'Ваша норма калорий {calories}')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.', reply_markup=types.ReplyKeyboardRemove())


if __name__ == '__main__':
    try:
        initiate_db()

        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(e)
