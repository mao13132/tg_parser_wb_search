from aiogram.types import Message

from aiogram import Dispatcher

from src.telegram.bussines.search_start_user import search_start_user
from src.telegram.sendler.sendler import Sendler_msg

from src.telegram.bot_core import BotDB


async def search_wb(message: Message):
    res = await search_start_user(message)

    return res


async def start(message: Message):
    id_user = message.chat.id

    login = message.chat.username

    new_user = BotDB.check_or_add_user(id_user, login)

    await Sendler_msg.send_msg_message(message, 'Бот запущен', None)

    me = await message.bot.me

    bot_name = f"{me.username}"

    await Sendler_msg.send_msg_message(message, f'Вас приветствует {bot_name}. '
                                                f'Инструкция: вбейте артикул WB и через пробел ключевой запрос', None)

    return True


def register_user(dp: Dispatcher):
    dp.register_message_handler(start, text='/start')

    dp.register_message_handler(search_wb, text_contains='')
