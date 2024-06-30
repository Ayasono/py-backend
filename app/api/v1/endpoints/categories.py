from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.categories import Categories
from app.db.session import get_db
from app.schemas.response_base.response_base import ResponseBase
from pydantic import BaseModel

router = APIRouter()


@router.get("/")
async def read_categories(db: Session = Depends(get_db)):
    categories = db.query(Categories).all()
    categories_data = [
        {
            "id": category.id,
            "name": category.name,
            "description": category.description
        }
        for category in categories
    ]
    return ResponseBase(code=200, message="ok", data=categories_data)


class Category(BaseModel):
    name: str
    description: str


@router.post("/")
async def create_category(category: Category, db: Session = Depends(get_db)):
    # check if category already exists
    category_exists = db.query(Categories).filter(Categories.name == category.name).first()
    if category_exists:
        return ResponseBase(code=400, message=f"{category.name} already exists", data=None)
    category = Categories(name=category.name, description=category.description)
    db.add(category)
    db.commit()
    db.refresh(category)
    return ResponseBase(code=201, message=f"{category} created")
