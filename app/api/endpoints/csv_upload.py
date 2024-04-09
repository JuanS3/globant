from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
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


@router.post("/upload/csv/departments/")
async def upload_csv_file(file: UploadFile = File(...)) -> dict[str, str]:
    """
    Upload a CSV file about deparments and save its data in the database.

    Parameters
    ----------
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

    return {'message': 'CSV file uploaded and data saved in the database.'}
