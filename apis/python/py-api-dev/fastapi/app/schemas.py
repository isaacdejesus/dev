from pydantic import BaseModel, EmailStr
from datetime import datetime
class PostBase(BaseModel):
    title: str
    content:str
    published: bool = True

class PostCreate(PostBase): #extends PostBase
    pass #take all member functions from main class

class Post(PostBase): #model used to return data to user
    #inherit all fields from PostBase + any additional fields
    created_at: datetime
    id: int
    class Config: #used to pass pydantic model 
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr #validates email
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

###These are the pydantic models. They are used to define models for
###How we want the user to enter data and how we want to send data back
### It validates user input.
### 
