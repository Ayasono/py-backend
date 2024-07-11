from app.models.users import Users
from app.db.session import get_db
from fastapi import APIRouter, Depends
from app.schemas.response_base.response_base import ResponseBase

userRouter = APIRouter()


@userRouter.get("/")
async def read_users(db=Depends(get_db)):
    users = db.query(Users).all()
    users_data = [
        {
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
        for user in users
    ]
    return ResponseBase(code=200, message="ok", data=users_data)
