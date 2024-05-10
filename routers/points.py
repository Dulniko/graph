from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List, Dict
from uuid import uuid4


router = APIRouter()
templates = Jinja2Templates(directory="templates")

points: List[Dict[str, int]] = []


@router.get("/points", response_class=HTMLResponse)
async def read_points(request: Request):
    return templates.TemplateResponse("points.html", {"request": request})


@router.get("/points-list", response_class=HTMLResponse)
async def get_points_list(request: Request):
    return templates.TemplateResponse(
        "points_list.html", {"request": request, "points": points}
    )


@router.post("/points", response_class=HTMLResponse)
async def add_point(request: Request, x: int = Form(...), y: int = Form(...)):
    points.append({"uuid": str(uuid4()), "x": x, "y": y})
    return templates.TemplateResponse(
        "points_list.html", {"request": request, "points": points}
    )


@router.delete("/points/{uuid}", response_class=HTMLResponse)
async def delete_point(request: Request, uuid: str):
    for point in points:
        if point["uuid"] == uuid:
            points.remove(point)
    return templates.TemplateResponse(
        "points_list.html", {"request": request, "points": points}
    )


@router.delete("/points", response_class=HTMLResponse)
async def clear_points(request: Request):
    points.clear()
    return templates.TemplateResponse(
        "points_list.html", {"request": request, "points": points}
    )
