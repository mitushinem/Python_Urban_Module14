import sqlite3


def initiate_db():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL)
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL)
        """)

        conn.commit()


#
#
def get_all_products():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        all_records = cur.execute("SELECT * FROM Products").fetchall()
        return all_records


def is_included(username):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        user_records = cur.execute("SELECT * FROM Users WHERE username = ?", (username,)).fetchall()

        return False if user_records == [] else True


def add_user(username, email, age):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        if not is_included(username):
            cur.execute(
                f"INSERT INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', '{age}', 1000)", )
            conn.commit()
