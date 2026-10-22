import sqlite3


connection = sqlite3.connect("homework_tracker.db")
cursor = connection.cursor()


cursor.execute("""
SELECT *
FROM students
WHERE id > 3
""")

rows = cursor.fetchall()

print(rows)


cursor.execute("""
SELECT
    students.name,
    homeworks.title,
    submissions.accepted
FROM submissions
JOIN students ON students.id = submissions.student_id
JOIN homeworks ON homeworks.id = submissions.homework_id
WHERE  submissions.accepted = 1
""")

rows = cursor.fetchall()
for row in rows:
    student_name = row[0]
    homework_title = row[1]
    accepted = bool(row[2])

    print(f"{student_name} | {homework_title} | accepted={accepted}")

connection.close()
