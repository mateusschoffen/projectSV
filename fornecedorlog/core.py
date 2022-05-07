from typing import List, Optional

from sqlmodel import select

from fornecedorlog.database import get_session
from fornecedorlog.models import fornecedor


def add_fornecedor_to_database(
    name: str,
    style: str,
    pagamento: int,
    image: int,
    limite: int,
) -> bool:
    with get_session() as session:
        fornecedor = fornecedor(**locals())
        session.add(fornecedor)
        session.commit()

    return True


def get_fornecedors_from_database(style: Optional[str] = None) -> List[fornecedor]:
    with get_session() as session:
        sql = select(fornecedor)
        if style:
            sql = sql.where(fornecedor.style == style)
        return list(session.exec(sql))
