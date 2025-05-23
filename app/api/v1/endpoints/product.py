from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.models.product import Product
from app.db.session import get_db
from app.schemas.product.product_schema import ProductBase, ProductResponse, ProductListResponse, \
    ProductCreateRequestBody, CreateProductResponse

router = APIRouter()


@router.get("/", response_model=ProductListResponse, description="Get all products")
async def read_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return ProductListResponse(code=status.HTTP_200_OK, message="Products retrieved successfully", data=products)


@router.get("/item/{sku}", response_model=CreateProductResponse, description="Get a product by SKU")
async def read_product(sku: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.sku == sku).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return CreateProductResponse(code=status.HTTP_200_OK, message="Product retrieved successfully", data=product)


@router.post("/", response_model=CreateProductResponse, status_code=status.HTTP_201_CREATED,
             description="Create a new product")
async def create_product(create_product_information: ProductCreateRequestBody, db: Session = Depends(get_db)):
    try:
        product = Product(**create_product_information.model_dump())
        db.add(product)
        db.commit()
        db.refresh(product)
        return CreateProductResponse(code=status.HTTP_201_CREATED,
                                     message=f"Product '{product.name}' created successfully", data=product)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Database integrity error: {str(e.orig)}")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"An unexpected error occurred: {str(e)}")
