#!/usr/bin/env python

# Задание 1
# Получить список заказов, сделанных за последние семь дней.

import sqlite3
from tabulate import tabulate


def main(conn):
    cursor = conn.cursor()

    # Выполнение запроса
    cursor.execute('''
        SELECT *
        FROM cb_order
        WHERE request_date >= date('now', '-7 day')
        ORDER BY request_date
    ''')

    # Вывод результата
    print(
        'Задача №1.\n'
        'Получить список заказов, сделанных за последние семь дней.'
    )
    print(tabulate(
        [i for i in cursor],
        headers=['order_id', 'name', 'amount', 'request_date'],
        tablefmt='fancy_grid'
    ))

    conn.close()  # Закрытие подключения


if __name__ == '__main__':
    # Подключение к БД
    try:
        conn = sqlite3.connect('file:database.sqlite?mode=ro', uri=True)
        main(conn)
    except sqlite3.OperationalError:
        print(
            'Отсутствует файл БД!\n'
            'Убедитесь что скрипт находится в одной папке с БД.'
        )
