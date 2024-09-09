from sqlalchemy.orm import Session
from models.flower import Flower as FlowerModel
from schemas.flower import Flower as FlowerSchema, FlowerCreate
from typing import List


def get_flower_service():
    try:
        yield FlowerService()
    finally:
        pass


class FlowerService:
    def get_all_flowers(self, db: Session) -> List[FlowerSchema]:
        return db.query(FlowerModel).all()

    def create(self, flower: FlowerCreate, db: Session) -> FlowerSchema:
        new_flower = FlowerModel(**flower.model_dump())
        db.add(new_flower)
        db.commit()
        db.refresh(new_flower)
        return new_flower
