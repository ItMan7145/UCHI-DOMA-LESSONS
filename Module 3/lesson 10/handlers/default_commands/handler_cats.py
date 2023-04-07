import requests
from loader import bot
from data_config import config
from keyboards.inline import main_keyboard


@bot.message_handler(commands=['cat', 'cats'])
def cmd_search_cat(message):
    bot.send_message(message.chat.id, 'Выберите параметры поиска', reply_markup=main_keyboard.kb_choice_cat())


@bot.callback_query_handler(func=lambda call: True)
def cmd_give_me_cat(callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)

    if callback.data == 'happy':
        response = requests.get('https://cataas.com/cat/happy')
        # print(response.content)
        bot.send_photo(callback.from_user.id, response.content)
        bot.send_message(callback.from_user.id, 'i love happy cats too! :)')
        print(callback.from_user)

    elif callback.data == 'wtf':
        response = requests.get('https://cataas.com/cat/wtf')
        # print(response.content)
        bot.send_photo(callback.from_user.id, response.content)
        bot.send_message(callback.from_user.id, 'i love cats wtf too! :)')
        print(callback.from_user)

    elif callback.data == 'niger':
        response = requests.get('https://cataas.com/cat?filter=negative')
        # print(response.content)
        bot.send_photo(callback.from_user.id, response.content)
        bot.send_message(callback.from_user.id, 'i love NIGER cat too! :)')
        print(callback.from_user)
