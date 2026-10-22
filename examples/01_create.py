import sqlite3


connection = sqlite3.connect("homework_tracker.db")
cursor = connection.cursor()


cursor.execute(
    "INSERT INTO students (name) VALUES (?)",
    ("Анна Петрова",),
)
cursor.execute(
    "INSERT INTO students (name) VALUES (?)",
    ("Макс Фрай",),
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
cursor.execute(
    "INSERT INTO submissions (student_id, homework_id, accepted) VALUES (?, ?, ?)",
    (2, 1, True),
)
# id созданной сдачи используем только для вывода на экран.
submission_id = cursor.lastrowid

connection.commit()
connection.close()

print(f"Created student #{student_id}")
print(f"Created homework #{homework_id}")
print(f"Created submission #{submission_id}")
