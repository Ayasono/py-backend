from app.db.session import Base
from sqlalchemy import Column, String, Integer


class Categories(Base):
    __tablename__ = 'categories'

    name = Column(String, primary_key=True, index=True)
    description = Column(String)
