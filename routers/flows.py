from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils.edmonds_karp import EdmondsKarp
from utils.ford_fulkerson import FordFulkerson

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
