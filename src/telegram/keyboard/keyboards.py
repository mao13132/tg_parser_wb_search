from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import SETTINGS_LIST


class ClientKeyb:
    def good_search(self, id_pk_request):
        self._start_key = InlineKeyboardMarkup(row_width=1)

        self._start_key.add(InlineKeyboardButton(text=f'🔄 Обновить', callback_data=f'refresh-{id_pk_request}'))

        return self._start_key

    def load(self, bot_name):
        self._start_key = InlineKeyboardMarkup(row_width=1)

        self._start_key.add(InlineKeyboardButton(text=f'Обновляется...', url=f'https://t.me/{bot_name}'))

        return self._start_key

    def admin(self):
        self._start_key = InlineKeyboardMarkup(row_width=1)

        self._start_key.add(InlineKeyboardButton(text=f'🎩 Админка', callback_data='admin_menu'))

        return self._start_key

    def admin_menu(self):
        self._start_key = InlineKeyboardMarkup(row_width=1)

        self._start_key.add(InlineKeyboardButton(text='⚙️ Настройки', callback_data='settings'))

        return self._start_key

    def edit_settings(self, target):
        self._start_key = InlineKeyboardMarkup(row_width=1)

        self._start_key.add(InlineKeyboardButton(text=f'✏️ Редактировать', callback_data=f'edit-{target}'))

        self._start_key.add(InlineKeyboardButton(text=f'🔙 Назад', callback_data='settings'))

        return self._start_key

    def settings(self):
        self._start_key = InlineKeyboardMarkup(row_width=1)

        for key, text in SETTINGS_LIST.items():
            self._start_key.add(InlineKeyboardButton(text=text, callback_data=key))

        self._start_key.add(InlineKeyboardButton(text=f'🔙 Назад', callback_data='admin_menu'))

        return self._start_key

    def back_target_command(self, target):
        self._start_key = InlineKeyboardMarkup(row_width=1)

        self._start_key.add(InlineKeyboardButton(text=f'🔙 Назад', callback_data=target))

        return self._start_key
