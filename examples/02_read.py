import sqlite3


connection = sqlite3.connect("homework_tracker.db")
cursor = connection.cursor()

# PRAGMA - специальная команда SQLite для настройки базы.
# foreign_keys = ON включает проверку FOREIGN KEY для этого подключения.
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
SELECT
    students.name,
    homeworks.title,
    submissions.accepted
FROM submissions
JOIN students ON students.id = submissions.student_id
JOIN homeworks ON homeworks.id = submissions.homework_id
ORDER BY submissions.id
""")

rows = cursor.fetchall()

for row in rows:
    student_name = row[0]
    homework_title = row[1]
    accepted = bool(row[2])

    print(f"{student_name} | {homework_title} | accepted={accepted}")

connection.close()
