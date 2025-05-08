from fastapi import FastAPI 
from app.database.database import Base, engine
from app.routers import todo_router
from app.routers import user_router

app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(todo_router.router)

app.include_router(user_router.router)