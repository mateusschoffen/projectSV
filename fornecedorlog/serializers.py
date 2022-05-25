from datetime import datetime
#from turtle import distance

from fastapi import HTTPException, status
from pydantic import BaseModel, validator


class fornecedorOut(BaseModel):
    id: int
    name: str
    style: str
    pagamento: int
    image: int
    limite: int
    rate: int
    date: datetime


class fornecedorIn(BaseModel):
    name: str
    style: str
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

class providerOut(BaseModel):
    id: int
    name: str
    distance: int
    pay: int
    status: int
    credit: int
    webstore: int
    date: datetime


class providerIn(BaseModel):
    name: str
    distance: int
    pay: int
    status: int
    credit: int
    webstore: int

    @validator("distance", "pay", "credit")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10000:
            raise HTTPException(
                detail=f"{field.name} must be between 1 and 10000",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return v
