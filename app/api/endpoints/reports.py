import config as cfg
from fastapi import APIRouter
from sqlalchemy import create_engine
from sqlalchemy.sql import text


router = APIRouter()


@router.get('/reports/hires/departments/q/{year}')
async def get_employees(year: int):
    """
    Get the number of employees hired by department in a given year.

    Parameters
    ----------
    year : int
        Year to get the data from.

    Returns
    -------
    list[dict[str, str|int]]
        Number of employees hired by department in a given year.
    """
    query = f"""
        with hired_by_qtr as (
            select
                d.department,
                j.job,
                extract('quarter' from e.hire_datetime) qtr,
                count(1) hired
            from
                departments d
                inner join employees e on e.department_id = d.id
                inner join jobs j on j.id = e.job_id
            where
                extract('year' from e.hire_datetime) = {year}
            group by
                d.department,
                j.job,
                extract('quarter' from e.hire_datetime)
        )

        select
            department,
            job,
            sum(case when qtr = 1 then hired else 0 end) q1,
            sum(case when qtr = 2 then hired else 0 end) q2,
            sum(case when qtr = 3 then hired else 0 end) q3,
            sum(case when qtr = 4 then hired else 0 end) q4
        from
            hired_by_qtr
        group by
            department,
            job
        order by
            department,
            job;
    """

    engine = create_engine(cfg.DB_URI)

    with engine.connect() as connection:
        result = connection.execute(text(query))
        rows = result.fetchall()

    result: list[dict[str, str|int]] = []
    for row in rows:
        result.append(
            {
                'department': row[0].replace("\r", ""),
                'job': row[1].replace("\r", ""),
                'q1': row[2],
                'q2': row[3],
                'q3': row[4],
                'q4': row[5]
            }
        )

    return result


@router.get('/reports/hires/departments/mean/{year}')
async def get_employees_mean(year: int):
    """
    Get the number of employees hired of each department in a given year
    that hired more employees than the mean of all departments in a given year.

    Parameters
    ----------
    year : int
        Year to get the data from.

    Returns
    -------
    list[dict[str, str|int]]
        Number of employees hired by department in a given year.
    """
    query = f"""
        with hired_by_dpt as (
            select
                d.id,
                d.department,
                count(1) hired,
                avg(count(1)) over() mean
            from
                departments d
                inner join employees e on e.department_id = d.id
            where
                extract('year' from e.hire_datetime) = {year}
            group by
                d.id,
                d.department
        )

        select
            id,
            department,
            hired
        from
            hired_by_dpt
        where
            hired > mean
        order by
            hired desc;
    """

    engine = create_engine(cfg.DB_URI)

    with engine.connect() as connection:
        result = connection.execute(text(query))
        rows = result.fetchall()

    result: list[dict[str, str|int]] = []
    for row in rows:
        result.append(
            {
                'id': row[0],
                'department': row[1].replace("\r", ""),
                'hired': row[2]
            }
        )

    return result
