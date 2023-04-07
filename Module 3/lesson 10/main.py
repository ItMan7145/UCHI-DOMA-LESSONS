from loader import bot
from utils import set_default_commands
import handlers

if __name__ == "__main__":
    print('Раб начинает работу на хозяина...')
    bot.remove_webhook()
    set_default_commands.cmd_set_default_commands(bot)
    bot.infinity_polling()
