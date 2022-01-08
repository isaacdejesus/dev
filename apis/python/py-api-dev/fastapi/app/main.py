from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
import time
from psycopg2.extras import RealDictCursor
from . import models,schemas, utils
from sqlalchemy.orm import Session
from .database import engine, get_db#used by sqlalch
models.Base.metadata.create_all(bind=engine)#user by sqlalch
from .routers import post, user

app = FastAPI()
#define structure of user input
#it validates user input
class Post(BaseModel):
    title: str
    content:str
    published: bool = True

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='isaac', password='QQ', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Connected to db")
        break
    except Exception as error:
        print("Connection failed")
        print("Error:", error)
        time.sleep(2)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id":1},
            {"title": "favorite foods", "content": "I like chile relleno", "id":2}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] ==id:
            return i

app.include_router(post.router)
app.include_router(user.router)
@app.get('/')
def root():
    return {"message": "Hello World"}


