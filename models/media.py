from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    media_type = Column(String, nullable=False)
    url = Column(String, nullable=False)
    sequence = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<Media(product_id={self.product_id}, media_type={self.media_type}, url={self.url}, sequence={self.sequence})>'
