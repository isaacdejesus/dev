from .. import models, schemas
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import Optional, List
router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)


@router.get('/', response_model= List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@router.post('/', status_code=status.HTTP_201_CREATED, response_model = schemas.Post)#send 201 status code on creating of post
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    #new_post = models.Post(title=post.title, content=post.content, published=post.published)
    #unpacks dict into correct format needed to add data to db
    new_post = models.Post(**post.dict())#does the same as above
    db.add(new_post)
    db.commit()
    db.refresh(new_post)#does what returning * does in postgre
    return new_post

@router.get('/{id}', response_model = schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)): #cast parameter to int
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    return  post
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    posts = db.query(models.Post).filter(models.Post.id == id)
    if posts.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    posts.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    #no data returned due to being 204 error 


@router.put('/{id}', response_model = schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()


