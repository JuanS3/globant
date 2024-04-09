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
                data = line.split(',')
                match model:
                    case 'employees':
                        repository.create_employee(*data)

                    case 'departments':
                        repository.create_department(*data)

                    case 'jobs':
                        repository.create_job(*data)

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
