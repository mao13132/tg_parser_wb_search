# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from datetime import datetime

from aiogram import types

from src.business.good.formate_sql_msg import formate_sql_msg
from src.logger._logger import logger_msg
from src.business.search_article.search_article import search_article

from src.telegram.bot_core import BotDB
from src.business.good.formate_msg import formate_msg
from src.telegram.keyboard.keyboards import ClientKeyb


async def refresh_request(call: types.CallbackQuery):
    id_user = call.message.chat.id

    me = await call.bot.me

    bot_name = f"{me.username}"

    load_keyb = ClientKeyb().load(bot_name)

    try:
        await call.message.edit_reply_markup(reply_markup=load_keyb)
    except Exception as es:
        logger_msg(f'Не могу обновить сообщение пользователя "{id_user}" "{es}"')

        return False

    try:
        _, id_pk_request = str(call.data).split('-')
    except Exception as es:
        logger_msg(f'Ошибка при разборе refresh- {es}')

        return False

    data_sql_by_user = BotDB.get_data_by_user(id_pk_request)

    if not data_sql_by_user:
        logger_msg(f'Нет {id_pk_request} запроса в SQL базе')

        return False

    article = data_sql_by_user[2]

    search_request = data_sql_by_user[3]

    response_wb = await search_article(search_request, article)

    statistic_req = await formate_sql_msg(response_wb['request'])

    msg_ = await formate_msg(response_wb, statistic_req)

    date_ = datetime.now().strftime('%Y-%m-%d %H:%M:%S').split()

    date_ = f"{date_[0]} в {date_[1]}"

    msg_ = f"{msg_}\n<b>Обновлено:</b> {date_}"

    keyb = ClientKeyb().good_search(id_pk_request)

    try:
        await call.message.edit_text(text=msg_, reply_markup=keyb, disable_web_page_preview=True)
    except Exception as es:
        logger_msg(f'Не могу обновить сообщение пользователя "{id_user}" "{es}"')

        return False

    return True
