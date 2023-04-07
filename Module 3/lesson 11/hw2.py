import requests
import telebot
from telebot.types import ReplyKeyboardMarkup

TOKEN = '6268534092:AAGthtYiTy4pp6UHP4kLYWaF7HRnXt3j03M'

data = None

def get_keys():
    global data
    URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(URL).json()
    data = response
    return data['Valute'].values()


bot = telebot.TeleBot(TOKEN)
keyboard = ReplyKeyboardMarkup(row_width=1)
keyboard.add(*[d['Name'] for d in get_keys()])


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     'Я тестовый бот!',
                     reply_markup=keyboard)


bot.infinity_polling()
