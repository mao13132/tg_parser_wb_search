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


async def get_data_sql_from_req(user_request):
    try:
        user_request = str(user_request).lower()
    except Exception as es:
        logger_msg(f'Не моогу изменить регистр пользовательского запроса "{es}"')

    data_count_req = BotDB.get_count_req_by_user_req(user_request)

    if not data_count_req:
        return ''

    cluster = data_count_req[2]

    count_req = data_count_req[3]

    refresh_data = data_count_req[4]

    count_req_from_cluster = BotDB.get_count_req_from_cluster(cluster)

    response_dict = {
        'req': user_request,
        'cluster': cluster,
        'count_req': count_req,
        'count_cluster': count_req_from_cluster,
        'date': refresh_data
    }

    return response_dict
