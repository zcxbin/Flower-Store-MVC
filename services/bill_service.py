from datetime import datetime

from sqlalchemy.orm import Session

from exceptions import raise_error
from models.bill import Bill as BillModel
from models.bill_flower import BillFlower as BillFlowerModel
from models.flower import Flower as FlowerModel
from schemas.base_response import BaseResponse
from schemas.bill import Bill as BillSchema, BillCreate, BillResponse
from typing import List

from models.user import User as UserModel


class BillService:
    def get_all_bills(self, db: Session, user_id: int) -> List[BillSchema]:
        return db.query(BillModel).filter(BillModel.user_id == user_id).all()

    def create_bill(self, db: Session, bill: BillCreate, user_id: int) -> BillSchema | None:
        total_amount = 0

        current_date = datetime.now().strftime('%Y-%m-%d')
        is_valid = True

        new_bill = BillModel(bill_date=current_date, user_id=user_id)

        for bill_flower in bill.flowers:
            if bill_flower.quantity <= 0:
                is_valid = False
            flower = db.query(FlowerModel).filter(FlowerModel.id == bill_flower.flower_id).first()
            if flower.quantity < 0 or flower.quantity < bill_flower.quantity:
                raise_error(200002)
            else:
                if flower:
                    amount = flower.price * bill_flower.quantity
                    total_amount += amount

                    bill_flower_model = BillFlowerModel(
                        flower_id=flower.id,
                        quantity=bill_flower.quantity
                    )
                    flower.quantity -= bill_flower.quantity
                    new_bill.bill_flowers.append(bill_flower_model)

        if is_valid:
            new_bill.amount = total_amount

            user_model = db.query(UserModel).filter(UserModel.id == user_id).first()
            user_model.total_money += total_amount
            db.add(new_bill)
            db.commit()
            db.refresh(new_bill)

            return new_bill
        else:
            return None
