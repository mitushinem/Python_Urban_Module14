import sqlite3
from random import randint
from crud_functions import get_all_products


# initiate_db()
#
# with sqlite3.connect('database.db') as conn:
#     c = conn.cursor()
#
#     for i in range(1, 5):
#         c.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                   (f'Товар {i}', f'Описание товара {i}', randint(10, 100)))
#
#         conn.commit()


for i in get_all_products():
    print(i)