from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    sku: str
    category_id: int
    brand_id: int
    rate: float
    is_active: bool


class ProductRead(ProductCreate):
    id: int

    class Config:
        from_attributes = True

class ProductReadFuell(BaseModel):
    pass
