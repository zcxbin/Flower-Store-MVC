import traceback
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.base_response import BaseResponse
from schemas.bill import BillResponse, BillCreate
from configs.database import get_db
from configs.authentication import get_current_user
from services.bill_service import BillService
from exceptions import raise_error
from services.user_service import get_user_service

router = APIRouter()


@router.get("", response_model=BillResponse | BaseResponse)
def get_all_bills(
        db: Session = Depends(get_db),
        user=Depends(get_current_user),
        bill_service: BillService = Depends()
):
    try:
        # print(user)
        bills = bill_service.get_all_bills(db, user.id)
        return BillResponse(
            data=bills,
            length=len(bills)
        )
    except Exception:
        print(traceback.format_exc())
        return raise_error(200001)


@router.post("", response_model=BillResponse)
def create_bill(
        bill: BillCreate,
        db: Session = Depends(get_db),
        user=Depends(get_current_user),
        bill_service: BillService = Depends(),
        user_service=Depends(get_user_service)
):
    try:
        new_bill = bill_service.create_bill(db, bill, user.id)
        if new_bill is not None:
            user_service.set_user_level(db, user.id)
            return BillResponse(
                data=[new_bill],
                length=1
            )
        else:
            return raise_error(200013)
    except Exception:
        print(traceback.format_exc())
        return raise_error(200002)
