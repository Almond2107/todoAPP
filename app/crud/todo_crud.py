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

def update_todo(db: Session, todo_id: int, todo: todo_schema.TodoCreate):
    db_todo = db.query(todo_model.Todo).filter(todo_model.Todo.id == todo_id).first()
    if not db_todo:
        return None
    for key, value in todo.dict().items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return todo


def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(todo_model.Todo).filter(todo_model.Todo.id == todo_id).first()
    if not db_todo:
        return None
    db.delete(db_todo)
    db.commit()
    return db_todo