from typing import List

from pydantic import BaseModel, validator, Field
from datetime import date


class Annot(BaseModel):
    annot: str

class User(BaseModel):
    f_name: str
    l_name: str
    annotation: list[Annot]
    date: date
    age: int

# validador for User
    
    @validator('age')
    def check_age(cls, v):
        if v < 16:
            raise ValueError('User age must be more then 16')
        return v


class Post(BaseModel):
    title: str = Field(..., max_length=20, min_length=3)
    author: str
    duaration: str
    date: date
    pages: int


class PostOut(Post):
    id: int = 1
