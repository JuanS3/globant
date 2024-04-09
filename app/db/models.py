from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hire_datetime = Column(TIMESTAMP)
    department_id = Column(Integer, foreign_key='departments.id')
    job_id = Column(Integer, foreign_key='jobs.id')


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    department = Column(String)


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    job = Column(String)
