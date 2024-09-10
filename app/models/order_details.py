from app.db.session import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class OrderDetails(Base):
    __tablename__ = 'order_details'

    order_id = Column(Integer, ForeignKey('orders.order_id'), index=True)
    sku = Column(String, ForeignKey('product.sku'), index=True)
    quantity = Column(Integer, nullable=False, default=1)
    original_price = Column(Float, nullable=False)
    discount_percentage = Column(Float, nullable=False, default=0)
    discount_amount = Column(Float, nullable=False, default=0)
    total = Column(Float, nullable=False)
