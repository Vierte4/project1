from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

organizators_main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🚀 Новый обмен'),
            KeyboardButton(text='🏦 Резервы валют')
        ],
        [
            KeyboardButton(text='🔑 Создать аккаунт'),
            KeyboardButton(text='💰 Запросить резерв')
        ],
        [
            KeyboardButton(text='😻 Оставить отзыв'),
            KeyboardButton(text='🌎 Изменить язык')
        ],

    ],
    resize_keyboard=True
)
