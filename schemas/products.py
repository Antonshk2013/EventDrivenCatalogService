from pydantic import BaseModel
from typing import Optional
from schemas.category import CategoryRead
from schemas.brands import BrandRead

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    sku: str
    category_id: int
    brand_id: int
    rate: float
    is_active: bool


class ProductRead(BaseModel):
    id: int
    name: str
    description: str
    price: float
    sku: str
    category: Optional[CategoryRead]
    brand: Optional[BrandRead]
    rate: float
    is_active: bool

    class Config:
        from_attributes = True

class ProductsList(BaseModel):
    data: list[ProductRead]
    count: int


class ProductFilter(BaseModel):
    name: str | None = None
    category_id: int | None = None