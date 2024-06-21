from fastapi import FastAPI
from app.db.session import engine, Base
from app.api.v1.endpoints import product

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)


# root route
@app.get("/")
def read_root():
    return {"Hello": "World"}


# include routers
common_prefix = "/api/v1"
app.include_router(product.router, prefix=f'{common_prefix}/products', tags=["products"])
