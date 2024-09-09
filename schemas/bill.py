from typing import List
from pydantic import BaseModel

from schemas.base_response import BaseResponse


class Bill(BaseModel):
    id: int
    bill_date: str
    amount: int
    user_id: int

    class Config:
        from_attributes = True


class BillFlowerCreate(BaseModel):
    flower_id: int
    quantity: int


class BillCreate(BaseModel):
    bill_date: str
    flowers: List[BillFlowerCreate]

    class Config:
        from_attributes = True


class BillResponse(BaseResponse):
    data: List[Bill] = []
    length: int = 0
