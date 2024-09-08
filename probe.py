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

#
# for i in get_all_products():
#     print(i)





import sqlite3
from random import randint

# conn = sqlite3.connect('test.db')
# cur = conn.cursor()
#
# cur.execute('''
# CREATE TABLE IF NOT EXISTS Users(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# username TEXT NOT NULL,
# email TEXT NOT NULL,
# age INTEGER
# )
# ''')

#cur.execute('''CREATE INDEX IF NOT EXISTS idx_email ON Users (email)''')

# for i in range(30):
#     cur.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", (f"newuser{i}", f"ex{1}@gmail.com", randint(20, 60)))

#cur.execute("UPDATE Users SET age = ? WHERE username = ?", (29, 'newuser'))

# for i in range(30):
#     cur.execute("DELETE FROM Users WHERE username = ?", (f'newuser{i}',))

#cur.execute("SELECT * FROM Users")
#cur.execute("SELECT username, age FROM Users WHERE age > ?", (29,))
#
# cur.execute("SELECT age, AVG(age) FROM Users GROUP BY age")
# users = cur.fetchall()
# for user in users:
#     print(user)

# cur.execute('SELECT COUNT(*) FROM Users')
#
# cur.execute('SELECT SUM(age) FROM Users')
# total1 = cur.fetchone()[0]
# cur.execute('SELECT COUNT(*) FROM Users')
# total2 = cur.fetchone()[0]
# print(total1)
# print(total2)
# print(total1, total1/total2)
#
#
# cur.execute('SELECT AVG(age) FROM Users')
# print(cur.fetchone()[0])
#
#
# conn.commit()
# conn.close()
#


def is_included(username):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        user_records = cur.execute("SELECT * FROM Users WHERE username = ?", (username,)).fetchall()

        return False if user_records == [] else True


print(is_included('qwer'))