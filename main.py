from typing import Optional

from fastapi import FastAPI, Form

from model import MathQuery

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/power/{a}/{b}")
async def read_power(a: int, b: int):
    return {"result":a**b}

@app.post("/modulo")
async def read_modulo(mathQuery: MathQuery):
    try:
        return {"query": mathQuery, "result": mathQuery.a%mathQuery.b}
    except Exception as e:
        return {"query": mathQuery, "error": str(e)}


def generate_password(username: str):
    return username[::-1]

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"authorized": generate_password(username) == password}