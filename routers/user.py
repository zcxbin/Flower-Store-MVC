
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from configs.authentication import get_current_user
from configs.database import get_db
from schemas.user import User as UserSchema
from models.user import User as UserModel

router = APIRouter()


@router.get('')
async def get_user(user=Depends(get_current_user), db=Depends(get_db)):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return db.query(UserModel).all()

