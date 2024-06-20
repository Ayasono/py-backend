from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.product import Product
from app.db.session import get_db

router = APIRouter()


@router.get("/")
def read_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products


@router.post("/")
def create_product(name: str, db: Session = Depends(get_db)):
    product = Product(name=name)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
