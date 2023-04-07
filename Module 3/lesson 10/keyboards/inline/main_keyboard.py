from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def kb_choice_cat():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('happy', callback_data='happy'),
                 InlineKeyboardButton('WTF', callback_data='wtf'),
                 InlineKeyboardButton('NIGER', callback_data='niger'))

    return keyboard
