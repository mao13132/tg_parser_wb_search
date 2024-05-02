# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from aiogram.types import Message

from settings import LOGO
from src.telegram.bot_core import BotDB
from src.telegram.keyboard.keyboards import ClientKeyb
from src.telegram.logic.devision_msg import division_photo_or_text
from src.telegram.sendler.sendler import Sendler_msg


async def change_settings_(message: Message, target):

    user_id = message.chat.id

    name_settings_text = BotDB.get_settings_by_key(target)

    keyb = ClientKeyb().edit_settings(target)

    await division_photo_or_text(message, LOGO, f'{name_settings_text}', keyb)

    return True
