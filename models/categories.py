from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    parent_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    description = Column(Text, nullable=True)
    image = Column(String(255), nullable=True) 
    parent = relationship("Category", remote_side=[id], backref="children")

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"
