import os

from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Hi from INDUS :). Code error: "INDUS"')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('TOKEN')

DEFAULT_COMMANDS = (('start', 'заставить работать'),
                    ('help', 'хэлпа'),
                    ('cat', 'поиск котёнка'))
