from sqlalchemy import Column, String, Integer, ForeignKey, Date, DECIMAL
import uuid
from app.db.session import Base

class Orders(Base):
    __tablename__ = 'orders'

    order_id = Column(String, primary_key=True, index=True, nullable=False, default=lambda: str(uuid.uuid4()))
    customer_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    order_date = Column(Date, nullable=False)
    ship_date = Column(Date)
    ship_carrier = Column(String(50))
    shipping_cost = Column(DECIMAL(10, 2), nullable=False, default=0.00)
    total_amount = Column(DECIMAL(10, 2), nullable=False, default=0.00)
