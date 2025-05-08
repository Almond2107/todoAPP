from fastapi import APIRouter, status, Depends
from fastapi import HTTPException
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

@router.put("/{todo_id}", response_model=todo_schema.TodoShow)
def update_todo(todo_id: int, todo: todo_schema.TodoCreate, db: Session = Depends(get_db)):
    updated = todo_crud.update_todo(db, todo_id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="Ohh sorry, Todo not found")
    return updated

@router.delete("/{todo_id}", response_model=todo_schema.TodoShow)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    deleted = todo_crud.delete_todo(db, todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Ohh sorry, Todo not found")
    return deleted
