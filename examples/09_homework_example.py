import sys
from pathlib import Path

import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

sys.path.append(str(Path(__file__).resolve().parents[1]))

from models import Base, Homework, Student, Submission

@pytest.fixture(scope="function", autouse=False)
def db_session():
    engine = create_engine("sqlite:///orm_homework_tracker.db")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session =  Session()
    yield session
    session.close()


# Написать тест на обновление данных существующего студента.
# Нужно обновить значения полей всех.
# После обновления - убедиться, что данные клиента обновились сделав запрос в БД.

@pytest.fixture(scope="function", autouse=False)
def prepared_student(db_session):
    student = Student(name="Анна Петрова")
    db_session.add(student)
    db_session.commit()
    yield student
    db_session.delete(student)
    db_session.commit()


def filter_by_student(db_session, name):
    query = select(Student).filter_by(name=name)
    return db_session.scalars(query).one()


def test_update_student(db_session, prepared_student):
    student: Student = filter_by_student(db_session, prepared_student.name)

    assert student, "Student not found"

    new_name = "User Name"
    student.name = new_name
    db_session.commit()

    student_with_name: Student = filter_by_student(db_session, new_name)
    assert student_with_name.name == "Анна Петрова"












