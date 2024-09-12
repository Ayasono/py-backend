from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from app.db.session import Base

class OrderDetails(Base):
    __tablename__ = 'order_details'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(String, ForeignKey('orders.order_id'), nullable=False)
    sku = Column(String(50), nullable=False)
    quantity = Column(Integer, nullable=False)
    original_price = Column(DECIMAL(10, 2), nullable=False)
    total = Column(DECIMAL(10, 2), nullable=False)
