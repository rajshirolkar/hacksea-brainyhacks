from email import message
from re import S
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello():
    return {'Hello Hacksea'}


# https://calendly.com/rajshirolkar/30min

@app.get('/book-session')
async def book_session():
    session = {
        'link': 'https://calendly.com/rajshirolkar/30min',
        'counsellor name': 'Raj Shirolkar',
        'Session Type': 'Video Counselling'
    }
    return session


@app.get('/login')
async def login(username: str, password: str):
    return { 
        message: 'Success',
        username: username,
        password: password
        }