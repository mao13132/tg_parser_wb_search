from src.logger._logger import logger_msg
from src.telegram.sendler.sendler import Sendler_msg

from aiogram.types import Message


async def division_message(message: Message, response, keyb):
    if len(response) > 4096:
        for x in range(0, len(response), 4096):
            try:
                await message.bot.send_message(message.chat.id, response[x:x + 4096],
                                               reply_markup=keyb)
            except Exception as es:
                logger_msg(f'Произошла ошибка при отправке division_message for: {es}"')

                return False
    else:
        try:
            await message.bot.send_message(message.chat.id, response,
                                           reply_markup=keyb)
        except Exception as es:
            logger_msg(f'Произошла ошибка при отправке division_message: {es}"')

            return False


async def division_message_logo(message: Message, photo, response, keyb):
    if len(response) > 1024:
        for x in range(0, len(response), 1024):
            try:
                with open(photo, 'rb') as file:
                    await message.bot.send_photo(message.chat.id, file, caption=response[x:x + 1024],
                                                 reply_markup=keyb)
            except Exception as es:
                logger_msg(f'Ошибка при отправке division_message_logo с фото for {es}')

                return False
    else:
        try:
            with open(photo, 'rb') as file:
                await message.bot.send_photo(message.chat.id, file, caption=response,
                                             reply_markup=keyb)
        except Exception as es:
            logger_msg(f'Ошибка при отправке division_message_logo с фото {es}')

            return False


async def division_photo_or_text(message: Message, photo, response, keyb):
    if len(response) < 1024:
        await division_message_logo(message, photo, response, keyb)
    else:
        await division_message(message, response, keyb)

    return True
