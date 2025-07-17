from typing import List
from pydantic import BaseModel

class BlogBase(BaseModel):
    title:str
    body:str
    class Config():
         orm_mode=True

class Blog(BlogBase):
    class Config():
        orm_mode=True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    # password:str
    blogs:List[Blog] = []
    class Config():
        orm_mode=True
class ShowBlog(BaseModel):
    title:str
    body:str
    creator:ShowUser
    class Config():
        orm_mode=True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None

# from pydantic import BaseModel
# from typing import List

# class BlogBase(BaseModel):
#     title: str
#     body: str

# class Blog(BlogBase):
#     class Config:
#         orm_mode = True

# class ShowBlog(BlogBase):
#     class Config:
#         orm_mode = True

# class User(BaseModel):
#     name: str
#     email: str
#     password: str

# class ShowUser(BaseModel):
#     name: str
#     email: str
#     blog: List[ShowBlog] = []

#     class Config:
#         orm_mode = True
