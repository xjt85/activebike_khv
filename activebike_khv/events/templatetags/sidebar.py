from django import template

from ..models import Article

import json

from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

from telethon.sessions import StringSession

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest
from decouple import Csv, config

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


async def main():
    url = TLG_CHANNEL_URL
    channel = await client.get_entity(url)
    await dump_all_messages(channel)


with client:
    res = client.loop.run_until_complete(main())


register = template.Library()


@register.inclusion_tag("includes/right_sidebar.html")
def show_sidebar():
    articles = Article.objects.all()
    # for msg in all_messages:
    #     msg['message'] = msg['message'].replace('\n',' ')[:100] + '...'
    return {
        'popular_articles': articles,
        'all_messages': all_messages
        }
