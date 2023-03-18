#Импорт библиотек
import os
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from module import config, logger, Body, database

storage = MemoryStorage()
bot = Bot(token=config.api_key, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
bd = database.BASEDATA()

Body.register_handlers(dp=dp)

if __name__ == '__main__':
    os.system('clear')
    os.system('cls')
    logger.success('Чат-бот запущен и успешно выполняет свои обязанности,происходит подключение к базе данных...')
    bd.create_usertable()
    
executor.start_polling(dp)

