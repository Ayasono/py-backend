from typing import Optional, TypeVar, Generic
from pydantic import BaseModel, Field

T = TypeVar('T')

class ResponseBase(BaseModel, Generic[T]):  # Use BaseModel instead of GenericModel
    code: int = Field(..., description="status code")
    message: str = Field(..., description="response message")
    data: Optional[T] = Field(None, description="response data")
