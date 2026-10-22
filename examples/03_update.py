import sqlite3


connection = sqlite3.connect("homework_tracker.db")
cursor = connection.cursor()


cursor.execute("SELECT * FROM submissions ORDER BY id LIMIT 1")
row = cursor.fetchall()
print(row)

cursor.execute(
    "UPDATE submissions SET accepted = ? WHERE id = ?",
    (True, 1),
)

connection.commit()

cursor.execute("SELECT * FROM submissions ORDER BY id LIMIT 1")
row = cursor.fetchall()
print(row)
connection.close()
