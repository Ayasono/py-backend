from app.models.users import Users
from app.db.session import get_db
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.response_base.response_base import ResponseBase
from pydantic import BaseModel
from app.schemas.user_responses.get_user_schema import UserResponse
from app.schemas.user_responses.delete_user_schema import DeleteUserResponse
from app.schemas.user_responses.create_user_schema import CreateUserResponse
from typing import Optional
from sqlalchemy.orm import Session

userRouter = APIRouter()


@userRouter.get("/", response_model=UserResponse, description="Get all users")
async def read_users(db: Session = Depends(get_db)):
    users = db.query(Users).all()

    return ResponseBase(code=200, message="ok", data=users)


class CreateUserRequestBody(BaseModel):
    name: str
    email: str
    password: str
    role: Optional[str] = "user"
    address: Optional[str] = ""
    phone: Optional[str] = ""


@userRouter.post("/", response_model=CreateUserResponse, description="Create new user")
async def create_user(user: CreateUserRequestBody, db: Session = Depends(get_db)):
    new_user = Users(name=user.name, email=user.email, role=user.role, address=user.address, phone=user.phone,
                     password=user.password)
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return ResponseBase(code=200, message="User created", data=new_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to create user: {e}")


@userRouter.delete("/{email}", response_model=DeleteUserResponse, description="Delete user by id")
async def delete_user(email: str, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        db.delete(user)
        db.commit()
        return ResponseBase(code=200, message="User deleted", data=user)
