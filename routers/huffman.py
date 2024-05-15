from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from utils.huffman import HuffmanCoding

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/huffman", response_class=HTMLResponse)
async def read_huffman(request: Request):
    return templates.TemplateResponse("huffman.html", {"request": request})


@router.post("/huffman", response_class=HTMLResponse)
async def encode_huffman(request: Request, text: str = Form(...)):
    if not text:
        raise HTTPException(status_code=400, detail="Tekst nie może być pusty!")

    tree = HuffmanCoding(text)
    encoded_text = tree.encode_text()
    decoded_text = tree.decode_text(encoded_text)

    return templates.TemplateResponse(
        "huffman.html",
        {
            "request": request,
            "encoded_text": encoded_text,
            "decoded_text": decoded_text,
            "codes": tree.codes,
        },
    )
