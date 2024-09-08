import sqlite3
from random import randint

conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

def add_user(user_id, username, first_name):
    check_user = cur.execute("SELECT * FROM Users WHERE id = ?", (user_id, ))

    if check_user.fetchone() is None:
        cur.execute(f"""
        INSERT INTO Users VALUES('{user_id}','{username}','{first_name}',0)
        """)


def show_users():
    users_list = cur.execute("SELECT * FROM Users")
    message = ''
    for user in users_list:
        message += f"{user[0]}@{user[1]} {user[2]}\n"
    conn.commit()
    return message


def show_stat():
    count_users = cur.execute("SELECT COUNT(*) FROM Users").fetchone()[0]
    conn.commit()

    return count_users

def remove_blacklist(inpup_id):
    cur.execute('UPDATE Users SET block = ? WHERE id = ?', (0, inpup_id,))
    conn.commit()

def add_to_blacklist(inpup_id):
    cur.execute('UPDATE Users SET block = ? WHERE id = ?', (1, inpup_id,))
    conn.commit()

def check_block(user_id):
    users = cur.execute(f"SELECT block FROM Users WHERE id = {user_id}").fetchone()[0]
    return users







conn.commit()
conn.close()

