import sqlite3


connection = sqlite3.connect("homework_tracker.db")
cursor = connection.cursor()

# PRAGMA - специальная команда SQLite для настройки базы.
# foreign_keys = ON включает проверку FOREIGN KEY для этого подключения.
cursor.execute("PRAGMA foreign_keys = ON")


cursor.execute(
    "INSERT INTO students (name) VALUES (?)",
    ("Анна Петрова",),
)
# lastrowid хранит id строки, которую только что добавили через INSERT.
student_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO homeworks (title) VALUES (?)",
    ("SQL SELECT",),
)
# Этот id нужен, чтобы связать сдачу с только что созданным заданием.
homework_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO submissions (student_id, homework_id, accepted) VALUES (?, ?, ?)",
    (student_id, homework_id, False),
)
# id созданной сдачи используем только для вывода на экран.
submission_id = cursor.lastrowid

connection.commit()
connection.close()

print(f"Created student #{student_id}")
print(f"Created homework #{homework_id}")
print(f"Created submission #{submission_id}")
