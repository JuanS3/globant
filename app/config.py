import os


DATA_BASE_TYPE: str = os.getenv('DATABASE_TYPE')
DATA_BASE_USER: str = os.getenv('DATABASE_USER')
DATA_BASE_PASS: str = os.getenv('DATABASE_PASS')
DATA_BASE_HOST: str = os.getenv('DATABASE_HOST')
DATA_BASE_PORT: str = os.getenv('DATABASE_PORT')
DATA_BASE_NAME: str = os.getenv('DATABASE_NAME')

DB_URI = f'{DATA_BASE_TYPE}://{DATA_BASE_USER}:{DATA_BASE_PASS}@{DATA_BASE_HOST}:{DATA_BASE_PORT}/{DATA_BASE_NAME}'