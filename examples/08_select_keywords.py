import sqlite3


connection = sqlite3.connect("select_keywords_demo.db")
cursor = connection.cursor()

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

cursor.execute("INSERT INTO students (name) VALUES (?)", ("Анна Петрова",))
anna_id = cursor.lastrowid

cursor.execute("INSERT INTO students (name) VALUES (?)", ("Борис Смирнов",))
boris_id = cursor.lastrowid

cursor.execute("INSERT INTO students (name) VALUES (?)", ("Мария Иванова",))
maria_id = cursor.lastrowid

cursor.execute("INSERT INTO homeworks (title) VALUES (?)", ("SQL SELECT",))
select_homework_id = cursor.lastrowid

cursor.execute("INSERT INTO homeworks (title) VALUES (?)", ("CRUD",))
crud_homework_id = cursor.lastrowid

cursor.execute("INSERT INTO homeworks (title) VALUES (?)", ("ORM",))
orm_homework_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO submissions (student_id, homework_id, accepted) VALUES (?, ?, ?)",
    (anna_id, select_homework_id, True),
)
cursor.execute(
    "INSERT INTO submissions (student_id, homework_id, accepted) VALUES (?, ?, ?)",
    (boris_id, crud_homework_id, False),
)
cursor.execute(
    "INSERT INTO submissions (student_id, homework_id, accepted) VALUES (?, ?, ?)",
    (maria_id, orm_homework_id, False),
)

connection.commit()

print("1. SELECT + FROM: выбрать все имена студентов")
cursor.execute("SELECT name FROM students")
print(cursor.fetchall())

print("\n2. SELECT несколько колонок")
cursor.execute("SELECT id, name FROM students")
print(cursor.fetchall())

print("\n3. WHERE: фильтр по точному имени")
cursor.execute("SELECT id, name FROM students WHERE name = ?", ("Анна Петрова",))
print(cursor.fetchall())

print("\n4. LIKE: поиск по части текста")
cursor.execute("SELECT id, name FROM students WHERE name LIKE ?", ("%ова",))
print(cursor.fetchall())

print("\n5. ORDER BY: сортировка")
cursor.execute("SELECT id, title FROM homeworks ORDER BY title")
print(cursor.fetchall())

print("\n6. LIMIT: взять только первые две строки")
cursor.execute("SELECT id, name FROM students ORDER BY id LIMIT 2")
print(cursor.fetchall())

print("\n7. AND: несколько условий одновременно")
cursor.execute("""
SELECT id, student_id, homework_id, accepted
FROM submissions
WHERE accepted = False AND student_id = ?
""", (boris_id,))
print(cursor.fetchall())

print("\n8. OR: подходит одно условие или другое")
cursor.execute("""
SELECT id, title
FROM homeworks
WHERE title = ? OR title = ?
""", ("CRUD", "ORM"))
print(cursor.fetchall())

print("\n9. JOIN: связать студентов, задания и сдачи")
cursor.execute("""
SELECT students.name, homeworks.title, submissions.accepted
FROM submissions
JOIN students ON students.id = submissions.student_id
JOIN homeworks ON homeworks.id = submissions.homework_id
ORDER BY students.name
""")
for student_name, homework_title, accepted in cursor.fetchall():
    print(student_name, homework_title, bool(accepted))

print("\n10. COUNT + GROUP BY: посчитать сдачи по статусу")
cursor.execute("""
SELECT accepted, COUNT(*)
FROM submissions
GROUP BY accepted
ORDER BY accepted
""")
for accepted, count in cursor.fetchall():
    print(bool(accepted), count)

connection.close()
