from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class ProductSpecs(Base):
    __tablename__ = 'product_specs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cpecifications_id = Column(Integer, ForeignKey('specifications.id'))
    value = Column(String)

    def __repr__(self):
        return f'<ProductSpecs(cpecifications_id={self.cpecifications_id})>'



