# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from aiogram.types import Message

from src.telegram.bussines.good.good_state import good_state
from src.telegram.bussines.search.search_core import search_core
from src.telegram.sendler.sendler import Sendler_msg

from src.telegram.bot_core import BotDB


async def search_start_user(message: Message):
    id_user = message.chat.id

    login = message.chat.username

    new_user = BotDB.check_or_add_user(id_user, login)

    await Sendler_msg.log_client_message(message)

    result_dict = await search_core(message)

    keyb = None

    if str(result_dict) == '-1':
        """Юзер ввёл не корректно запрос"""

        msg_ = f'❌ Неверный формат.\n' \
               f'В запросе должен быть сначала артикул, после чего ключевое слово. ' \
               f'Пример: <code>74211840 розовая соль.</code>'

    elif not result_dict:
        """Ошибка при поиске"""

        await Sendler_msg.sendler_to_admin(message, 'Не могу получить ответ от WB - смотрите логи', None)

        return True
    else:

        if not result_dict['page']:
            """Артикул не найден"""

            msg_ = f'🤨 Артикул <a href="https://www.wildberries.ru/catalog/{result_dict["article"]}' \
                   f'/detail.aspx">{result_dict["article"]}</a> по запросу {result_dict["request"]} на первых ' \
                   f'10 страницах не ранжируется.'
        else:
            """Всё ок"""

            good_params = await good_state(id_user, result_dict)

            msg_ = good_params['msg']

            keyb = good_params['keyb']

    res_send = await Sendler_msg.send_msg_message(message, msg_, keyb)

    return res_send
