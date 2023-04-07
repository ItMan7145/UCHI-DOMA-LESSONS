from data_config import config
from telebot.types import BotCommand


def cmd_set_default_commands(bot):
    bot.set_my_commands([BotCommand(*l) for l in config.DEFAULT_COMMANDS])
