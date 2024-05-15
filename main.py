from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from routers.points import router as points_router
from routers.huffman import router as huffman_router
from routers.flows import router as flows_router
from routers.kmp import router as kmp_router

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(points_router)
app.include_router(huffman_router)
app.include_router(flows_router)
app.include_router(kmp_router)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("starting_page.html", {"request": request})
