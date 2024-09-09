from fastapi import FastAPI
from configs.database import Base, engine
from routers.authentication import router as auth_router
from routers.flower import router as flower_router
from routers.bill import router as bill_router

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(auth_router, prefix='/auth', tags=['Auth'])
app.include_router(flower_router, prefix="/flowers", tags=["Flowers"])
app.include_router(bill_router, prefix="/bills", tags=["Bills"])
