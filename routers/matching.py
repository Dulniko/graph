from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from utils.matching import Graph
from typing import List


graph: Graph = None
max_front: int = 0
max_back: int = 0
tmp_list: List[tuple[int, int]] = []

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/matching", response_class=HTMLResponse)
async def read_matching(request: Request):
    tmp_list.clear()
    return templates.TemplateResponse("matching.html", {"request": request})


@router.get("/graph", response_class=HTMLResponse)
async def get_graph_edge(request: Request):
    return templates.TemplateResponse(
        "graph.html", {"request": request, "graph": graph}
    )


@router.post("/matching", response_class=HTMLResponse)
async def add_graph(
    request: Request, num_front: int = Form(...), num_back: int = Form(...)
):
    if num_front < 0 or num_back < 0:
        raise HTTPException(status_code=400, detail="Number must be non-negative")
    global graph, max_front, max_back
    max_front, max_back = num_front, num_back
    graph = Graph(num_front, num_back)
    tmp_list.clear()
    return templates.TemplateResponse(
        "graph.html", {"request": request, "graph": graph}
    )


@router.get("/edge", response_class=HTMLResponse)
async def get_edge_list(request: Request):
    return templates.TemplateResponse(
        "edge_list.html", {"request": request, "graph": graph, "tmp_list": tmp_list}
    )


@router.post("/edge", response_class=HTMLResponse)
async def add_edge(request: Request, front: int = Form(...), back: int = Form(...)):
    front -= 1
    back -= 1
    if front < 0 or front > max_front or back < 0 or back > max_back:
        raise HTTPException(
            status_code=400,
            detail="Number must be positive and within range of ziomale",
        )
    tmp_list.append((front + 1, back + 1))
    graph.add_edge(front, back)
    return templates.TemplateResponse(
        "edge_list.html", {"request": request, "graph": graph, "tmp_list": tmp_list}
    )


@router.get("/matching-result", response_class=HTMLResponse)
async def matching_result(request: Request):
    return templates.TemplateResponse(
        "edge_list.html",
        {
            "request": request,
            "graph": graph,
            "tmp_list": tmp_list,
            "result": graph.max_matching(),
        },
    )
