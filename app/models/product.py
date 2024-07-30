from sqlalchemy import Column, String, DECIMAL, Integer, ForeignKey
from app.db.session import Base


class Product(Base):
    __tablename__ = 'products'

    sku = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(DECIMAL(10, 2))
    stock = Column(Integer)
    category = Column(String, ForeignKey('categories.name'))
