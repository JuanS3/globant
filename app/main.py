from fastapi import FastAPI
from api.endpoints import (
    csv_upload,
    index
)

import uvicorn


app = FastAPI(
    title='Globant\'s  Data  Engineering  Coding Challenge',
    description='API for uploading CSV files and saving their data in the database, as part of Globant\'s Data Engineering Coding Challenge.',
    summary='API for uploading CSV files and saving their data in the database',
    version='0.0.1',
)

app.include_router(index.router)
app.include_router(csv_upload.router)


def main():
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)


if __name__ == "__main__":
    main()
