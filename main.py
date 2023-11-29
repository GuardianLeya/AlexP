import telebot
import random
from telebot import types

TOKEN = '6890523392:AAFFcOlp04PPKMECaA2ORRvXKHk3B6aNLEM'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Предсказать судьбу')
    markup.add(button)
    bot.send_message(message.chat.id, "Привет! Я предсказатель судьбы.\nЯ помогу тебе определиться с выбором!\n Нажми на кнопку, чтобы получить ответ на твой вопрос.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def send_prediction(message):
    if message.text == 'Предсказать судьбу':
        predictions = [
            'Да',
            'Нет',
            'Возможно',
            'Лучше не рассказывать',
            'Попробуй еще раз позже'
        ]
        bot.send_message(message.chat.id, random.choice(predictions))


bot.polling()
