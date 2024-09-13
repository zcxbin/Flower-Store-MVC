from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
import traceback
from sqlalchemy.orm import Session
from configs.database import get_db
from configs.authentication import get_current_user
from exceptions import raise_error
from services.revenue_service import get_revenue_service

router = APIRouter()


@router.get('/get_all_revenue')
async def get_revenue(db: Session = Depends(get_db),
                      user=Depends(get_current_user),
                      revenue_service=Depends(get_revenue_service)):
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail='Not enough permissions')
    return revenue_service.get_all_revenues(db)


@router.get('/get_revenue_by_day')
async def get_revenue_by_day(
        day: str,
        month: str,
        year: str,
        db: Session = Depends(get_db),
        user=Depends(get_current_user),
        revenue_service=Depends(get_revenue_service)):
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail='Not enough permissions')
    return revenue_service.get_revenue_by_day(db, day, month, year)


@router.get('/get_revenue_by_month')
async def get_revenue_by_month(
        month: str,
        year: str,
        db: Session = Depends(get_db),
        user=Depends(get_current_user),
        revenue_service=Depends(get_revenue_service)):
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail='Not enough permissions')
    return revenue_service.get_revenue_by_day(db, month, year)


@router.get('/get_revenue_by_year')
async def get_revenue_by_day(
        year: str,
        db: Session = Depends(get_db),
        user=Depends(get_current_user),
        revenue_service=Depends(get_revenue_service)):
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail='Not enough permissions')
    return revenue_service.get_revenue_by_day(db, year)
