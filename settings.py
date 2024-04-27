import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), 'src', 'telegram', '.env')

load_dotenv(dotenv_path)

ADMIN = ['']

TOKEN = os.getenv('TOKEN')

START_MESSAGE = 'Стартовое сообщение'
