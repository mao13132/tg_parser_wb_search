# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time
from datetime import datetime

import aiohttp

from src.logger._logger import logger_msg


async def _get_position(request_user, search_page=1):
    _page = '' if search_page == 1 else f'page={search_page}&'

    url_get_img = f'https://search.wb.ru/exactmatch/ru/common/v5/search?' \
                  f'ab_testid=sort_rel_limit_50&' \
                  f'{_page}' \
                  f'appType=1&' \
                  f'curr=rub&' \
                  f'&dest=12358553&' \
                  f'query={request_user}&' \
                  f'resultset=catalog&' \
                  f'sort=popular'

    headers_price = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36',
        'Refer': 'https://www.wildberries.ru'
    }

    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=1, connect=.1)) as session:
            async with session.get(url_get_img, timeout=aiohttp.ClientTimeout(total=60),
                                   headers=headers_price) as resul:
                response = await resul.text()

                if resul.status != 200:
                    logger_msg(f'Wb запрос поисковой выдачи: Ответ от сервера не 200 "{response}"')

                return response

    except Exception as es:
        logger_msg(f'Wb запрос поисковой выдачи: Ошибка при при получение выдачи "{es}"')

        return '-1'


async def check_error(data_response):
    try:
        error = data_response['message']
    except:
        return False

    msg = f'Wb запрос поисковой выдачи: Ошибка при получение анализе ответа "{error}"'

    logger_msg(msg)

    return True


async def loop_get_position(request_user, search_page):
    for _try in range(10):
        data_response = await _get_position(request_user, search_page)

        if data_response == '-1':
            time.sleep(30)

            continue

        if not data_response:
            return False

        is_error = await check_error(data_response)

        if is_error == '-1':
            time.sleep(30)

            continue

        if is_error:
            return False

        return data_response

    msg = f'Wb запрос поисковой выдачи: исчерпаны все попытки на при получение ответа поисковой выдачи {request_user}'

    logger_msg(msg)

    return False

# if __name__ == '__main__':
#     import asyncio
#
#     import json
#
#     _request = 'ванночка'
#
#     res = asyncio.run(loop_get_position(_request))
#
#     print()
