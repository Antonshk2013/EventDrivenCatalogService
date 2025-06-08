from pydantic import BaseModel, Field
from typing import Optional, List

class BrandCreate(BaseModel):
    name: str
    logo: Optional[str] = None
    description: Optional[str] = None


class BrandRead(BrandCreate):
    id: int

    class Config:
        from_attributes = True


class BrandsList(BaseModel):
    data: List[BrandRead]
    count: int