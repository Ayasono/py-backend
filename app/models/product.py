from sqlalchemy import Column, String, DECIMAL, Integer, ForeignKey
from app.db.session import Base


class Product(Base):
    __tablename__ = 'products'

    sku = Column(String(50), primary_key=True, index=True)
    name = Column(String(100), index=True, nullable=False)
    description = Column(String(255))
    price = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    category = Column(String(50), ForeignKey('categories.name'), nullable=False)
