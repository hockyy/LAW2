from typing import Optional

from fastapi import FastAPI, Form

from model import MathQuery, MessageResponse, ValueResponse, MathResponse

app = FastAPI()


@app.get("/", response_model=MessageResponse)
async def read_root():
    res = MessageResponse("Hello World", 200)
    print("HELLO")
    return res

@app.get("/power/{a}/{b}", response_model=ValueResponse)
async def read_power(a: int, b: int):
    '''
    Latihan pertama, menentukan a pangkat b dengan kedua parameter ialah bilangan bulat
    '''
    return ValueResponse(a**b, 200)

def generate_password(username: str):
    '''
    Mencari password dari sebuah username
    :param username: username yang ingin dicari
    :return: password dari username tersebut
    '''
    return username[::-1]

@app.post("/login", response_model=MessageResponse)
async def login(username: str = Form(...), password: str = Form(...)):
    '''
    Latihan kedua, fungsi login yang akan mengauthorize jika dan hanya jika username[::-1] = password
    '''
    return MessageResponse("True" if generate_password(username) == password else "False", 200)

@app.post("/modulo", response_model=MathResponse)
async def read_modulo(mathQuery: MathQuery):
    '''
    Melakukan modulo untuk bilangan pertama dan kedua, format masukan berupa sebuah payload dengan parameter a dan b sebagai kedua bilangan bulat
    '''
    try:
        return MathResponse(mathQuery, mathQuery.a%mathQuery.b, None)
    except Exception as e:
        return MathResponse(mathQuery, mathQuery.a%mathQuery.b, str(e))

