from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from src.logger._logger import logger_msg
from src.telegram.bussines.refresh.refresh_request import refresh_request
from src.telegram.logic.change_settings import change_settings_
from src.telegram.sendler.sendler import *

from src.telegram.keyboard.keyboards import *
from src.telegram.state.states import States


async def admin_menu(call: types.CallbackQuery):
    await Sendler_msg.log_client_call(call)

    id_user = call.message.chat.id

    keyb = ClientKeyb().admin_menu()

    count_users = BotDB.count_users()

    text_admin = f'🌿 Админ панель\n\n' \
                 f'Кол-во пользователей: {count_users}'

    await Sendler_msg().sendler_photo_call(call, LOGO, text_admin, keyb)

    return True


async def over_state(call: types.CallbackQuery, state: FSMContext):
    await state.finish()

    await Sendler_msg.log_client_call(call)

    return True


async def refresh(call: types.CallbackQuery):
    await Sendler_msg.log_client_call(call)

    res = await refresh_request(call)

    return res


async def view_settings(call: types.CallbackQuery, state: FSMContext):
    await state.finish()

    await Sendler_msg.log_client_call(call)

    await change_settings_(call.message, call.data)

    return True


async def settings(call: types.CallbackQuery, state: FSMContext):
    await state.finish()

    await Sendler_msg.log_client_call(call)

    id_user = call.message.chat.id

    keyb = ClientKeyb().settings()

    text_admin = 'Настройки'

    await Sendler_msg().sendler_photo_call(call, LOGO, text_admin, keyb)

    return True


async def edit_settings(call: types.CallbackQuery, state: FSMContext):
    await Sendler_msg.log_client_call(call)

    try:
        _, target_command = call.data.split('-')
    except Exception as es:
        logger_msg(f'edit_settings: не могу распарсить данные из кнопки "{es}"')

        return False

    _msg = f'⚠️Пришлите следующим сообщением новое значение для настройки "{SETTINGS_LIST[target_command]}"'

    keyb = ClientKeyb().back_target_command(target_command)

    await Sendler_msg.send_msg_call(call, _msg, keyb)

    await States.edit_settings.set()

    async with state.proxy() as data:
        data['target_command'] = target_command

    return True


async def send_db(call: types.CallbackQuery, state: FSMContext):
    await Sendler_msg.log_client_call(call)

    id_user = call.message.chat.id

    keyb = ClientKeyb().back_admin()

    _text_msg = 'База данных:'

    try:
        with open('DB.db', 'rb') as file:
            await call.bot.send_document(id_user, file, caption=_text_msg, reply_markup=keyb)
    except Exception as es:
        logger_msg(f'Ошибка отправки send_db {es}')

        return False

    return True


def register_callbacks(dp: Dispatcher):
    dp.register_callback_query_handler(admin_menu, text_contains='admin_menu')

    dp.register_callback_query_handler(refresh, text_contains='refresh')

    dp.register_callback_query_handler(over_state, text='over_state', state='*')

    dp.register_callback_query_handler(settings, text='settings', state='*')

    for row, _ in SETTINGS_LIST.items():
        dp.register_callback_query_handler(view_settings, text=row, state='*')

    dp.register_callback_query_handler(edit_settings, text_contains='edit-')

    dp.register_callback_query_handler(send_db, text='send_db')
