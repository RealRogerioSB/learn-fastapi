import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
# from fastapi.responses import JSONResponse

app = FastAPI()

content_json = {
    "1": ["Python", "Delphi"],
    "2": ["JavaScript", "TypeScript"],
    "3": ["Assembly", "Cobol"],
}

content_html = """
<center>
    <h1>FastAPI Web na <u>Geek University</u></h1>
    <span>Para mais cursos, visite nosso site clicando <a href='https://www.geekuniversity.com.br' target='_blank'>
    aqui</a>.</span>
</center>
"""


@app.get("/")
async def root():
    return HTMLResponse(content=content_html)
    # return JSONResponse(content=content_json)


if __name__ == '__main__':
    uvicorn.run("main:app", port=5000)
