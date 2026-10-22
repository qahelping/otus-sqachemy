import sqlite3


connection = sqlite3.connect("homework_tracker.db")
cursor = connection.cursor()


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

connection.commit()
connection.close()

print("Database schema created")
