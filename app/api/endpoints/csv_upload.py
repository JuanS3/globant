import config as cfg
from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

from db.repository import (
    Repository,
    EmployeeRepository,
    DepartmentRepository,
    JobRepository
)

router = APIRouter()


def verify_csv(file: UploadFile) -> None:
    """
    Verify that the file is a CSV file.

    Parameters
    ----------
    file : UploadFile
        File to verify.

    Raises
    ------
    HTTPException
        status_code : 400
            If the file is not a CSV file.
    """
    if not file.filename.endswith('.csv'):
        raise HTTPException(
            status_code=400,
            detail='Must be a CSV file.'
        )


def validate_data(data: list[str]) -> list[str]:
    """
    Validate the data in the CSV file.

    Parameters
    ----------
    data : list[str]
        Data to validate.

    Returns
    -------
    list[str]
        Data validated.
    """
    return [d if d.strip() != '' else None for d in data]


async def save_csv(content_file: bytes, model: str) -> dict[str, str]:
    """
    Save the data in the CSV file in the database.

    Parameters
    ----------
    content_file : bytes
        Content of the CSV file.
    model : str
        Type of data in the CSV file (e.g., 'departments', 'employees', 'jobs').

    Returns
    -------
    dict[str, str]
        A message indicating that the data was saved in the database.
    """
    message: dict[str, str] = {}
    repository: Repository = None
    match model:
        case 'employees':
            repository: EmployeeRepository = EmployeeRepository(cfg.DB_URI)

        case 'departments':
            repository: DepartmentRepository = DepartmentRepository(cfg.DB_URI)

        case 'jobs':
            repository: JobRepository = JobRepository(cfg.DB_URI)

    n: int = 0
    try:

        for line in content_file.decode().split('\n'):

            if line:
                data = validate_data(line.split(','))
                match model:
                    case 'employees':
                        try:
                            repository.create_employee(*data)
                        except Exception as e:
                            if 'error_employees' in message:
                                message['error_employees'] = []
                            message['error_employees'].append(f'Error saving employee: {e}')

                    case 'departments':
                        try:
                            repository.create_department(*data)
                        except Exception as e:
                            if 'error_departments' in message:
                                message['error_departments'] = []
                            message['error_departments'].append(f'Error saving department: {e}')

                    case 'jobs':
                        try:
                            repository.create_job(*data)
                        except Exception as e:
                            if 'error_jobs' in message:
                                message['error_jobs'] = []
                            message['error_jobs'].append(f'Error saving job: {e}')
                n += 1

        message['ok'] = 'Data saved in the database.'

    except Exception as e:

        message['error'] = f'Error saving data in the database: {e}'

    finally:

        repository.close()
        message['records_saved'] = f'{n} records saved in the database.'

    return message


@router.post("/upload/csv/{model}/")
async def upload_csv_file(model: str, file: UploadFile = File(...)) -> dict[str, str]:
    """
    Upload a CSV file about deparments and save its data in the database.

    Parameters
    ----------
    data_type : str
        Type of data in the CSV file (e.g., 'departments', 'employees', 'jobs').
    file : UploadFile
        Archivo CSV a cargar.

    Returns
    -------
    dict
        A message indicating that the CSV file was uploaded and its data was saved in the database.

    Raises
    ------
    HTTPException
        status_code : 400
            If the file is not a CSV file.
        status_code : 500
            If the data could not be saved in the database.
    """
    verify_csv(file)

    content = await file.read()

    if not model in ('employees', 'departments', 'jobs'):
        raise HTTPException(
            status_code=400,
            detail='Invalid data type. Must be "employees", "departments", or "jobs".'
        )

    message: dict[str, str] = await save_csv(content, model)

    if 'error' in message:
        raise HTTPException(
            status_code=500,
            detail=message
        )

    message['message'] = f'CSV file uploaded and data saved in the database.'
    return message
