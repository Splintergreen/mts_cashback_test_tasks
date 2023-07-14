# Задание 2
# Выполнить выборку данных, получив все заказы, у которых количество позиций больше трёх и сумма одной позиции больше 1000.

import sqlite3


# Подключение к БД
conn = sqlite3.connect('database.sqlite')
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
for result in cursor:
    print(result)

# Закрытие подключения
conn.close()
