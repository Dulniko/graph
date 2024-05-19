from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException
from utils.guards import Guard, SegmentTree, Point, Stop, patrol_route
from utils.graham import Graham
from routers.points import points
from typing import List
from uuid import uuid4

router = APIRouter()
templates = Jinja2Templates(directory="templates")

guards: List[Guard] = []


@router.get("/guards", response_class=HTMLResponse)
async def read_guards(request: Request):
    return templates.TemplateResponse("guards.html", {"request": request})


@router.get("/guards-list", response_class=HTMLResponse)
async def get_guards_list(request: Request):
    return templates.TemplateResponse(
        "guards_list.html", {"request": request, "guards": guards}
    )


@router.post("/guards", response_class=HTMLResponse)
async def add_guard(request: Request, energy: int = Form(...)):
    if energy < 0:
        raise HTTPException(status_code=400, detail="Energy must be a positive integer")
    guards.append(Guard(uuid=str(uuid4()), energy=energy))
    return templates.TemplateResponse(
        "guards_list.html", {"request": request, "guards": guards}
    )


@router.delete("/guards/{uuid}", response_class=HTMLResponse)
async def delete_guard(request: Request, uuid: str):
    for guard in guards:
        if guard.uuid == uuid:
            guards.remove(guard)
    return templates.TemplateResponse(
        "guards_list.html", {"request": request, "guards": guards}
    )


@router.delete("/guards", response_class=HTMLResponse)
async def clear_guards(request: Request):
    guards.clear()
    return templates.TemplateResponse(
        "guards_list.html", {"request": request, "guards": guards}
    )


@router.get("/guards-range", response_class=HTMLResponse)
async def get_guard_range(request: Request):
    segment_tree = SegmentTree(guards)
    result = segment_tree.range_query(0, len(guards))
    return templates.TemplateResponse(
        "guards_range.html", {"request": request, "guard": result}
    )


@router.post("/scout", response_class=HTMLResponse)
async def scout(
    request: Request, guard_uuid: str = Form(...), max_steps: int = Form(...)
):
    if len(points) < 3:
        raise HTTPException(
            status_code=404, detail="Not enough points to plot a convex hull"
        )
    guard = next((g for g in guards if g.uuid == guard_uuid), None)
    if not guard:
        raise HTTPException(status_code=404, detail="Guard not found")

    hull = Graham(points).scan()
    stops = patrol_route(hull, max_steps)

    return templates.TemplateResponse(
        "scout_result.html", {"request": request, "stops": stops}
    )
