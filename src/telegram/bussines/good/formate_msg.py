# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from src.logger._logger import logger_msg

from src.telegram.bot_core import BotDB


async def formate_msg(result_dict):
    good_text = BotDB.get_settings_by_key('good_text')

    text_link = BotDB.get_settings_by_key('text_link')

    try:
        good_text = str(good_text).replace('%article%', str(result_dict["article"]))

        good_text = str(good_text).replace('%request%', str(result_dict["request"]))

        good_text = str(good_text).replace('%page%', str(result_dict["page"]))

        good_text = str(good_text).replace('%row%', str(result_dict["row"]))

    except Exception as es:
        logger_msg(f'Не могу сформировать good сообщение из настроек "{es}"')

        return False

    try:
        good_text = f'{good_text}{text_link}'

    except Exception as es:
        logger_msg(f'Ошибка при формирования положительного ответа (склейка) "{es}"')

        return False

    return good_text
