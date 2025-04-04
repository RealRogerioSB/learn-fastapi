from typing import Dict

import uvicorn
from fastapi import FastAPI
from app.routers import routers_produtos, routers_usuarios

MENSAGEM_HOME: str = "Bem-vindo à API de Recomendação de Produtos"

app = FastAPI()

app.include_router(routers_usuarios.router)
app.include_router(routers_produtos.router)


@app.get("/")
def home() -> Dict[str, str]:  # Iniciando o servidor
    global MENSAGEM_HOME
    return {"mensagem": MENSAGEM_HOME}


if __name__ == "__main__":
    uvicorn.run(app, port=5000)
