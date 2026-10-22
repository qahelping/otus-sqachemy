import sqlite3


connection = sqlite3.connect("cursor_values_demo.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("DELETE FROM students")
cursor.execute("DELETE FROM sqlite_sequence")

cursor.execute(
    "INSERT INTO students (name) VALUES (?)",
    ("Анна Петрова",),
)

# lastrowid хранит id строки, которую только что добавили через INSERT.
print("lastrowid after INSERT:", cursor.lastrowid)

cursor.execute(
    "INSERT INTO students (name) VALUES (?)",
    ("Борис Смирнов",),
)

print("lastrowid after second INSERT:", cursor.lastrowid)

cursor.execute("SELECT id, name FROM students ORDER BY id")

# description хранит информацию о колонках в результате SELECT.
print("description after SELECT:", cursor.description)

# fetchone возвращает одну следующую строку результата.
first_row = cursor.fetchone()
print("fetchone:", first_row)

# fetchall возвращает все оставшиеся строки результата.
other_rows = cursor.fetchall()
print("fetchall:", other_rows)

cursor.execute(
    "UPDATE students SET name = ? WHERE id = ?",
    ("Анна Иванова", 1),
)

# rowcount показывает, сколько строк изменил последний UPDATE или DELETE.
print("rowcount after UPDATE:", cursor.rowcount)

cursor.execute("DELETE FROM students WHERE id = ?", (2,))
print("rowcount after DELETE:", cursor.rowcount)

connection.commit()
connection.close()
