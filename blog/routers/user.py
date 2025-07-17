from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from ..database import engine,Base,sessionLocal, get_db
from ..schemas import User, ShowUser #Blog, ShowBlog, 
from ..model import  Users #Blog as model_blog,
from sqlalchemy.orm import Session
from ..repository import users

router=APIRouter(
    prefix="/user",
    tags=['user']
)



@router.post("/")
def create_user(request:User, db: Session = Depends(get_db)):
    return users.create_user(request,db)

@router.get('/{id}',response_model=ShowUser)
def get_user(id, db: Session=Depends(get_db)):
    return users.get_user(id,db)