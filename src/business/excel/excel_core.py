# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from datetime import datetime

import openpyxl

from src.logger._logger import logger_msg


class JobExcel:
    @staticmethod
    async def _load_excel_file(file_patch):

        try:

            load_file = openpyxl.load_workbook(file_patch)

        except Exception as es:

            msg = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} ' \
                  f'WB _load_excel_file: ошибка при загрузке Excel файла "{es}"'

            logger_msg(msg)

            return False

        load_file = load_file.active

        return load_file

    @staticmethod
    async def _format_excel_from_list(load_file):
        good_row_list = []

        for row in load_file.iter_rows(min_col=0, max_col=19, min_row=1, max_row=10000, values_only=True):
            if row[0] is None:
                continue
            good_row_list.append(row)

        return good_row_list

    @staticmethod
    async def format_excel_from_list(load_file):
        try:
            good_row_list = await JobExcel._format_excel_from_list(load_file)

        except Exception as es:

            msg = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} ' \
                  f'WB _load_excel_file: ошибка при форматирование Excel файла в список "{es}"'

            logger_msg(msg)

            return False

        return good_row_list

    @staticmethod
    async def load_excel_file(file_patch):
        print(f'\nначинаю загружать данные из excel файла\n')

        load_file = await JobExcel._load_excel_file(file_patch)

        if not load_file:
            return False

        format_excel_from_dict = await JobExcel.format_excel_from_list(load_file)

        return format_excel_from_dict
