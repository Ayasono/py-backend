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
app.include_router(product.router, prefix="/products", tags=["products"])
