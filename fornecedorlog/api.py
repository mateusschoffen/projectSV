from turtle import st
from typing import List, Optional

from fastapi import FastAPI, Response, status, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fornecedorlog.core import get_fornecedors_from_database
from fornecedorlog.database import get_session
from fornecedorlog.models import Fornecedor
from fornecedorlog.serializers import fornecedorIn, fornecedorOut

api = FastAPI(title="fornecedorlog ")

api.mount("/fornecedorlog/static", StaticFiles(directory="fornecedorlog/static"), name="static")

templates = Jinja2Templates(directory="fornecedorlog/templates")

@api.get("/teste")
def teste():
    return {"chave":"valor"}

@api.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

@api.get("/home", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request":request
        })


@api.get("/fornecedors", response_model=List[fornecedorOut])
async def list_fornecedors(style: Optional[str] = None):
    """Lists fornecedors from the database"""
    fornecedors = get_fornecedors_from_database(style)
    return fornecedors


@api.post("/fornecedors", response_model=fornecedorOut)
async def add_fornecedor(fornecedor_in: fornecedorIn, response: Response):
    fornecedor = Fornecedor(**fornecedor_in.dict())
    with get_session() as session:
        session.add(fornecedor)
        session.commit()
        session.refresh(fornecedor)

    response.status_code = status.HTTP_201_CREATED
    return fornecedor
