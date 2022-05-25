from datetime import datetime
from statistics import mean  # NEW
from typing import Optional

from pydantic import validator  # NEW
from sqlmodel import Field, SQLModel


class Fornecedor(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    pagamento: int
    image: int
    limite: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

    # NEW
    @validator("image", "pagamento", "limite")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v

    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean([values["pagamento"], values["image"], values["limite"]])
        return int(rate)

##Nova Tabela
class Provider(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    distance: int
    pay: int
    status: int
    credit: int
    webstore: int
    date: datetime = Field(default_factory=datetime.now)

    # NEW
    @validator("distance", "pay", "credit")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10000:
            raise RuntimeError(f"{field.name} must be between 1 and 10000")
        return v

