from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class ClientKeyb:
    def good_search(self, id_pk_request):
        self._start_key = InlineKeyboardMarkup(row_width=1)

        self._start_key.add(InlineKeyboardButton(text=f'🔄 Обновить', callback_data=f'refresh-{id_pk_request}'))

        return self._start_key

    def load(self, bot_name):
        self._start_key = InlineKeyboardMarkup(row_width=1)

        self._start_key.add(InlineKeyboardButton(text=f'Обновляется...', url=f'https://t.me/{bot_name}'))

        return self._start_key
