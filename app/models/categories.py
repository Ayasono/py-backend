from app.db.session import Base
from sqlalchemy import Column, String, Integer


class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

    class Config:
        orm_mode = True
