import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"mensagem": "Aprendendo FastAPI!"}


@app.get("/help")
async def help():
    return {"ajuda": "Entendendo o funcionamento de FastAPI"}
