from typing import List, Optional

from fastapi import FastAPI, Response, status

from fornecedorlog.core import get_fornecedors_from_database
from fornecedorlog.database import get_session
from fornecedorlog.models import Fornecedor
from fornecedorlog.serializers import fornecedorIn, fornecedorOut

api = FastAPI(title="fornecedorlog ")


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
