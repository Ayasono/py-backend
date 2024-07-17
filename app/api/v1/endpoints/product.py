from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.product import Product
from app.db.session import get_db
from app.schemas.response_base.response_base import ResponseBase
from typing import List, Union
from pydantic import BaseModel

router = APIRouter()


class ProductResponse(BaseModel):
    name: str
    description: str
    stock: int
    price: float
    sku: str
    category: str

    class Config:
        from_attributes = True


class ProductListResponse(ResponseBase):
    data: Union[List[ProductResponse], None]


@router.get("/", response_model=ProductListResponse, description="Get all products")
async def read_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return {
        "code": 200,
        "message": "ok",
        "data": products
    }


@router.get("/item/{sku}")
async def read_product(sku: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.sku == sku).first()
    if not product:
        return ResponseBase(code=404, message="Product not found", data=None)
    return ResponseBase(code=200, message="ok", data=product.name)


@router.post("/")
async def create_product(name: str, db: Session = Depends(get_db)):
    product = Product(name=name)
    db.add(product)
    db.commit()
    db.refresh(product)
    return ResponseBase(code=201, message=f"{product} created")
