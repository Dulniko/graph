from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException
from utils.guards import Guard
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
