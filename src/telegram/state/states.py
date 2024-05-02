import asyncio
import os

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from settings import SETTINGS_LIST, LOGO, report_path
from src.business.excel.excel_core import JobExcel
from src.business.excel.load_from_sql_data import load_from_sql_data
from src.logger._logger import logger_msg
from src.telegram.keyboard.keyboards import ClientKeyb
from src.telegram.sendler.sendler import Sendler_msg
from src.telegram.bot_core import BotDB


class States(StatesGroup):
    edit_settings = State()

    add_report = State()


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


async def add_report(message: Message, state: FSMContext):
    await Sendler_msg.log_client_message(message)

    type_msg = message.content_type

    if type_msg != 'document':
        _msg = f'⚠️Вы прислали не верный файл! Необходимо прислать файл excel! ' \
               f'Попробуйте ещё раз или нажмите кнопку "назад"'

        keyb = ClientKeyb().back_admin()

        await Sendler_msg().new_sendler_photo_message(message, LOGO, _msg, keyb)

        return False

    await state.finish()

    keyb = ClientKeyb().admin_menu()

    _msg = f'Начинаю загружать файл. Ожидайте'

    await Sendler_msg().new_sendler_photo_message(message, LOGO, _msg, keyb)

    id_file = message.document.file_id

    file_name = message.document.file_name

    download_path = f'{report_path}{os.sep}{file_name}'

    try:
        file_path = await message.bot.get_file(id_file)

        res_down = await message.bot.download_file(file_path.file_path, download_path)

    except Exception as es:

        logger_msg(f'Не могу загрузить отчёт "{es}"')

        _msg = f'Не могу загрузить отчёт - смотрите логи'

        keyb = ClientKeyb().admin_menu()

        await Sendler_msg().new_sendler_photo_message(message, LOGO, _msg, keyb)

        return False

    create_job = asyncio.create_task(JobExcel.load_excel_file(download_path))

    data_excel = await create_job

    if not data_excel:
        _msg = f'Не могу открыть отчёт - смотрите логи'

        keyb = ClientKeyb().admin_menu()

        await Sendler_msg().new_sendler_photo_message(message, LOGO, _msg, keyb)

        return False

    try:
        os.remove(download_path)
    except Exception as es:
        logger_msg(f'Не могу удалить загружен файл "{es}"')

    sql_create_job = asyncio.create_task(load_from_sql_data(data_excel))

    good_data_report = await sql_create_job

    if not good_data_report:
        _msg = f'Не могу найти нужные колонки в отчёте - смотрите логи'

        keyb = ClientKeyb().admin_menu()

        await Sendler_msg().new_sendler_photo_message(message, LOGO, _msg, keyb)

        return False

    _msg = f'✅Отчёт успешно загружен\n{good_data_report}'

    await message.reply(_msg)

    return True


def register_state(dp: Dispatcher):
    dp.register_message_handler(edit_settings, state=States.edit_settings)

    dp.register_message_handler(add_report, state=States.add_report, content_types=[types.ContentType.ANY])
