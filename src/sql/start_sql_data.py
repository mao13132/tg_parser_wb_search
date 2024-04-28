# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------


def start_sql_data(BotDB):
    BotDB.start_settings('count_page', '10')

    BotDB.start_settings('text_link', '🔥ТОП запросов в кластере с этим ключевым запросом')

    BotDB.start_settings('link', 'https://t.me/Positive83')

    BotDB.start_settings('bad_text', f'❌ Неверный формат.\n'
                                     f'В запросе должен быть сначала артикул, после чего ключевое слово. '
                                     f'Пример: <code>74211840 розовая соль</code>')

    BotDB.start_settings('not_found_text', f'🤨 Артикул <a href="https://www.wildberries.ru/'
                                           f'catalog/%article%'
                                           f'/detail.aspx">%article%</a> '
                                           f'по запросу %request% на первых '
                                           f'%count% страницах не ранжируется.')

    BotDB.start_settings('good_text', f'👍 Артикул <a href="https://www.wildberries.ru/catalog/%article%'
                                      f'/detail.aspx">%article%</a> '
                                      f'по запросу %request% найден:\n'
                                      f'Страница: %page%\n'
                                      f'Позиция: %row%\n\n')

    BotDB.start_settings('start_message', f'Вас приветствует %botname%. 👋\n'
                                          f'Инструкция: вбейте артикул WB и через пробел ключевой запрос. '
                                          f'Пример: <code>74211840 розовая соль</code>')
