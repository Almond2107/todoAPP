from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import todo_crud
from app.schemas import todo_schema
from app.database import database

router = APIRouter(prefix="/todos", tags=["Todos"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[todo_schema.TodoShow])
def read_todos(db: Session = Depends(get_db)):
    return todo_crud.get_todos(db)

@router.post("/", response_model=todo_schema.TodoShow)
def create_todo(todo: todo_schema.TodoCreate, db: Session = Depends(get_db)):
    return todo_crud.create_todo(db, todo)
