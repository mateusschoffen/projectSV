from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import validator
from statistics import mean
from datetime import datetime


class fornecedor(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    distance: int
    limit: int
    payment: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

    @validator("distance", "limit", "payment")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v

    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean([values["distance"], values["limit"], values["payment"]])
        return int(rate)


brewdog = fornecedor(name="Brewdog", style="NEIPA", distance=5, limit=8, payment=8)
