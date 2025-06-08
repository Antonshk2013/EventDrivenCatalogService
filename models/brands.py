from sqlalchemy import Column, Integer, String
from database import Base


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    logo = Column(String(255))
    description = Column(String(2000))

    def __repr__(self):
        return f'<Brands(id={self.id}, name={self.name})>'