# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from aiogram.types import Message

from src.logger._logger import logger_msg


async def parsing_user_msg(message: Message):
    try:
        split_msg = message.text.split()

        if len(split_msg) <= 1:
            return '-1'

        article = split_msg[0]

        if not article.isdigit():
            return '-1'

        search_request = ' '.join(split_msg[1:])

    except Exception as es:
        logger_msg(f'Ошибка распознавания сообщения от пользователя "{es}"')

        return '-1'

    response_dict = {'article': article, 'search_request': search_request}

    return response_dict
