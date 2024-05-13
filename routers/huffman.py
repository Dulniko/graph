from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from utils.huffman import (
    build_huffman_tree,
    assign_codes_to_characters,
    encode_text,
    decode_text,
)

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/huffman", response_class=HTMLResponse)
async def read_huffman(request: Request):
    return templates.TemplateResponse("huffman.html", {"request": request})


@router.post("/huffman", response_class=HTMLResponse)
async def encode_huffman(request: Request, text: str = Form(...)):
    if not text:
        raise HTTPException(status_code=400, detail="Tekst nie może być pusty!")

    root = build_huffman_tree(text)
    codes = assign_codes_to_characters(root)

    encoded_text = encode_text(text, codes)
    decoded_text = decode_text(encoded_text, root)

    return templates.TemplateResponse(
        "huffman.html",
        {
            "request": request,
            "encoded_text": encoded_text,
            "decoded_text": decoded_text,
            "codes": codes,
        },
    )
