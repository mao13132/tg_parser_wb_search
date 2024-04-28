from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from settings import SETTINGS_LIST, LOGO
from src.telegram.keyboard.keyboards import ClientKeyb
from src.telegram.sendler.sendler import Sendler_msg
from src.telegram.bot_core import BotDB


class States(StatesGroup):
    edit_settings = State()


async def edit_settings(message: Message, state: FSMContext):
    await Sendler_msg.log_client_message(message)

    new_settings_value = message.text

    target_command = ''

    async with state.proxy() as data:
        target_command = data['target_command']

    res_change_sql = BotDB.edit_settings(target_command, new_settings_value)

    status_change = f'✅Успешно изменил' if res_change_sql else '❌Не смог изменить'

    _msg = f'{status_change} "{SETTINGS_LIST[target_command]}"\n\n<b>изменил на</b>\n\n{new_settings_value}'

    keyb = ClientKeyb().settings()

    await Sendler_msg().new_sendler_photo_message(message, LOGO, _msg, keyb)

    await state.finish()


def register_state(dp: Dispatcher):
    dp.register_message_handler(edit_settings, state=States.edit_settings)
