from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from ..schemas import Login
from ..database import get_db
from sqlalchemy.orm import Session
from ..model import Users
from ..hashing import Hash
from ..token import create_access_token

router=APIRouter(
     tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db: Session = Depends(get_db)):
    user=db.query(Users).filter(Users.email==request.username).first()

    if not user:
         raise HTTPException(status_code=404, detail=f"Invalid Credentials")
    
    if not Hash.verify(user.password,request.password):
         raise HTTPException(status_code=404, detail=f"Incorrect Password")
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}