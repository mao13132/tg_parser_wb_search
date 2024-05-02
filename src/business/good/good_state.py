# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from datetime import datetime

from src.business.good.formate_msg import formate_msg
from src.business.good.formate_sql_msg import formate_sql_msg

from src.telegram.bot_core import BotDB
from src.telegram.keyboard.keyboards import ClientKeyb


async def good_state(id_user, result_dict):
    date_ = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    id_request = BotDB.add_wb_request(id_user, result_dict["article"], result_dict["request"],
                                      result_dict["page"], result_dict["row"], date_)

    statistic_req = await formate_sql_msg(result_dict['request'])

    msg_ = await formate_msg(result_dict, statistic_req)

    keyb = ClientKeyb().good_search(id_request)

    response_dict = {'msg': msg_, 'keyb': keyb}

    return response_dict
