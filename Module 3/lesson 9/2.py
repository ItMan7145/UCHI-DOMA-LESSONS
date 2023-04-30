import telebot
import requests

TOKEN = '6268534092:AAFY4aJMVAntV61vIRDI52ouxRDCBmhvCWU'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def cmd_start_help(message):
    bot.reply_to(message, 'Hello from INDUS! :)')


@bot.message_handler(commands=['cat'])
def cmd_start_help(message):
    response = requests.get('https://cataas.com/cat')
    # print(response.content)
    bot.send_photo(message.chat.id, response.content)
    bot.send_message(message.chat.id, 'i love cats too! :)')
    print(message.from_user)


@bot.message_handler(content_types=['text'])
def cmd_eho(message):
    bot.reply_to(message, message.data)


if __name__ == '__main__':
    print('Start')
    bot.infinity_polling()
