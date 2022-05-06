from datetime import datetime
from pydantic import BaseModel, validator
from fastapi import HTTPException, status


class fornecedorOut(BaseModel):
    id: int
    name: str
    style: str
    distance: int
    limit: int
    payment: int
    rate: int
    date: datetime


class fornecedorIn(BaseModel):
    name: str
    style: str
    distance: int
    limit: int
    payment: int

    @validator("limit", "distance", "payment")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise HTTPException(
                detail=f"{field.name} must be between 1 and 10",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return v
