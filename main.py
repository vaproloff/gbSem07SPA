import os.path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open('static/index.html', "r") as f:
        return f.read()


@app.get("/{page}", response_class=HTMLResponse)
async def get_page():
    return await read_root()


@app.get("/get-content/{page}", response_class=HTMLResponse)
async def get_content(page: str):
    if os.path.exists(f'templates/{page}.html'):
        with open(f'templates/{page}.html', 'r', encoding='UTF-8') as f:
            return f.read()

    with open(f'templates/404.html', 'r', encoding='UTF-8') as f:
        return f.read()


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
