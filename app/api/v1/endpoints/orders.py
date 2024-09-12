from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.orders import Orders
from app.models.order_details import OrderDetails
from app.models.product import Product
from app.schemas.response_base.response_base import ResponseBase
from pydantic import BaseModel
from typing import List
from datetime import datetime

router = APIRouter()

class OrderItem(BaseModel):
    sku: str
    quantity: int

class CreateOrderRequest(BaseModel):
    customer_id: int
    items: List[OrderItem]

@router.post("/", response_model=ResponseBase, description="创建新订单")
async def create_order(order: CreateOrderRequest, db: Session = Depends(get_db)):
    # create order
    new_order = Orders(customer_id=order.customer_id, order_date=datetime.now())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    total_amount = 0
    for item in order.items:
        product = db.query(Product).filter(Product.sku == item.sku).first()
        if product is None:
            raise HTTPException(status_code=400, detail="the product does not exit.")
        order_detail = OrderDetails(order_id=new_order.order_id, sku=item.sku, quantity=item.quantity, original_price=product.price, total=product.price * item.quantity)
        db.add(order_detail)
        total_amount += order_detail.total

    new_order.total_amount = total_amount
    db.commit()

    return ResponseBase(code=200, message="success", data={"order_id": new_order.order_id})

