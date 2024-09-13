from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy import func

from exceptions import raise_error
from models.bill import Bill as BillModel
from schemas.revenue import RevenueByDate


def get_revenue_service():
    try:
        yield RevenueService()
    finally:
        pass


class RevenueService:
    def get_all_revenues(self, db: Session) -> int:
        total_revenue = db.query(func.sum(BillModel.amount)).scalar()
        return total_revenue

    def get_revenue_by_day(self, db: Session, day: str, month: str, year: str) -> RevenueByDate:
        target_date_str = ""
        try:
            target_date = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d").date()
            target_date_str = target_date.strftime("%Y-%m-%d")
        except ValueError:
            raise_error(200011)
        total_revenue = db.query(func.sum(BillModel.amount)).filter(BillModel.bill_date == target_date_str).scalar()
        if not total_revenue:
            raise_error(200012)
        return RevenueByDate(
            total_revenue=total_revenue,
            date=f'{year}-{month}-{day}'
        )

    def get_revenue_by_month(self, db: Session, month: str, year: str) -> RevenueByDate:
        target_date_str = ""
        try:
            target_date = datetime.strptime(f"{year}-{month}", "%Y-%m-%d").date()
            target_date_str = target_date.strftime("%Y-%m-%d")
        except ValueError:
            raise_error(200011)

        total_revenue = db.query(func.sum(BillModel.amount)) \
            .filter(BillModel.bill_date.startswith(target_date_str)).scalar()
        if not total_revenue:
            raise_error(200012)
        return RevenueByDate(
            total_revenue=total_revenue,
            date=f'{year}-{month}'
        )

    def get_revenue_by_year(self, db: Session, year: str) -> RevenueByDate:
        target_date_str = ""
        try:
            target_date = datetime.strptime(f"{year}", "%Y-%m-%d").date()
            target_date_str = target_date.strftime("%Y-%m-%d")
        except ValueError:
            raise_error(200011)
        total_revenue = db.query(func.sum(BillModel.amount)) \
            .filter(BillModel.bill_date.startswith(target_date_str)).scalar()
        if not total_revenue:
            raise_error(200012)
        return RevenueByDate(
            total_revenue=total_revenue,
            date=f'{year}'
        )
