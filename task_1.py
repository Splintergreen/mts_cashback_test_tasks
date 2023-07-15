#!/usr/bin/env python

# Задание 1
# Получить список заказов, сделанных за последние семь дней.

import sqlite3
import sys


# Подключение к БД
conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()

# Выполнение запроса
cursor.execute('''
    SELECT *
    FROM cb_order
    WHERE request_date >= date('now', '-7 day')
    ORDER BY request_date
''')

# Вывод результата
for result in cursor:
    # sys.stdout(result)
    print(result)

# Закрытие подключения
conn.close()
