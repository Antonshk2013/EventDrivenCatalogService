from sqlalchemy import Column, Integer, String, Enum as BaseEnum, text
from database import Base
from enum import Enum


class Specifications(Base):
    __tablename__ = 'specifications'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    specific_type = Column(String(15))

    def __repr__(self):
        return f"<Specifications(name='{self.name}')>"
