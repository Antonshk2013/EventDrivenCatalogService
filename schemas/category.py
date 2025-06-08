from pydantic import BaseModel, Field
from typing import Optional, List


class CategoryCreate(BaseModel):
    name: str
    description: Optional[str] = None
    parent_id: Optional[int] = Field(default=None)
    image: Optional[str] = None


class CategoryRead(CategoryCreate):
    id: int

    class Config:
        from_attributes = True


class CategoryList(BaseModel):
    data: List[CategoryRead]
    count: int

