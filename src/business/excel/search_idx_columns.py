# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from src.logger._logger import logger_msg


async def search_idx_request(report):
    for row in report[:2]:
        try:
            name_idx = row.index('Запросы')
        except:
            continue

        return name_idx

    logger_msg(f'Не смог найти в отчёте колонку "Запросы"')

    return False


async def search_idx_cluster(report):
    for row in report[:2]:
        try:
            name_idx = row.index('Кластер WB')
        except:
            continue

        return name_idx

    logger_msg(f'Не смог найти в отчёте колонку "Кластер WB"')

    return False


async def search_idx_count(report):
    for row in report[:2]:
        try:
            name_idx = row.index('Частота WB')
        except:
            continue

        return name_idx

    logger_msg(f'Не смог найти в отчёте колонку "Частота WB"')

    return False
