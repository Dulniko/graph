from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List, Dict
from uuid import uuid4
from utils.graham import Graham, Point

import base64
import io


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


@router.get("/points-plot")
async def plot_points():
    if len(points) < 3:
        raise HTTPException(
            status_code=404, detail="Not enough points to plot a convex hull"
        )

    buf = io.BytesIO()
    graham = Graham([Point(point["x"], point["y"]) for point in points])
    hull_points = graham.scan()
    graham.visualize_hull(buf)
    buf.seek(0)

    img_base64 = base64.b64encode(buf.getvalue()).decode("ascii")
    html_content = f"<img src='data:image/png;base64,{img_base64}' alt='Plot of Points' style='max-width: 100%;'>"
    html_content += "<ul>"
    for point in hull_points:
        html_content += f"<li>({point.x}, {point.y})</li>"
    html_content += "</ul>"
    return HTMLResponse(content=html_content)
