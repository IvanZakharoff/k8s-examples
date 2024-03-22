import socket
import os

from fastapi import FastAPI
from sqlalchemy import create_engine

SQLALCHEMY_URL =  f'postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}'

engine = create_engine(SQLALCHEMY_URL)

app = FastAPI() 


@app.get("/")
def read_root():
    return f'hostname v1: {socket.gethostname()}'


@app.post('/db')
def create_db():
    from db import Base

    Base.metadata.create_all(engine)


@app.get('/sqlalchemy_url')
def create_db():
    return SQLALCHEMY_URL
