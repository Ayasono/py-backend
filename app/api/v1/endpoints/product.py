from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
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

    if not products:
        raise HTTPException(status_code=404, detail="Products not found")

    return {
        "code": 200,
        "message": "ok",
        "data": products
    }


@router.get("/item/{sku}")
async def read_product(sku: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.sku == sku).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return ResponseBase(code=200, message="ok", data=product.name)


class ProductCreateRequestBody(BaseModel):
    name: str
    sku: str
    description: str
    stock: int
    price: float
    category: str


class CreateProductResponse(ResponseBase):
    data: Union[ProductCreateRequestBody, None]


@router.post("/", response_model=CreateProductResponse, description="Create a new product")
async def create_product(create_product_information: ProductCreateRequestBody, db: Session = Depends(get_db)):
    try:
        product = Product(**create_product_information.model_dump())
        db.add(product)
        db.commit()
        db.refresh(product)
        return ResponseBase(code=201, message=f"Product '{product.name}' created", data=product)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"{e.orig}")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"{e}")
