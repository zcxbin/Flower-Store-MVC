import traceback

from fastapi import APIRouter, Depends
from schemas.base_response import BaseResponse
from services.flower_service import get_flower_service
from configs.database import get_db
from configs.authentication import get_current_user
from schemas.flower import FlowerCreate, FlowerResponse
from exceptions import raise_error

router = APIRouter()


@router.get("", response_model=FlowerResponse | BaseResponse)
def get_all_flowers(flower_service=Depends(get_flower_service), db=Depends(get_db), user=Depends(get_current_user)):
    try:
        flowers = flower_service.get_all_flowers(db)
        return FlowerResponse(
            data=flowers,
            length=len(flowers)
        )
    except Exception:
        print(traceback.format_exc())
        return raise_error(200001)


@router.post("", response_model=FlowerResponse)
def create_flower(flower: FlowerCreate, flower_service=Depends(get_flower_service), db=Depends(get_db),
                  user=Depends(get_current_user)):
    try:
        if user.role != "admin":
            return FlowerResponse(
                message="You are not authorized to create a flower",
                status="error"
            )

        return FlowerResponse(
            data=[flower_service.create(flower, db)],
            length=1
        )
    except Exception:
        print(traceback.format_exc())
        return raise_error(200002)
