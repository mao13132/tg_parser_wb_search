# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from src.business.good.get_data_sql_from_req import get_data_sql_from_req


async def formate_sql_msg(user_request):
    data_from_sql = await get_data_sql_from_req(user_request)

    if not data_from_sql:
        return ''

    _msg = f'Частотность запроса за 30 дней на WB: {data_from_sql["count_req"]}\n' \
           f'Количество запросов в кластере: {data_from_sql["count_cluster"]}'

    return _msg
