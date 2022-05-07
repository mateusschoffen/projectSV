from datetime import datetime

from fastapi import HTTPException, status
from pydantic import BaseModel, validator


class fornecedorOut(BaseModel):
    id: int
    name: str
    cidade: str
    pagamento: int
    image: int
    limite: int
    rate: int
    date: datetime


class fornecedorIn(BaseModel):
    name: str
    cidade: str
    pagamento: int
    image: int
    limite: int

    @validator("image", "pagamento", "limite")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise HTTPException(
                detail=f"{field.name} must be between 1 and 10",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return v
