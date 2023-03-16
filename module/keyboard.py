from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


#[Button Menu /Start] =================================================================
def startbutton():
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    attraction = types.KeyboardButton("🕌 Достопримечательности края")
    products = types.KeyboardButton("🛒 Исторические факты")
    info = types.KeyboardButton("📔 F.A.Q")
    help = types.KeyboardButton("🎧 Техническая поддержка")
    start.add(attraction).add(products).add(info,help)
    return start