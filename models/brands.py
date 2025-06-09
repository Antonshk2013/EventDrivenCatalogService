from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    logo = Column(String(255))
    description = Column(String(2000))
    products = relationship("Product", back_populates="brand")

    def __repr__(self):
        return f'<Brands(id={self.id}, name={self.name})>'