import sqlite3


connection = sqlite3.connect("homework_tracker.db")
cursor = connection.cursor()

# PRAGMA - специальная команда SQLite для настройки базы.
# foreign_keys = ON включает проверку FOREIGN KEY для этого подключения.
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("SELECT id FROM submissions ORDER BY id DESC LIMIT 1")
row = cursor.fetchone()
submission_id = row[0]

cursor.execute("DELETE FROM submissions WHERE id = ?", (submission_id,))

connection.commit()
print(f"Deleted submission #{submission_id}")

connection.close()
