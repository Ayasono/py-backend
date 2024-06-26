from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.product import Product
from app.db.session import get_db
from app.schemas.response_base.response_base import ResponseBase

router = APIRouter()


@router.get("/")
def read_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    products_data = [[product.sku, product.name] for product in products]
    return ResponseBase(code=200, message="ok", data=products_data)


@router.post("/")
def create_product(name: str, db: Session = Depends(get_db)):
    product = Product(name=name)
    db.add(product)
    db.commit()
    db.refresh(product)
    return ResponseBase(code=201, message=f"{product} created")