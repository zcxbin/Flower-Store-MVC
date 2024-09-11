from sqlalchemy.orm import Session
from exceptions import raise_error
from typing import List, Set, Any
from datetime import datetime
from schemas.user import User as UserSchema
from models.user import User as UserModel
from models.bill import Bill as BillModel


def get_user_service():
    try:
        yield UserService()
    finally:
        pass


class UserService:
    def get_all_users(self, db: Session) -> List[UserSchema]:
        return db.query(UserModel).all()

    def get_user_by_id(self, db: Session, user_id: int) -> UserSchema:
        return db.query(UserModel).filter(UserModel.id == user_id).first()

    def get_users_by_day(self, db: Session, day: str, month: str, year: str) -> set[UserSchema]:
        try:
            target_date = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d").date()
            target_date_str = target_date.strftime('%Y-%m-%d')
            # print(f"Target date: {target_date}")
        except ValueError:
            raise_error(200007)
        bills = db.query(BillModel).filter(BillModel.bill_date == target_date_str).all()

        # print(bills)
        if not bills:
            raise_error(200008)

        users = set(bill.user for bill in bills)

        return users

    def get_users_by_month(self, db: Session, month: str, year: str) -> set[UserSchema]:
        try:
            target_year_month = f"{year}-{month}"  # Format the target as YYYY-MM
            print(f"Target year and month: {target_year_month}")
        except ValueError:
            raise_error(200007)

        bills = db.query(BillModel).filter(BillModel.bill_date.startswith(target_year_month)).all()

        if not bills:
            raise_error(200008)

        users = set(bill.user for bill in bills)
        return users

    def get_users_by_year(self, db: Session, year: str) -> set[UserSchema]:
        try:
            target_year = f"{year}"
            print(f"Target year and month: {target_year}")
        except ValueError:
            raise_error(200007)

        bills = db.query(BillModel).filter(BillModel.bill_date.startswith(target_year)).all()

        if not bills:
            raise_error(200008)

        users = set(bill.user for bill in bills)
        return users

    def set_user_level(self, db: Session, user_id: int) -> UserSchema:
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise_error(200008)
        if user.total_money >= 5000000:
            user.loyal_level = "Diamond"
        elif user.total_money >= 2000000:
            user.loyal_level = "Gold"
        elif user.total_money >= 1000000:
            user.loyal_level = "Silver"
        elif user.total_money >= 500000:
            user.loyal_level = "Bronze"
        else:
            user.loyal_level = "New Account"

        db.commit()
        db.refresh(user)
        return user
