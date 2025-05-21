from pydantic import BaseModel, Field, ConfigDict
from typing import List
from app.schemas.response_base.response_base import ResponseBase


class ProductBase(BaseModel):
    name: str = Field(..., example="iPhone 12")
    description: str = Field(..., example="Latest iPhone model")
    stock: int = Field(..., ge=0, example=100)
    price: float = Field(..., gt=0, example=999.99)
    sku: str = Field(..., example="IPHONE12-64GB-BLACK")
    category: str = Field(..., example="Electronics")

    model_config = ConfigDict(from_attributes=True)


class ProductResponse(ProductBase):
    pass


class ProductListResponse(ResponseBase):
    data: List[ProductResponse] = Field(default_factory=list)


class ProductCreateRequestBody(ProductBase):
    pass


class CreateProductResponse(ResponseBase):
    data: ProductResponse
