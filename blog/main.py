from fastapi import FastAPI # Depends, status, Response, HTTPException, APIRouter
from .database import engine,Base
from .routers import blog,user,authentication


# from sqlalchemy.orm import Session
# from typing import List
# from .hashing import Hash
# from sqlalchemy.orm import joinedload
# from .schemas import Blog, ShowBlog, User, ShowUser
# from .model import Blog as model_blog, Users

app=FastAPI()

Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
# def get_db():
#     db=sessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



# @app.post("/user",tags=['user'])
# def create_user(request:User, db: Session = Depends(get_db)):
#     new_user=Users(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}',tags=['user'],response_model=ShowUser)
# def get_user_debug(id, db: Session=Depends(get_db)):
#     user = db.query(Users).filter(Users.id==id).first()
#     if not user:
#         return {"error": "User not found"}
#     return user