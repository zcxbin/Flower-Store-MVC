from sqlalchemy.orm import relationship

from configs.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Bill(Base):
    __tablename__ = 'bills'
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, nullable=False)
    bill_date = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='bills')
    bill_flowers = relationship("BillFlower", back_populates="bill")

