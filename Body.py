from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from module import config, keyboard, logger, database
from aiogram.dispatcher.filters.state import State, StatesGroup
import random
import datetime

bd = database.BASEDATA()
bot = Bot(token=config.api_key)

class Create_Item_Attractions(StatesGroup):
    name = State()
    url_google_maps = State()
    descriptions = State()
    picture = State()

# ["Welcome"] ==============================================

async def welcome(msg: types.Message):
    if bd.find_user(id=msg.from_user.id).fetchone() is None:
        bd.create_user(msg.from_user.username, msg.from_user.id, 'Начинающий историк', datetime.datetime.now())
    await msg.answer('''
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

# [Профиль юзера] ==============================================

async def profile(msg: types.Message):
    checkers = bd.check_profile(id=msg.from_user.id)
    await bot.send_message(chat_id=msg.chat.id, text=f'''
<code>📑 Бот Маресеевич / Профиль пользователя </code>

Имя: {checkers[0]}
Статус: {checkers[2]}
Баланс: {checkers[1]} рублей
Дата регистрации: {checkers[4]}

<b>Разработчик</b> » @raizyxadev
''', parse_mode='HTML')

# ["Attraction City"] ==============================================

async def create_attraction(msg: types.Message, state: FSMContext):
    if msg.from_user.id in config.owners_id:
        await bot.send_message(chat_id=msg.chat.id, text=f'{msg.chat.id}, напишите название Достопримечательности')
        Create_Item_Attractions.name.set()

async def add_url_attr(msg: types.Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await bot.send_message(chat_id=msg.chat.id, text=f'Хорошо, теперь киньте мне ссылку на Достопримечательность на карте Google или Яндекс')
    await Create_Item_Attractions.next()

def register_handlers(dp : Dispatcher):
    dp.register_message_handler(faqinfo, text="📔 F.A.Q")
    dp.register_message_handler(supportOpen, text="🎧 Техническая поддержка")
    dp.register_message_handler(welcome, commands=['start'])
    dp.register_message_handler(attractioncity, text="🕌 Достопримечательности края")
    dp.register_message_handler(profile, text=['🎧 Профиль'])
    dp.register_message_handler(create_attraction, text=['Добавить достопримечательность'])
    dp.register_callback_query_handler(add_url_attr, state= Create_Item_Attractions.name)