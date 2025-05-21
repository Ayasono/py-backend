from app.schemas.response_base.response_base import ResponseBase
from pydantic import BaseModel
from typing import List


class UsersInfo(BaseModel):
    name: str
    email: str
    role: str


class UserResponse(ResponseBase):
    data: List[UsersInfo]
