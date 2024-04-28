import datetime
import sqlite3
from datetime import datetime

from src.logger._logger import logger_msg


class BotDB:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, db_file):
        try:

            self.conn = sqlite3.connect(db_file, timeout=30)

            print('Подключился к SQL DB:', db_file)

            self.cursor = self.conn.cursor()

            self.check_table()

        except Exception as es:
            print(f'Ошибка при работе с SQL {es}')

    def check_table(self):

        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS "
                                f"users (id_pk INTEGER PRIMARY KEY AUTOINCREMENT, "
                                f"id_user TEXT, "
                                f"login TEXT, "
                                f"status TEXT DEFAULT new, "
                                f"push1 BOOLEAN DEFAULT 1, "
                                f"push_time DATETIME DEFAULT 0, "
                                f"join_date DATETIME, "
                                f"last_time DATETIME DEFAULT 0, "
                                f"license BOOLEAN DEFAULT 0, "
                                f"date_buy DATETIME DEFAULT 0, "
                                f"other TEXT)")

        except Exception as es:
            print(f'SQL исключение check_table users {es}')

        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS "
                                f"wb_requests (id_pk INTEGER PRIMARY KEY AUTOINCREMENT, "
                                f"id_user TEXT, "
                                f"article TEXT, "
                                f"wb_request TEXT, "
                                f"page NUMERIC, "
                                f"position NUMERIC, "
                                f"check_time DATETIME DEFAULT 0, "
                                f"other TEXT)")

        except Exception as es:
            print(f'SQL исключение check_table wb_requests {es}')

    def check_or_add_user(self, id_user, login):
        try:

            result = self.cursor.execute(f"SELECT * FROM users WHERE id_user='{id_user}'")

            response = result.fetchall()

            if not response:
                now_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                self.cursor.execute("INSERT OR IGNORE INTO users ('id_user', 'login',"
                                    "'join_date') VALUES (?,?,?)",
                                    (id_user, login,
                                     now_date,))

                self.conn.commit()

                return True

            return False
        except Exception as es:
            logger_msg(f'SQL ошибка check_or_add_user "{es}"')

            return False

    def edit_user(self, key, value, id_user):

        try:

            result = self.cursor.execute(f"SELECT {key} FROM users "
                                         f"WHERE id_user = '{id_user}'")

            response = result.fetchall()

            if not response:
                logger_msg(f'SQL Не могу отредактировать пользователя "{id_user}" поле: "{key}" значение: "{value}"')
                return False

            self.cursor.execute(f"UPDATE users SET {key} = '{value}' WHERE id_user = '{id_user}'")

            self.conn.commit()

            print(f'SQL: Отредактировал пользователя "{id_user}" поле: "{key}" значение: "{value}"')

            return True

        except Exception as es:
            logger_msg(f'SQL ERROR: Не смог изменить пользователя"{id_user}" поле: "{key}" значение: "{value}" "{es}"')

            return False

    def add_wb_request(self, id_user, article, wb_request, page, position, date):

        try:

            self.cursor.execute("INSERT OR IGNORE INTO wb_requests ('id_user', 'wb_request', 'page',"
                                "'position', 'check_time', 'article') VALUES (?,?,?,?,?,?)",
                                (id_user, wb_request, page,
                                 position, date, article))

            self.conn.commit()

        except Exception as es:
            logger_msg(f'SQL ошибка add_wb_request "{es}"')

            return False

        return self.cursor.lastrowid

    def get_data_by_user(self, id_pk_request):
        try:

            result = self.cursor.execute(f"SELECT * FROM wb_requests "
                                         f"WHERE id_pk = '{id_pk_request}'")

            response = result.fetchall()

            response = response[0]


        except Exception as es:
            logger_msg(f'SQL Ошибка SQL get_data_by_user: {es}')

            return False

        return response

    def close(self):

        self.conn.close()

        logger_msg('Отключился от SQL BD')
