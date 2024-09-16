from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime
from app.schemas.response_base.response_base import ResponseBase

class OrderItem(BaseModel):
    sku: str
    quantity: int


class CreateOrderRequest(BaseModel):
    customer_id: int
    items: List[OrderItem]


class OrderDetailBase(BaseModel):
    order_id: str
    sku: str
    quantity: int
    original_price: float
    total: float

    model_config = ConfigDict(from_attributes=True)


class OrderBase(BaseModel):
    order_id: str
    customer_id: int
    order_date: datetime
    ship_date: Optional[datetime]
    ship_carrier: Optional[str]
    shipping_cost: float
    total_amount: float
    order_details: List[OrderDetailBase] = []

    model_config = ConfigDict(from_attributes=True)


class OrderResponse(ResponseBase):
    data: List[OrderBase]


class CreateOrderResponse(ResponseBase):
    data: OrderBase