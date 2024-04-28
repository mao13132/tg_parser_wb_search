from aiogram.types import Message

from aiogram import Dispatcher

from settings import ADMIN
from src.logger._logger import logger_msg
from src.telegram.bussines.search_start_user import search_start_user
from src.telegram.keyboard.keyboards import ClientKeyb
from src.telegram.sendler.sendler import Sendler_msg

from src.telegram.bot_core import BotDB


async def search_wb(message: Message):
    res = await search_start_user(message)

    return res


async def start(message: Message):
    keyb = None

    id_user = message.chat.id

    login = message.chat.username

    new_user = BotDB.check_or_add_user(id_user, login)

    await Sendler_msg.send_msg_message(message, 'Бот запущен', None)

    me = await message.bot.me

    bot_name = f"{me.username}"

    if str(id_user) in ADMIN:
        keyb = ClientKeyb().admin()

    start_message = BotDB.get_settings_by_key('start_message')

    try:
        start_message = str(start_message).replace('%botname%', bot_name)

    except Exception as es:
        logger_msg(f'Не могу сформировать стартовое сообщение из настроек "{es}"')

        return False

    await Sendler_msg.send_msg_message(message, start_message, keyb)

    return True


def register_user(dp: Dispatcher):
    dp.register_message_handler(start, text='/start')

    dp.register_message_handler(search_wb, text_contains='')
