# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from src.business.excel.search_idx_columns import search_idx_request, search_idx_cluster, search_idx_count

from src.telegram.bot_core import BotDB


async def load_from_sql_data(data_excel):
    idx_request_column = await search_idx_request(data_excel)

    if str(idx_request_column) == 'False':
        return False

    idx_cluster_column = await search_idx_cluster(data_excel)

    if str(idx_cluster_column) == 'False':
        return False

    idx_count_request = await search_idx_count(data_excel)

    if str(idx_count_request) == 'False':
        return False

    add_count = 0

    update_count = 0

    for row in data_excel[1:-1]:

        res = BotDB.add_request(row[idx_request_column], row[idx_cluster_column], row[idx_count_request])

        if not res:
            continue

        if res == 'add':
            add_count += 1

        if res == 'update':
            update_count += 1

    add_count = f'\nДобавлено: {add_count}' if add_count else ''

    update_count = f'\nОбновлено: {update_count}' if update_count else ''

    return f'{add_count}{update_count}'
