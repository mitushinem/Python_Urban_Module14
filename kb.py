from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton('Купить')],
    [KeyboardButton('Рассчитать'), KeyboardButton('Информация')],
    [KeyboardButton('Регистрация')],
], resize_keyboard=True)

kb_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton('Формулы расчёта', callback_data='formulas')]
    ]
)

kb_product_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Product1', callback_data='product_buying|Product1'),
            InlineKeyboardButton('Product2', callback_data='product_buying|Product2'),
            InlineKeyboardButton('Product3', callback_data='product_buying|Product3'),
            InlineKeyboardButton('Product4', callback_data='product_buying|Product4')
        ]
    ]
)
