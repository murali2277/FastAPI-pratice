from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn 

app=FastAPI()

@app.get("/blog")
def index(limit=10,published: bool=True,sort:Optional[str]=None):
    # return published
    if published:
        return {"data":f"{limit} published Blog from db"}
    else:
        return {"data":f"{limit} Blog from db"}

@app.get("/show/unpublished")
def show():
    return {"data":"unpublished"}

@app.get("/show/{id}")
def show(id: int):
    return {"data":{"id":id}}
class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post("/blog")
def create_blog(blog:Blog):
    return {"data":f"Blog is created with title as {blog.title}"}

# if __name__=="__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9000)