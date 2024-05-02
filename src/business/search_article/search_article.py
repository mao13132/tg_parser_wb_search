# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import asyncio

from src.logger._logger import logger_msg
from src.business.search_article.converter_json import converter_json
from src.business.wb.wb_search import loop_get_position


async def _search_article_from_response(response_wb, article):
    try:
        for count, product in enumerate(response_wb['data']['products']):
            if str(product['id']) == str(article):
                return count + 1

    except Exception as es:
        logger_msg(f'_search_article_from_response Нет продуктов в ответе "{es}"')

        return '-1'

    return False


async def search_article(user_request, article):
    for page in range(10):
        """Итерация страниц"""

        status_error = False

        for zero_product in range(2):
            """Цикл если товаров нет"""

            search_page = page + 1

            response_wb = await loop_get_position(user_request, search_page)

            if not response_wb:
                return False

            response_wb = await converter_json(response_wb)

            if not response_wb:
                return False

            if len(response_wb['data']['products']) < 10 and search_page < 3:

                print(f"В ответе WB всего '{len(response_wb['data']['products'])}' товар(ов)")

                status_error = True

                await asyncio.sleep(5)

                continue
            else:
                status_error = False

                break

        if status_error:
            continue

        position = await _search_article_from_response(response_wb, article)

        if position == '-1':
            return False

        if str(position) == 'False':
            print(f'Нет на {search_page} странице артикула "{article}" по запросу "{user_request}"')

            continue

        return {'page': search_page, 'row': position,
                'request': user_request, 'article': article}

    return {'page': 0, 'row': 0, 'request': user_request, 'article': article}
