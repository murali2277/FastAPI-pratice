from fastapi import FastAPI, Depends, status, Response, HTTPException
from .schemas import Blog, ShowBlog, User 
from .model import Blog as model_blog, Users
from .database import engine,Base,sessionLocal
from sqlalchemy.orm import Session
from typing import List
from .hashing import Hash

app=FastAPI()

Base.metadata.create_all(engine)

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog",status_code=status.HTTP_201_CREATED)
def create(request: Blog,db: Session = Depends(get_db)):
    new_blog=model_blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 

@app.get("/blog", response_model=List[ShowBlog])
def all(db: Session = Depends(get_db)):
    blogs=db.query(model_blog).all()
    return blogs

@app.get("/blog/{id}", status_code=200, response_model=ShowBlog)
def show(id, response: Response, db: Session = Depends(get_db)):
    blogs=db.query(model_blog).filter(model_blog.id==id).first()
    if not blogs:
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"details":f"Blog with id {id} not availabe"}

        # or 

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not availabe")

    return blogs

@app.delete("/blog/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    blog=db.query(model_blog).filter(model_blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not availabe")
    blog.delete(synchronize_session=False)
    db.commit()
    return "deleted successfully"

@app.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id, request: Blog, db: Session = Depends(get_db)):
    blog=db.query(model_blog).filter(model_blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not availabe")
    blog.update(request,dict())
    db.commit()
    return "updated successfully"

@app.post("/user")
def create_user(request:User, db: Session = Depends(get_db)):
    new_user=Users(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    return new_user
