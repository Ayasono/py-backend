from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.orders import Orders
from app.models.order_details import OrderDetails
from app.models.product import Product
from app.schemas.response_base.response_base import ResponseBase
from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

router = APIRouter()


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


# Routes
@router.post("/", response_model=CreateOrderResponse, description="Create a new order")
async def create_order(order: CreateOrderRequest, db: Session = Depends(get_db)):
    new_order = Orders(customer_id=order.customer_id, order_date=datetime.now())
    db.add(new_order)
    db.flush()  # 获取 order_id，但不提交事务

    total_amount = 0
    for item in order.items:
        product = db.query(Product).filter(Product.sku == item.sku).first()
        if product is None:
            raise HTTPException(status_code=400, detail=f"Product {item.sku} does not exist")
        order_detail = OrderDetails(
            order_id=new_order.order_id,
            sku=item.sku,
            quantity=item.quantity,
            original_price=product.price,
            total=product.price * item.quantity
        )
        db.add(order_detail)
        total_amount += order_detail.total

    new_order.total_amount = total_amount
    db.commit()
    db.refresh(new_order)

    return CreateOrderResponse(code=status.HTTP_200_OK, message="Success", data=new_order)


@router.get("/", response_model=OrderResponse, description="Get all orders")
async def read_orders(db: Session = Depends(get_db)):
    orders = db.query(Orders).all()
    return OrderResponse(code=status.HTTP_200_OK, message="Success", data=orders)


@router.get("/{customer_id}", response_model=OrderResponse, description="Get orders items by customer id")
async def read_orders_by_customer_id(customer_id: str, db: Session = Depends(get_db)):
    orders = db.query(Orders).filter(Orders.customer_id == customer_id).all()

    return OrderResponse(code=status.HTTP_200_OK, message="Success", data=orders)
