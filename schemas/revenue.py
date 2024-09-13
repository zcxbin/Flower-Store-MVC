from pydantic import BaseModel


class RevenueByDate(BaseModel):
    total_revenue: int
    date: str

    class Config:
        from_attribute: True


