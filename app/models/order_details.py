from app.db.session import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class OrderDetails(Base):
    __tablename__ = 'order_details'

    order_id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, ForeignKey('product.sku'))
    quantity = Column(Integer, nullable=False, default=1)
    original_price = Column(Integer, nullable=False)
    discount = Column(Integer, nullable=False, default=0)
    total = Column(Float, nullable=False)
