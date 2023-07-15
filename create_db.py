#!/usr/bin/env python

import sqlite3
from random import randint, random, uniform
from datetime import datetime, timedelta

# Создание базы данных и подключение к ней
conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()

# Создание таблицы cb_order
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cb_order (
        order_id INTEGER PRIMARY KEY,
        name TEXT,
        amount REAL,
        request_date TEXT
    )
''')

# Создание таблицы cb_order_item
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cb_order_item (
        id_item INTEGER PRIMARY KEY,
        order_id INTEGER,
        item_name TEXT,
        item_quantity INTEGER,
        item_amount REAL,
        FOREIGN KEY (order_id) REFERENCES cb_order (order_id)
    )
''')


# Заполнение таблицы cb_order тестовыми данными
def random_date():
    '''Генирирует случайную дату
    в промежутке текущее время - год назад '''
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)

    return str(start_date + (end_date - start_date) * random())


# Таблица cb_order c полями order_id, name, amount, request_date;
order_data = [(i, f'Order {i}', round(uniform(1, 200), 2), random_date()) for i in range(1, 101)]

cursor.executemany('INSERT INTO cb_order VALUES (?, ?, ?, ?)', order_data)

# Заполнение таблицы cb_order_item тестовыми данными
# Таблица cb_order_item с полями id_item, order_id, item_name, item_quantity, item_amount.
order_item_data = [(i, randint(1, 101), f'Item {i}', randint(1, 10), round(uniform(1, 1500), 2)) for i in range(1, 1001)]

cursor.executemany('INSERT INTO cb_order_item VALUES (?, ?, ?, ?, ?)', order_item_data)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print('База данных успешно создана и наполнена тестовыми записями.')
