from sqlalchemy.orm import relationship

from configs.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class BillFlower(Base):
    __tablename__ = 'bill_flower'
    id = Column(Integer, primary_key=True, index=True)
    bill_id = Column(Integer, ForeignKey("bills.id"), nullable=False)
    flower_id = Column(Integer, ForeignKey("flowers.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    bill = relationship("Bill", back_populates="bill_flowers")
    flower = relationship("Flower", back_populates="bill_flowers")
