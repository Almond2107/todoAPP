from sqlalchemy.orm import Session
from app.models import todo_model
from app.schemas import todo_schema

def get_todos(db: Session):
    return db.query(todo_model.Todo).all()

def create_todo(db: Session, todo: todo_schema.TodoCreate):
    db_todo = todo_model.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo