from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import (
    Employee,
    Department,
    Job
)


class Repository:
    def __init__(self, db_uri: str):
        engine = create_engine(db_uri)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_commit(self, obj: Any):
        self.session.add(obj)
        self.session.commit()

    def get_attribute_by_id(self, model: Any, attribute_id: int):
        return self.session.query(model).filter_by(id=attribute_id).first()

    def get_all_attributes(self, model: Any):
        return self.session.query(model).all()

    def close(self):
        self.session.close()


class EmployeeRepository(Repository):

    def __init__(self, db_uri: str):
        super().__init__(db_uri)
    def create_employee(self, id_employee, name, hire_datetime, department_id, job_id):
        employee = Employee(
            id=id_employee,
            name=name,
            hire_datetime=hire_datetime,
            department_id=department_id,
            job_id=job_id
        )
        self.add_commit(employee)
        return employee

    def get_employee_by_id(self, employee_id):
        return self.get_attribute_by_id(Employee, employee_id)


class DepartmentRepository(Repository):
    def create_department(self, id_department, department):
        dpt = Department(id=id_department, department=department)
        self.add_commit(dpt)
        return dpt

    def get_department_by_id(self, department_id):
        return self.get_attribute_by_id(Department, department_id)


class JobRepository(Repository):
    def create_job(self, id_job, job):
        job = Job(id=id_job, job=job)
        self.add_commit(job)
        return job

    def get_job_by_id(self, job_id):
        return self.get_attribute_by_id(Job, job_id)

