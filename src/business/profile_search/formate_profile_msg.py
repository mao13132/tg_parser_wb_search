# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from datetime import datetime

from src.telegram.bot_core import BotDB


async def formate_profile_msg(user_row):
    id_user = user_row[1]

    login = user_row[2]

    _msg = f'ID: {id_user} Логин: {login}\n\n'

    requests_list_from_user = BotDB.get_req_from_user(id_user)

    if not requests_list_from_user:
        return f"{_msg}Запросов нет"

    sorted_list = sorted(requests_list_from_user, key=lambda tup: datetime.strptime(tup[6], '%Y-%m-%d %H:%M:%S'),
                         reverse=True)

    old_requests = []

    for count, sql_row in enumerate(sorted_list):
        article = sql_row[2]

        req_name = sql_row[3]

        try:
            req_name = req_name.lower()
        except:
            pass

        if req_name in old_requests:
            continue

        old_requests.append(req_name)

        page = sql_row[4]

        position = sql_row[5]

        date_req = sql_row[6]

        data_count_req = BotDB.get_count_req_by_user_req(req_name)

        cluster_text = 'Кластер не обнаружен\n\n'

        if data_count_req:
            cluster = data_count_req[2]

            count_req = data_count_req[3]

            refresh_data = data_count_req[4]

            count_req_from_cluster = BotDB.get_count_req_from_cluster(cluster)

            req_cluster = BotDB.req_from_cluster(cluster)

            req_cluster = sorted(req_cluster, key=lambda tup: tup[3],
                                 reverse=True)

            req_from_cluster = '\n'.join(f"Запрос: <code>{row[1]}</code> Частотность: {row[3]}" for row in req_cluster)

            cluster_text = f'Кластер: <code>{cluster}</code> Частотность: {count_req}\n' \
                           f'Запросы из кластера:\n---\n' \
                           f'{req_from_cluster}\n\n'

        _msg += f'{count + 1}. Артикул: <code>{article}</code> Запрос: <code>{req_name}</code>\n' \
                f'Дата запроса: {date_req}\n' \
                f'Страница: {page} Позиция: {position}\n{cluster_text}'

    return _msg
