from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(155), nullable=False)
    description = Column(String(1000), nullable=False)
    price = Column(Float, nullable=False)
    sku = Column(String(155), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    brand_id = Column(Integer, ForeignKey('brands.id'))
    rate = Column(Float, nullable=False)
    is_active = Column(Boolean, nullable=False)
    category = relationship("Category", back_populates="products")
    brand = relationship("Brand", back_populates="products")

    def __repr__(self):
        return f'<Products(id={self.id}, name={self.name}, description={self.description})>'
