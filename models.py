from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    submissions = relationship(
        "Submission",
        back_populates="student",
        cascade="all, delete-orphan",
    )


class Homework(Base):
    __tablename__ = "homeworks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    submissions = relationship("Submission", back_populates="homework")


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True)
    accepted = Column(Boolean, default=False, nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    homework_id = Column(Integer, ForeignKey("homeworks.id"), nullable=False)

    student = relationship("Student", back_populates="submissions")
    homework = relationship("Homework", back_populates="submissions")
