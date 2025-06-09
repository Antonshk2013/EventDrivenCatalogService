from pydantic import BaseModel
from enum import Enum
from typing import List

class SpecificType(str, Enum):
    text = 'text'
    int = 'int'
    float = 'float'
    bool = 'bool'

class SpecificationCreate(BaseModel):
    name: str
    specific_type: SpecificType


class SpecificationRead(SpecificationCreate):
    id: int

    class Config:
        from_attributes = True


class SpecificationsList(BaseModel):
    data: List[SpecificationRead]
    count: int