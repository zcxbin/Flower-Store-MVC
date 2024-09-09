from sqlalchemy.orm import relationship

from configs.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False, unique=True, index=True)
    password = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False, default='user')
    total_money = Column(Integer, nullable=False, default=0)

    bills = relationship("Bill", back_populates="user")
