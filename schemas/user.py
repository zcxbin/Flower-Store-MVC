from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    total_amount: int = 0
    role: str
