# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from aiogram.types import Message

from src.business.search_article.search_article import search_article
from src.business.search.parsing_user_msg import parsing_user_msg
from src.telegram.sendler.sendler import Sendler_msg


async def search_core(message: Message):
    result_dict = await parsing_user_msg(message)

    if str(result_dict) == '-1':
        return '-1'

    start_msg = '🔎 Поиск запущен.. Ранжирование артикула проверяется в полной версии сайта для компьютеров.'

    await Sendler_msg.send_msg_message(message, start_msg, None)

    response_wb = await search_article(result_dict['search_request'], result_dict['article'])

    return response_wb
