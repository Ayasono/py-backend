from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.product import Product
from app.db.session import get_db
from app.schemas.response_base.response_base import ResponseBase

router = APIRouter()


@router.get("/")
async def read_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    products_data = [[product.sku, product.name] for product in products]
    return ResponseBase(code=200, message="ok", data=products_data)


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
