from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from module import config, keyboard, logger
from aiogram.dispatcher.filters.state import State, StatesGroup
import random
import datetime

logger.info('Тело работает')

# ["Welcome"] ==============================================

async def welcome(message):
    await message.answer('''
<code>📑 Бот Маресеевич / Приветствие</code>

📌 Ты попал в гости к Маресеевичу 🛕
⚡️ Здесь вы,молодые историки, можете изучить историю Хабаровского края! 
👨🏻‍💻 Тех.Поддержка - @raizyxadev

Удачных вам новых открытий и путешествий!
    
    ''',reply_markup = keyboard.startbutton())


# ["Attraction City"] ==============================================

async def attractioncity(message):
    await message.answer('ЭМ')

# ["F.A.Q"] ==============================================

async def faqinfo(message):
    await message.answer('''
<code>📑 Бот Маресеевич / F.A.Q проекта</code>

1. <b> Что такое проект? </b>
- Проект - это совокупность работ, направленных на достижение определенной цели в определенный срок.

2. <b> Какие цели ставит перед собой наш проект? </b>
- Цели проекта: улучшение и упрощение изучения исторических материалов, связанных с Хабаровским краем.Знакомство нового поколения с историей своих предков и своего региона.

3. <b> Каковы основные этапы проекта? </b>
- Основные этапы нашего проекта: Создание модели чат-бота с исскуственным интеллектом,способного подсказать вам любой  

4. <b> Какие инструменты используются в проекте? </b>
- В проекте используются различные инструменты: программное обеспечение для управления проектом, системы контроля версий, системы управления задачами и т.д
    ''')
# [Пункт меню "Поддержка"] ==============================================

async def supportOpen(message):
    await message.answer('''
<code>📑 Бот Маресеевич / Техническая Поддержка</code>

Здесь вы можете связаться с администрацией проекта или технической поддержкой,
чтобы задать свой вопрос: по улучшению проекта,исправлению багов и тд

<b>Разработчик</b> » @raizyxadev
''')

def register_handlers(dp : Dispatcher):
    dp.register_message_handler(faqinfo, text="📔 F.A.Q")
    dp.register_message_handler(supportOpen, text="🎧 Техническая поддержка")
    dp.register_message_handler(welcome, commands=['start'])
    dp.register_message_handler(attractioncity,text="🕌 Достопримечательности края")
    