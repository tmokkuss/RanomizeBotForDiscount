from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random

bot = Bot(token='')
dp = Dispatcher(bot)

photos = ['3.png', '4.png', '5.png', '6.png', '7.png']


@dp.message_handler(commands=['start'])
async def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    join = types.KeyboardButton('Получить скидку')
    markup.add(join)
    mess = f'Привет, {message.from_user.first_name} 👋 \nУ тебя появилась уникальная возможность получить скидку на обучение. \nНажимай на кнопку "Получить скидку" и проверь свою удачу! '
    await bot.send_message(message.chat.id, mess, reply_markup=markup)


@dp.message_handler()
async def get_user_text(message):
    if message.text == 'Получить скидку':
        with open(random.choice(photos), 'rb') as photo:
            mess = f'Лови свою скидку и вперед к мечтам!'
            mess2 = f'Чтобы применить скидку напиши мне: @AliceKdesign, и я забронирую место ✍'
            markup = types.InlineKeyboardMarkup()
            remove = types.ReplyKeyboardRemove()
            back_chat = types.InlineKeyboardMarkup()
            back_chat.add(types.InlineKeyboardButton("Вернуться в чат", url='https://t.me/AliceKdesign'))
            markup.add()
            markup.add(types.InlineKeyboardButton("Профессия Веб-дизайнер вместе с Alice K", url='https://alicek.design/web-and-mobile-design-course/'))
            await bot.send_message(message.chat.id, mess, reply_markup=remove)
            await bot.send_photo(message.chat.id, photo, reply_markup=markup)
            await bot.send_message(message.chat.id, mess2, reply_markup=back_chat)
            with open('data.csv', 'a') as csvfile:
                csvfile.write(f'{message.from_user.username} {photo} \n')


executor.start_polling(dp, skip_updates=True)
