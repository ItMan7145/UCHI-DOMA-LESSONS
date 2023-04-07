from loader import bot
from data_config import config

@bot.message_handler(commands=['start', 'help'])
def cmd_start(message):
    text = [f'/{commands} - {description}' for commands, description in config.DEFAULT_COMMANDS]
    bot.send_message(message.chat.id, '\n'.join(text))
