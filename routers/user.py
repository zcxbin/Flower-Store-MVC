
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from configs.authentication import get_current_user
from configs.database import get_db
from exceptions import raise_error
from schemas.user import User as UserSchema
from models.user import User as UserModel
from services.user_service import get_user_service

router = APIRouter()


@router.get('')
async def get_user(user_service=Depends(get_user_service), user=Depends(get_current_user), db=Depends(get_db)):
    if user.role != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You can not read user account")
    try:
        users = user_service.get_all_users(db)
        if users is None:
            raise_error(200006)
        return users
    except Exception as e:
        return e


@router.get('/get_user_by_day')
async def get_user_by_day(
        day: str,
        month: str,
        year: str,
        user_service=Depends(get_user_service),
        user=Depends(get_current_user),
        db=Depends(get_db)):
    if user is None or user.role != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        users = user_service.get_users_by_day(db, day=day, month=month, year=year)
        if users is None:
            raise_error(200006)
        return users
    except Exception as e:
        return e


@router.get('/get_user_by_month')
async def get_user_by_month(
        month: str,
        year: str,
        user_service=Depends(get_user_service),
        user=Depends(get_current_user),
        db=Depends(get_db)
):
    if user is None or user.role != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        users = user_service.get_users_by_month(db, month=month, year=year)
        if users is None:
            raise_error(200006)
        return users
    except Exception as e:
        return e


@router.get('/get_user_by_year')
async def get_user_by_year(
        year: str,
        user_service=Depends(get_user_service),
        user=Depends(get_current_user),
        db=Depends(get_db)
):
    if user is None or user.role != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        users = user_service.get_users_by_year(db, year=year)
        if users is None:
            raise_error(200006)
        return users
    except Exception as e:
        return e
