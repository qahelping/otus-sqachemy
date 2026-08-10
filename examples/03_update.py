import sqlite3


connection = sqlite3.connect("homework_tracker.db")
cursor = connection.cursor()

# PRAGMA - специальная команда SQLite для настройки базы.
# foreign_keys = ON включает проверку FOREIGN KEY для этого подключения.
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("SELECT id FROM submissions ORDER BY id LIMIT 1")
row = cursor.fetchone()
submission_id = row[0]

cursor.execute(
    "UPDATE submissions SET accepted = ? WHERE id = ?",
    (True, submission_id),
)

connection.commit()
print(f"Submission #{submission_id} accepted=True")

connection.close()
