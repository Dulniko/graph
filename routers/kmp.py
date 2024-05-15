from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils.kmp import KMP  # Import the KMP class

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/kmp", response_class=HTMLResponse)
async def read_kmp(request: Request):
    return templates.TemplateResponse("kmp.html", {"request": request})


@router.post("/kmp_search", response_class=HTMLResponse)
async def search_kmp(request: Request, text: str = Form(...), pattern: str = Form(...)):
    if not text or not pattern:
        raise HTTPException(status_code=400, detail="Text and pattern cannot be empty!")

    kmp = KMP(text)
    result = kmp.KMP_search(pattern)

    return templates.TemplateResponse(
        "kmp_result.html",
        {"request": request, "result": result, "text": text, "pattern": pattern},
    )
