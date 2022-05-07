from typing import List, Optional

from sqlmodel import select

from fornecedorlog.database import get_session
from fornecedorlog.models import fornecedor


def add_fornecedor_to_database(
    name: str,
    cidade: str,
    pagamento: int,
    image: int,
    limite: int,
) -> bool:
    with get_session() as session:
        fornecedor = fornecedor(**locals())
        session.add(fornecedor)
        session.commit()

    return True


def get_fornecedors_from_database(cidade: Optional[str] = None) -> List[fornecedor]:
    with get_session() as session:
        sql = select(fornecedor)
        if cidade:
            sql = sql.where(fornecedor.cidade == cidade)
        return list(session.exec(sql))
