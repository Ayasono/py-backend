from sqlalchemy import Column, String, Integer, ForeignKey, DECIMAL, DateTime
import uuid

from sqlalchemy.orm import relationship

from app.db.session import Base


class Orders(Base):
    __tablename__ = 'orders'

    order_id = Column(String, primary_key=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()))
    customer_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    order_date = Column(DateTime, nullable=False)
    ship_date = Column(DateTime)
    ship_carrier = Column(String(50))
    shipping_cost = Column(DECIMAL(10, 2), nullable=False, default=0.00)
    total_amount = Column(DECIMAL(10, 2), nullable=False, default=0.00)

    order_details = relationship("OrderDetails", back_populates="order")
