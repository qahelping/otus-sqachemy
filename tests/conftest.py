import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Homework, Student, Submission


@pytest.fixture
def db_session(tmp_path):
    db_path = tmp_path / "test_homework_tracker.db"
    engine = create_engine(f"sqlite:///{db_path}")

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    anna = Student(name="Анна Петрова")
    boris = Student(name="Борис Смирнов")
    sql_homework = Homework(title="SQL SELECT")
    crud_homework = Homework(title="CRUD")

    anna_submission = Submission(
        student=anna,
        homework=sql_homework,
        accepted=False,
    )
    boris_submission = Submission(
        student=boris,
        homework=crud_homework,
        accepted=True,
    )

    session.add_all([
        anna,
        boris,
        sql_homework,
        crud_homework,
        anna_submission,
        boris_submission,
    ])
    session.commit()

    yield session

    session.close()
