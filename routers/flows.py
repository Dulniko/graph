from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils.edmonds_karp import EdmondsKarp
from utils.ford_fulkerson import FordFulkerson

import base64
import io


router = APIRouter()
templates = Jinja2Templates(directory="templates")


class Algorithm:
    edmonds_karp = "edmonds_karp"
    ford_fulkerson = "ford_fulkerson"


@router.get("/flows", response_class=HTMLResponse)
async def read_flow(request: Request):
    return templates.TemplateResponse("flows.html", {"request": request})


@router.post("/flows", response_class=HTMLResponse)
async def calculate_flow(
    request: Request,
    graph: str = Form(...),
    source: int = Form(...),
    sink: int = Form(...),
    algorithm: str = Form(...),
):
    if not graph or source is None or sink is None:
        raise HTTPException(
            status_code=400, detail="Graph, source, and sink cannot be empty!"
        )

    try:
        graph = eval(graph)  # Convert string representation of list to list
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid graph format!")

    if algorithm == "edmonds_karp":
        ek = EdmondsKarp(graph)
        flow = ek.edmonds_karp(source, sink)
    elif algorithm == "ford_fulkerson":
        ff = FordFulkerson(graph)
        flow = ff.ford_fulkerson(source, sink)
    else:
        raise HTTPException(status_code=400, detail="Invalid algorithm selected!")

    return templates.TemplateResponse(
        "flow_result.html", {"request": request, "flow": flow, "algorithm": algorithm}
    )


# TODO: Visualize the flow in the graph, asynchronusly graph additon

@router.get("/graph-plot", response_class=HTMLResponse)
async def plot_graph(
    graph: str = Form(...)
):
    try:
        graph = eval(graph) 
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid graph format!")

    buf = io.BytesIO()
    ek = EdmondsKarp(graph)
    ek.graph_visualize(buf)
    buf.seek(0)

    img_base64 = base64.b64encode(buf.getvalue()).decode("ascii")
    html_content = f"<img src='data:image/png;base64,{img_base64}' alt='Graph Image' style='max-width: 100%;'>"
    
    return HTMLResponse(content=html_content)