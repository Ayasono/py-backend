from fastapi import FastAPI
from app.db.session import engine, Base
from app.api.v1.endpoints import product
from app.api.v1.endpoints import categories
from app.schemas.response_base.response_base import ResponseBase

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)


# root route
@app.get("/", response_model=ResponseBase)
def read_root():
    res = ResponseBase(code=200, message="Hello World")
    return res


# include routers
common_prefix = "/api/v1"
app.include_router(product.router, prefix=f'{common_prefix}/products', tags=["products"])
app.include_router(categories.router, prefix=f'{common_prefix}/categories', tags=["categories"])
