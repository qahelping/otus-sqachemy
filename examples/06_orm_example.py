import sys
from pathlib import Path

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

sys.path.append(str(Path(__file__).resolve().parents[1]))

from models import Base, Homework, Student, Submission


engine = create_engine("sqlite:///orm_homework_tracker.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

student = Student(name="Анна Петрова")
# cursor.execute(
#     "INSERT INTO students (name) VALUES (?)",
#     ("Анна Петрова",),
# )


homework = Homework(title="SQLAlchemy ORM")
submission = Submission(student=student, homework=homework, accepted=False)

session.add(student)
session.add(homework)
session.add(submission)
session.commit()

query = select(Submission).join(Student).join(Homework)
submissions = session.scalars(query).all()

for item in submissions:
    print(f"{item.student.name}: {item.homework.title} | accepted={item.accepted}")

submission.accepted = True
session.commit()

print("Status changed to accepted")

session.delete(submission)
session.commit()

print("Submission deleted")

session.close()
