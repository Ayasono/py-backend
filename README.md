# py-backend

## used technologies
- python = "^3.12"
- fastapi = "^0.111.0"
- uvicorn = "^0.30.1"
- sqlalchemy = "^2.0.30"
- postgresql = "^16.0"

## implemented endpoints

- GET /api/v1/products
  - get all products
- GET /api/v1/products/{sku}
  - get product by sku
- POST /api/v1/products
  - create a new product


## how to run the project
in **root** directory
```bash
uvicorn app.main:app --reload
```
