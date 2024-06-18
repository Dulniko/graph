from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils.kmp import KMP

router = APIRouter()
templates = Jinja2Templates(directory="templates")
text = ""


@router.get("/kmp", response_class=HTMLResponse)
async def read_kmp(request: Request):
    return templates.TemplateResponse("kmp.html", {"request": request})


@router.post("/kmp_replace", response_class=HTMLResponse)
async def replace_kmp(
    request: Request,
    text: str = Form(...),
    pattern: str = Form(...),
    replacement: str = Form(...),
):
    if not text or not pattern or not replacement:
        raise HTTPException(
            status_code=400, detail="Text, pattern, and replacement cannot be empty!"
        )

    kmp = KMP(text)
    result = kmp.KMP_search(pattern)
    modified_text = kmp.KMP_replace(pattern, replacement)

    return templates.TemplateResponse(
        "kmp_replace_result.html",
        {
            "request": request,
            "modified_text": modified_text,
            "result": result,
            "text": text,
            "pattern": pattern,
            "replacement": replacement,
        },
    )
