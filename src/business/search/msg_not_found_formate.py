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


async def msg_not_found_formate(result_dict):
    not_found_text = BotDB.get_settings_by_key('not_found_text')

    count_page = BotDB.get_settings_by_key('count_page')

    try:
        not_found_text = str(not_found_text).replace('%article%', result_dict["article"])

        not_found_text = str(not_found_text).replace('%request%', result_dict["request"])

        not_found_text = str(not_found_text).replace('%count%', str(count_page))

    except Exception as es:
        logger_msg(f'Не могу сформировать сообщение из настроек not_found "{es}"')

        return False

    return not_found_text
