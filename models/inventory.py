from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    count = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<Inventory {self.id}>'
