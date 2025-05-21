from app.schemas.response_base.response_base import ResponseBase
from pydantic import BaseModel
from typing import Optional


class CreateUserRequestBody(BaseModel):
    name: str
    email: str
    password: str
    role: Optional[str] = "user"
    address: Optional[str] = ""
    phone: Optional[str] = ""


class CreateUserResponse(ResponseBase):
    data: CreateUserRequestBody
