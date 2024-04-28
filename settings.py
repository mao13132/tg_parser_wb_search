import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), 'src', 'telegram', '.env')

load_dotenv(dotenv_path)

LOGO = r'src/telegram/media/logo.png'

# ADMIN = ['1422194909', '1514001292']
ADMIN = ['1422194909']

TOKEN = os.getenv('TOKEN')

START_MESSAGE = 'Стартовое сообщение'

SETTINGS_LIST = {
    'count_page': '🔍 Сколько обрабатывать страниц',
    'text_link': '🖊 Надпись к сообщению с результатами',
    'start_message': '👋 Приветственное сообщение',
    'good_text': '✅ Сообщение об успехе',
    'bad_text': '❌ Сообщение с ошибкой',
    'not_found_text': '🙅‍♂️ Сообщение не найдено',
}
