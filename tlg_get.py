from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import GetHistoryRequest
from decouple import config
from datetime import date, datetime
import json

API_ID = config('TLG_API_ID')
API_HASH = config('TLG_API_HASH')
USERNAME = config('TLG_USERNAME')
SESSION_STRING = config('TLG_SESSION_STRING')
TLG_CHANNEL_URL = config('TLG_CHANNEL_URL')

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

all_messages = []   # список всех сообщений


async def dump_all_messages(channel):
    """Записывает json-файл с информацией о всех сообщениях канала/чата"""
    offset_msg = 0    # номер записи, с которой начинается считывание
    limit_msg = 3   # максимальное число записей, передаваемых за один раз

    total_messages = 0
    total_count_limit = 3  # поменяйте это значение, если вам нужны не все сообщения

    class DateTimeEncoder(json.JSONEncoder):
        '''Класс для сериализации записи дат в JSON'''
        def default(self, o):
            if isinstance(o, datetime):
                return o.isoformat()
            if isinstance(o, bytes):
                return list(o)
            return json.JSONEncoder.default(self, o)

    while True:
        history = await client(GetHistoryRequest(
            peer=channel,
            offset_id=offset_msg,
            offset_date=None, add_offset=0,
            limit=limit_msg, max_id=0, min_id=0,
            hash=0))
        if not history.messages:
            break
        messages = history.messages
        for message in messages:
            all_messages.append(message.to_dict())
            if message.message == "":
                total_count_limit += 1
        offset_msg = messages[len(messages) - 1].id
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break

    with open('channel_messages.json', 'w', encoding='utf8') as outfile:
        json.dump(all_messages, outfile, ensure_ascii=False, cls=DateTimeEncoder)


async def main():
    url = TLG_CHANNEL_URL
    channel = await client.get_entity(url)
    await dump_all_messages(channel)


with client:
    res = client.loop.run_until_complete(main())

