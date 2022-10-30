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


async def dump_all_participants(channel):
    """Записывает json-файл с информацией о всех участниках канала/чата"""
    offset_user = 0    # номер участника, с которого начинается считывание
    limit_user = 100   # максимальное число записей, передаваемых за один раз

    all_participants = []   # список всех участников канала
    filter_user = ChannelParticipantsSearch('')

    while True:
        participants = await client(GetParticipantsRequest(channel,
            filter_user, offset_user, limit_user, hash=0))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset_user += len(participants.users)

    all_users_details = []   # список словарей с интересующими параметрами участников канала

    for participant in all_participants:
        all_users_details.append({"id": participant.id,
            "first_name": participant.first_name,
            "last_name": participant.last_name,
            "user": participant.username,
            "phone": participant.phone,
            "is_bot": participant.bot})

    with open('channel_users.json', 'w', encoding='utf8') as outfile:
        json.dump(all_users_details, outfile, ensure_ascii=False)

all_messages = []   # список всех сообщений

async def dump_all_messages(channel):
    """Записывает json-файл с информацией о всех сообщениях канала/чата"""
    offset_msg = 0    # номер записи, с которой начинается считывание
    limit_msg = 5   # максимальное число записей, передаваемых за один раз

    total_messages = 0
    total_count_limit = 5  # поменяйте это значение, если вам нужны не все сообщения

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
            print(f"https://t.me/activebike/{message.id}")
            all_messages.append(message.to_dict())
        offset_msg = messages[len(messages) - 1].id
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break


async def main():
    url = config('TLG_CHANNEL_URL')
    channel = await client.get_entity(url)
    # await dump_all_participants(channel)
    await dump_all_messages(channel)


with client:
    client.loop.run_until_complete(main())


for item in all_messages:
    print(f"id: {item['id']}, message: {item['message']};")