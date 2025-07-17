from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..model import Blog as model_blog
from ..schemas import Blog 


def get_all(db: Session):
    blogs=db.query(model_blog).all()
    return blogs

def create(request: Blog,db: Session):
    new_blog=model_blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destory(id: int,db: Session):
    blog=db.query(model_blog).filter(model_blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not availabe")
    blog.delete(synchronize_session=False)
    db.commit()
    return "deleted successfully"

def get_blog(id: int,db: Session):
    blog = db.query(model_blog).filter(model_blog.id == id).first() #.options(joinedload(model_blog.creator))
    if not blog:
         # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"details":f"Blog with id {id} not availabe"}
        # or 
        raise HTTPException(status_code=404, detail=f"Blog with id {id} not available")
    return blog

def update(id,db,request):
    blog=db.query(model_blog).filter(model_blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not availabe")
    blog.update(request.dict())
    db.commit()
    return "updated successfully"