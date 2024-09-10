from app.db.session import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Date, DECIMAL


class Orders(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('users.customer_id'), nullable=False)
    order_date = Column(Date, nullable=False)
    ship_date = Column(Date)
    ship_carrier = Column(String(50))
    shipping_cost = Column(DECIMAL(10, 2), nullable=False, default=0.00)
    quantity = Column(Integer, nullable=False, default=1)
