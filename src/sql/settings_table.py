# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from src.logger._logger import logger_msg


def settings_table(cursor):
    try:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS "
                       f"settings (id_pk INTEGER PRIMARY KEY AUTOINCREMENT, "
                       f"key TEXT, "
                       f"value TEX)")

    except Exception as es:
        logger_msg(f'SQL исключение check_table settings {es}')

        return False

    return True
