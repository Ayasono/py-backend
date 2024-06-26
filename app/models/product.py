from sqlalchemy import Column, String
from app.db.session import Base


class Product(Base):
    __tablename__ = 'products'
    sku = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)

    class Config:
        orm_mode = True
