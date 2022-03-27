import datetime

from aiogram.dispatcher import FSMContext
from keyboards.default import organizators_main_keyboard
from loader import dp, bot
from data.config import USERS
from aiogram import types
from aiogram.types import CallbackQuery


@dp.message_handler(commands='Start')
async def send_main_kb(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=organizators_main_keyboard)
n = [0]
