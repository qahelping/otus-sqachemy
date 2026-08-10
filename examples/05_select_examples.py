import sqlite3


connection = sqlite3.connect("homework_tracker.db")
cursor = connection.cursor()

# PRAGMA - специальная команда SQLite для настройки базы.
# foreign_keys = ON включает проверку FOREIGN KEY для этого подключения.
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS homeworks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    accepted BOOLEAN NOT NULL DEFAULT False,
    student_id INTEGER NOT NULL,
    homework_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (homework_id) REFERENCES homeworks(id),
    CHECK (accepted IN (False, True))
)
""")

cursor.execute("DELETE FROM submissions")
cursor.execute("DELETE FROM homeworks")
cursor.execute("DELETE FROM students")
cursor.execute("DELETE FROM sqlite_sequence")

cursor.execute(
    "INSERT INTO students (name) VALUES (?)",
    ("Анна Петрова",),
)
# lastrowid хранит id строки, которую только что добавили через INSERT.
anna_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO students (name) VALUES (?)",
    ("Борис Смирнов",),
)
# Этот id нужен ниже, чтобы связать Бориса с его сдачей.
boris_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO homeworks (title) VALUES (?)",
    ("SQL SELECT",),
)
# id задания нужен для записи в submissions.homework_id.
first_homework_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO homeworks (title) VALUES (?)",
    ("CRUD",),
)
# id второго задания тоже нужен для связи со сдачей.
second_homework_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO submissions (student_id, homework_id, accepted) VALUES (?, ?, ?)",
    (anna_id, first_homework_id, True),
)

cursor.execute(
    "INSERT INTO submissions (student_id, homework_id, accepted) VALUES (?, ?, ?)",
    (boris_id, second_homework_id, False),
)

connection.commit()

print("1. All students")
cursor.execute("SELECT id, name FROM students")
print(cursor.fetchall())

print("\n2. WHERE")
cursor.execute("SELECT id, name FROM students WHERE name = ?", ("Анна Петрова",))
print(cursor.fetchall())

print("\n3. ORDER BY")
cursor.execute("SELECT id, title FROM homeworks ORDER BY title")
print(cursor.fetchall())

print("\n4. JOIN")
cursor.execute("""
SELECT students.name, homeworks.title, submissions.accepted
FROM submissions
JOIN students ON students.id = submissions.student_id
JOIN homeworks ON homeworks.id = submissions.homework_id
ORDER BY students.name
""")
for student_name, homework_title, accepted in cursor.fetchall():
    print(student_name, homework_title, bool(accepted))

print("\n5. COUNT")
cursor.execute("SELECT COUNT(*) FROM submissions")
print(cursor.fetchone()[0])

print("\n6. accepted=False")
cursor.execute("SELECT id, student_id, homework_id FROM submissions WHERE accepted = False")
print(cursor.fetchall())

connection.close()
