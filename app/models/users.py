from app.db.session import Base
from sqlalchemy import Column, String, Integer, Enum
import enum


class UsersEnum(enum.Enum):
    admin = "admin"
    user = "user"
    test = "test"


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    name = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    address = Column(String)
    phone = Column(String)
    role = Column(Enum(UsersEnum), default=UsersEnum.user, nullable=False)

    class Config:
        orm_mode = True
