from aiogram import Dispatcher, types

from src.logger._logger import logger_msg
from src.telegram.bussines.refresh.refresh_request import refresh_request
from src.telegram.sendler.sendler import *

from src.telegram.keyboard.keyboards import *


async def adminka(call: types.CallbackQuery):
    await Sendler_msg.log_client_call(call)


async def refresh(call: types.CallbackQuery):
    await Sendler_msg.log_client_call(call)

    res = await refresh_request(call)

    return res


def register_callbacks(dp: Dispatcher):
    dp.register_callback_query_handler(adminka, text_contains='adminka')

    dp.register_callback_query_handler(refresh, text_contains='refresh')
