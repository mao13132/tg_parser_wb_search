# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from src.logger._logger import logger_msg


async def formate_msg(result_dict):
    try:
        msg_ = f'👍 Артикул <a href="https://www.wildberries.ru/catalog/{result_dict["article"]}' \
               f'/detail.aspx">{result_dict["article"]}</a> ' \
               f'по запросу {result_dict["request"]} найден:\n' \
               f'Страница: {result_dict["page"]}\n' \
               f'Позиция: {result_dict["row"]}'
    except Exception as es:
        logger_msg(f'Ошибка при формирования положительного ответа "{es}"')

        return False

    return msg_
