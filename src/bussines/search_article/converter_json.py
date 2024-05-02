# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import json

from src.logger._logger import logger_msg


async def converter_json(data):
    try:
        convert_data = json.loads(data)
    except Exception as es:
        logger_msg(f'Ошибка при конвертации ответа из json "{es}"')

        return False

    return convert_data
