import telebot
# import sqlite3
from telebot import types
bot = telebot.TeleBot('6582298193:AAF5qCksB2mB9IzPtIf1vod3mCXxB0zg7f8')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Общение')
    item2 = types.KeyboardButton('Поботать')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Привет! Давай выберем цель'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Общение':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        sport = types.KeyboardButton('Спорт')
        art = types.KeyboardButton('Искусство')
        proj = types.KeyboardButton('Проекты')
        party = types.KeyboardButton('Тусовки')
        ex = types.KeyboardButton('Вернуться в главное меню')
        markup.add(sport, art, proj, party, ex)
        bot.send_message(message.chat.id, 'Выбери тему для общения'.format(message.from_user), reply_markup=markup)
    elif message.text == 'Спорт':
        bot.send_message(message.chat.id, 'https://t.me/+dY-trJ_5UyhiYTBi')
    elif message.text == 'Искусство':
        bot.send_message(message.chat.id, 'https://t.me/+gsCp_euLpkdkMWMy')
    elif message.text == 'Проекты':
        bot.send_message(message.chat.id, 'https://t.me/+UMTfzAL7ZcgzOTU6')
    elif message.text == 'Тусовки':
        bot.send_message(message.chat.id, 'https://t.me/+aFwqT2Q4zao2NWRi')
    elif message.text == 'Поботать':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1k = types.KeyboardButton('1 курс')
        item2k = types.KeyboardButton('2 курс')
        item3k = types.KeyboardButton('3 курс')
        item4k = types.KeyboardButton('4 курс')
        ex = types.KeyboardButton('Вернуться в главное меню')
        markup.add(item1k, item2k, item3k, item4k, ex)
        bot.send_message(message.chat.id, 'Давай выберем курс'.format(message.from_user), reply_markup=markup)
    elif message.text == 'ИТКН':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itkn1math = types.KeyboardButton('Математика')
        itkn1machine = types.KeyboardButton('Вычмаш')
        itkn1proga = types.KeyboardButton('Прога')
        ex = types.KeyboardButton('Вернуться в главное меню')
        markup.add(itkn1math, itkn1machine, itkn1proga, ex)
        bot.send_message(message.chat.id, 'Давай выберем предмет'.format(message.from_user), reply_markup=markup)
    elif message.text == '2 курс':
        bot.send_message(message.chat.id, 'в процессе разработки...')
    elif message.text == 'Математика':
        bot.send_message(message.chat.id, 'https://t.me/+0GM40f_u1bo1MTky')
    elif message.text == 'Вычмаш':
        bot.send_message(message.chat.id, 'https://t.me/+CsL4fOCHhzIzZTZi')
    elif message.text == 'Прога':
        bot.send_message(message.chat.id, 'https://t.me/+qRgmsWiHGVwwNzMy')
    elif message.text == '3 курс':
        bot.send_message(message.chat.id, 'в процессе разработки...')
    elif message.text == '4 курс':
        bot.send_message(message.chat.id, 'в процессе разработки...')
    elif message.text == 'ЭкоТех':
        bot.send_message(message.chat.id, 'в процессе разработки...')
    elif message.text == 'ИНМиН':
        bot.send_message(message.chat.id, 'в процессе разработки...')
    elif message.text == 'ЭУПП':
        bot.send_message(message.chat.id, 'в процессе разработки...')
    elif message.text == 'ГИ':
        bot.send_message(message.chat.id, 'в процессе разработки...')
    elif message.text == 'ИБО':
        bot.send_message(message.chat.id, 'в процессе разработки...')
    elif message.text == '1 курс':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        in11k = types.KeyboardButton('ЭкоТех')
        in21k = types.KeyboardButton('ИНМиН')
        in31k = types.KeyboardButton('ЭУПП')
        in41k = types.KeyboardButton('ИТКН')
        in51k = types.KeyboardButton('ГИ')
        in61k = types.KeyboardButton('ИБО')
        ex = types.KeyboardButton('Вернуться в главное меню')
        markup.add(in11k, in21k, in31k, in41k, in51k, in61k, ex)
        bot.send_message(message.chat.id, 'Давай выберем институт'.format(message.from_user), reply_markup=markup)
    elif message.text == 'Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Общение')
        item2 = types.KeyboardButton('Поботать')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Выбери цель'.format(message.from_user), reply_markup=markup)


bot.polling(none_stop=True)
#   bot.infinity_polling() - альтернатива предыдущей команде
