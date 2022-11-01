from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from decouple import Csv, config

API_ID = config('TLG_API_ID')
API_HASH = config('TLG_API_HASH')

# Авторизация и печать ключа сессии
with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print(client.session.save())
