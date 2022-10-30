import json

from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest
from decouple import Csv, config

api_id = config('TLG_API_ID')
api_hash = config('TLG_API_HASH')
username = config('TLG_USERNAME')

client = TelegramClient(username, api_id, api_hash)

client.start()

msgs = []

all_messages = []   # список всех сообщений


async def dump_all_messages(channel):
    """Записывает json-файл с информацией о всех сообщениях канала/чата"""
    offset_msg = 0    # номер записи, с которой начинается считывание
    limit_msg = 3   # максимальное число записей, передаваемых за один раз

    total_messages = 0
    total_count_limit = 5  # поменяйте это значение, если вам нужны не все сообщения

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
        offset_msg = messages[len(messages) - 1].id
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break


async def main():
    url = config('TLG_CHANNEL_URL')
    channel = await client.get_entity(url)
    await dump_all_messages(channel)


with client:
    res = client.loop.run_until_complete(main())

for msg in all_messages:
    print(msg['date'])
    text = msg['message'].replace('\n',' ')[:100]
    print(f"{text}...")
    print(f"https://t.me/activebike/{msg['id']}")
    # print("")


