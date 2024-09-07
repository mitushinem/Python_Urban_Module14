import sqlite3

with sqlite3.connect('not_telegram.db') as conn:
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER,
                balance INTEGER NOT NULL)
    ''')

    for i in range(1, 11):
        cur.execute(
            "INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
            (f'User{i}', f'example{i}@gmail.com', i * 10, 1000)
        )
    conn.commit()

    for i in range(1, 11, 2):
        cur.execute('UPDATE Users SET balance=? WHERE username = ?', (500, f'User{i}'))
    conn.commit()

    for i in range(1, 11, 3):
        cur.execute(f"DELETE FROM Users WHERE id={i}")
    conn.commit()

    result = cur.execute('SELECT * FROM Users WHERE age != 60').fetchall()
    for row in result:
        print(f'Имя: {row[1]} | Почта: {row[2]} | Возраст: {row[3]} | Баланс: {row[4]}')
