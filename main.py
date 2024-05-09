from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List, Dict

app = FastAPI()
templates = Jinja2Templates(directory="templates")

points: List[Dict[str, int]] = []


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/points", response_class=HTMLResponse)
async def get_points_list(request: Request):
    return templates.TemplateResponse(
        "points_list.html", {"request": request, "points": points}
    )


@app.post("/points", response_class=HTMLResponse)
async def add_point(request: Request, x: int = Form(...), y: int = Form(...)):
    points.append({"x": x, "y": y})
    return templates.TemplateResponse(
        "points_list.html", {"request": request, "points": points}
    )
