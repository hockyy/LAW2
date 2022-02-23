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
    '''
    Latihan pertama, menentukan a pangkat b dengan kedua parameter ialah bilangan bulat
    '''
    return {"result":a**b}

def generate_password(username: str):
    '''
    Mencari password dari sebuah username
    :param username: username yang ingin dicari
    :return: password dari username tersebut
    '''
    return username[::-1]

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    '''
    Latihan kedua, fungsi login yang akan mengauthorize jika dan hanya jika username[::-1] = password
    '''
    return {"authorized": generate_password(username) == password}

@app.post("/modulo")
async def read_modulo(mathQuery: MathQuery):
    '''
    Melakukan modulo untuk bilangan pertama dan kedua, format masukan berupa sebuah payload dengan parameter a dan b sebagai kedua bilangan bulat
    '''
    try:
        return {"query": mathQuery, "result": mathQuery.a%mathQuery.b}
    except Exception as e:
        return {"query": mathQuery, "error": str(e)}

