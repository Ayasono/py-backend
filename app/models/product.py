from sqlalchemy import Column, Integer, String
from app.db.session import Base


class Product(Base):
    __tablename__ = 'products'
    sku = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
