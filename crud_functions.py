import sqlite3


def initiate_db():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        )
        """)

        conn.commit()
#
#
def get_all_products():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        all_records = cur.execute("SELECT * FROM Products").fetchall()
        return all_records

