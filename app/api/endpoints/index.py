from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def read_root():
    return {'message': 'Globant\'s Data Engineering Coding Challenge API'}
