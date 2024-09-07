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

cur.execute('SELECT COUNT(*) FROM Users')

cur.execute('SELECT SUM(age) FROM Users')
total1 = cur.fetchone()[0]
cur.execute('SELECT COUNT(*) FROM Users')
total2 = cur.fetchone()[0]
print(total1)
print(total2)
print(total1, total1/total2)


cur.execute('SELECT AVG(age) FROM Users')
print(cur.fetchone()[0])


conn.commit()
conn.close()

