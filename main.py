from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "APP no ar"