from app.schemas.response_base.response_base import ResponseBase
from pydantic import BaseModel


class UsersInfo(BaseModel):
    name: str
    email: str
    role: str


class DeleteUserResponse(ResponseBase):
    data: UsersInfo
