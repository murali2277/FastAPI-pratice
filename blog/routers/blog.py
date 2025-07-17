from fastapi import FastAPI, Depends, status, Response, APIRouter
from ..database import sessionLocal, get_db
from ..schemas import Blog, ShowBlog # User, ShowUser
from ..model import Blog as model_blog, Users
from typing import List
from sqlalchemy.orm import Session
from ..repository import blogs
from .. oauth2 import get_current_user

router=APIRouter(
    prefix="/blog",
    tags=["blog"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request: Blog,db: Session = Depends(get_db),current_user:Users=Depends(get_current_user)):
    return blogs.create(request,db)
     
@router.get("/", response_model=List[ShowBlog])
def all(db: Session = Depends(get_db),current_user:Users=Depends(get_current_user)):
    return blogs.get_all(db)

# from sqlalchemy.orm import joinedload

@router.get("/{id}", response_model=ShowBlog, tags=['blog'])
def get_blog(id: int, db: Session = Depends(get_db),current_user:Users=Depends(get_current_user)):
    return blogs.get_blog(id,db)

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db),current_user:Users=Depends(get_current_user)):
    return blogs.destory(id,db)

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id, request: Blog, db: Session = Depends(get_db),current_user:Users=Depends(get_current_user)):
    return blogs.update(id,db,request)