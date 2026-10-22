import sqlite3


connection = sqlite3.connect("homework_tracker.db")
cursor = connection.cursor()

cursor.execute("DELETE FROM submissions WHERE id = ? or accepted = ?", (2,))



cursor.execute("SELECT * FROM submissions")
row = cursor.fetchall()
print(row)

connection.close()
