from sqlalchemy import select

from models import Homework, Student, Submission


def test_add_student(db_session):
    student = Student(name="Мария Иванова")
    db_session.add(student)
    db_session.commit()

    # scalars выполняет SELECT и возвращает ORM-объекты без лишней обертки строк.
    result = db_session.scalars(
        select(Student).where(Student.name == "Мария Иванова")
    ).all()

    assert len(result) == 1
    assert result[0].name == "Мария Иванова"


def test_delete_student(db_session):
    student = db_session.scalars(
        select(Student).where(Student.name == "Борис Смирнов")
    ).one()

    db_session.delete(student)
    db_session.commit()

    students = db_session.scalars(select(Student).order_by(Student.name)).all()
    names = [student.name for student in students]

    assert names == ["Анна Петрова"]


def test_accept_homework(db_session):
    submission = db_session.scalars(
        select(Submission)
        .join(Student)
        .join(Homework)
        .where(Student.name == "Анна Петрова")
        .where(Homework.title == "SQL SELECT")
    ).one()

    assert submission.accepted is False

    submission.accepted = True
    db_session.commit()

    updated_submission = db_session.get(Submission, submission.id)

    assert updated_submission.accepted is True
