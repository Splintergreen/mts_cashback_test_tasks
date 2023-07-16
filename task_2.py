#!/usr/bin/env python

# Задание 2
# Выполнить выборку данных, получив все заказы, у которых
# количество позиций больше трёх и сумма одной позиции больше 1000.

import sqlite3
from tabulate import tabulate


def main(conn):
    cursor = conn.cursor()

    # Выполнение запроса
    cursor.execute('''
        SELECT o.order_id, o.name, o.amount, o.request_date
        FROM cb_order o
        JOIN cb_order_item oi ON o.order_id = oi.order_id
        GROUP BY o.order_id
        HAVING COUNT(oi.id_item) > 3 AND oi.item_amount > 1000
        ORDER BY o.request_date
    ''')

    # Вывод результата
    print(
        'Задача №2.\nВыполнить выборку данных, получив все заказы,'
        'у которых количество позиций больше трёх и сумма '
        'одной позиции больше 1000.'
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
