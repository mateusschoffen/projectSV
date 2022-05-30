#from turtle import st
from typing import List, Optional
from mangum import Mangum

from fastapi import FastAPI, Response, status, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fornecedorlog.core import add_provider_to_database, get_fornecedors_from_database, get_providers_from_database
from fornecedorlog.database import get_session
from fornecedorlog.models import Fornecedor
from fornecedorlog.serializers import fornecedorIn, fornecedorOut
from fornecedorlog.models import Provider
from fornecedorlog.serializers import providerIn, providerOut

api = FastAPI(
    title="fornecedorlog",
    root_path="/prod/"
    )


api.mount("/prod/fornecedorlog/static", StaticFiles(directory="fornecedorlog/static"), name="static")
templates = Jinja2Templates(directory="fornecedorlog/templates")

@api.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("page_selection.html", {"request": request, "title":"Página de Seleção"})

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

@api.get("/fornecedors", response_class=HTMLResponse, response_model=List[fornecedorOut])
async def list_fornecedors(request: Request, style: Optional[str] = None):
    """Lists fornecedors from the database"""
    fornecedors = get_fornecedors_from_database(style)
    return templates.TemplateResponse("fornecedors_list.html", {"request": request, "fornecedors": fornecedors, "title":"Página de Fornecedors"})


@api.post("/fornecedors", response_model=fornecedorOut)
async def add_fornecedor(fornecedor_in: fornecedorIn, response: Response):
    fornecedor = Fornecedor(**fornecedor_in.dict())
    with get_session() as session:
        session.add(fornecedor)
        session.commit()
        session.refresh(fornecedor)

    response.status_code = status.HTTP_201_CREATED
    return fornecedor

@api.post("/provider", response_model=providerOut)
async def add_provider(provider_in: providerIn, response: Response):
    provider = Provider(**provider_in.dict())
    with get_session() as session:
        session.add(provider)
        session.commit()
        session.refresh(provider)

    response.status_code = status.HTTP_201_CREATED
    return provider

@api.get("/providers", response_class=HTMLResponse, response_model=List[providerOut])
async def list_providers(request: Request, style: Optional[str] = None):
    """Lists providers from the database"""
    providers = get_providers_from_database(style)
    return templates.TemplateResponse("providers_list.html", {"request": request, "providers": providers, "title":"Página de Providers"})


handler = Mangum(api)