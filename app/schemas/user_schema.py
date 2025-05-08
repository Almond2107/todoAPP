from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr


    class Config:
        orm_mode = True
    
class UserLogin(BaseModel):
    username: str
    password: str