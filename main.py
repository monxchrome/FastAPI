from typing import List

from fastapi import FastAPI, Query, Body
from schemas import Post, User, PostOut

app = FastAPI()

# post url

@app.get('/')
def home():
    return {"key": "hi"}


@app.get('/{pk}')
def get_item(pk: int, q: str = None):
    return  {
        "key": pk, 
        "q": q
    }


@app.get('/post/{pk}/item/{item}/')
def get_post_item(pk: int, item: str):
    return{"post": pk, "item": item}


@app.post('/post', response_model=Post, response_model_exclude_unset=True)
def create_post(item: Post, author: User, quantity: int=Body(...)):
    return {"item": item, "author": user, "quantity": quantity}


@app.get('/post')
def get_post(q: List[str] = Query(["test", "test2"], description="searchpost")):
    return q


@app.get('/post/{pk}')
def get_single_post(pk: int):
    return {"pk": pk}

# user url

@app.post('/user', response_model=User, response_model_exclude_unset=True, response_model_exclude={"date"})
def create_user(author: User = Body(..., embed=True)):
    return {"author": user}
