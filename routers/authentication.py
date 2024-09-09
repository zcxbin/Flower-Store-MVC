from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from configs.database import get_db
from schemas.authentication import Register
from services.authentication_service import get_authen_service

router = APIRouter()


@router.post('/login')
def login(login_data: OAuth2PasswordRequestForm = Depends(), authentication_service=Depends(get_authen_service)
          , db=Depends(get_db)):
    try:
        response = authentication_service.authenticate_user(login_data, db)
        if response is None:
            return None
        return response
    except Exception as e:
        return e


@router.post('/register')
def register(register_data: Register, authentication_service=Depends(get_authen_service), db=Depends(get_db)):
    try:
        return authentication_service.register_user(register_data, db)
    except Exception as e:
        return e
