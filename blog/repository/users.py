from fastapi import HTTPException, status
from ..schemas import User
from ..model import  Users
from ..hashing import Hash
from sqlalchemy.orm import Session

def create_user(request:User,db:Session):
    new_user=Users(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id,db:Session):
    user = db.query(Users).filter(Users.id==id).first()
    if not user:
         raise HTTPException(status_code=404, detail=f"User with id {id} not available")
    return user