# py-backend

## used technologies

- python = "^3.12"
- fastapi = "^0.111.0"
- uvicorn = "^0.30.1"
- sqlalchemy = "^2.0.30"
- postgresql = "^16.0"

## how to run the project

in **root** directory

```bash
uvicorn app.main:app --reload
```

## implemented endpoints

### products

- GET /api/v1/products
    - get all products
- GET /api/v1/products/{sku}
    - get product by sku
- POST /api/v1/products
    - create a new product
- PUT /api/v1/products/{sku}
    - update product by sku
- DELETE /api/v1/products/{sku}
    - delete product by sku

### categories

- GET /api/v1/categories
    - get all categories
- GET /api/v1/categories/{id}
    - get category by id
- POST /api/v1/categories
    - create a new category
- PUT /api/v1/categories/{id}
    - update category by id
- DELETE /api/v1/categories/{id}
    - delete category by id

### users

- GET /api/v1/users
    - get all users
- GET /api/v1/users/{id}
  - get user by id
- POST /api/v1/users
  - create a new user
- PUT /api/v1/users/{id}
  - update user by id
- DELETE /api/v1/users/{id}
  - delete user by id
