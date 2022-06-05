from typing import List, Optional

from sqlmodel import select

from fornecedorlog.database import get_session
from fornecedorlog.models import Fornecedor, Provider


def add_fornecedor_to_database(
    name: str,
    style: str,
    pagamento: int,
    image: int,
    limite: int,
) -> bool:
    with get_session() as session:
        fornecedor = Fornecedor(**locals())
        session.add(fornecedor)
        session.commit()

    return True


def get_fornecedors_from_database(style: Optional[str] = None) -> List[Fornecedor]:
    with get_session() as session:
        sql = select(Fornecedor)
        if style:
            sql = sql.where(Fornecedor.style == style)
        return list(session.exec(sql))

def add_provider_to_database(
    name: str,
    distance: int,
    pay: int,
    status: int,
    credit: int,
    webstore: int,
) -> bool:
    with get_session() as session:
        provider = Provider(**locals())
        session.add(provider)
        session.commit()

    return True

def get_providers_from_database(style: Optional[str] = None) -> List[Provider]:
    with get_session() as session:
        sql = select(Provider)
        if style:
            sql = sql.where(Provider.style == style)
        return list(session.exec(sql))

def get_providersall():
    with get_session() as session:
        sql = select(Provider)
    return list(session.exec(sql))