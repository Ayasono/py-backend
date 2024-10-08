
## how to run

```bash
uvicorn app.main:app --reload
```

## Implemented Endpoints

### Products

- GET /api/v1/products
    - Get all products
- GET /api/v1/products/{sku}
    - Get product by SKU
- POST /api/v1/products
    - Create a new product
- PUT /api/v1/products/{sku}
    - Update product by SKU
- DELETE /api/v1/products/{sku}
    - Delete product by SKU

### Categories

- GET /api/v1/categories
    - Get all categories
- GET /api/v1/categories/{id}
    - Get category by ID
- POST /api/v1/categories
    - Create a new category
- PUT /api/v1/categories/{id}
    - Update category by ID
- DELETE /api/v1/categories/{id}
    - Delete category by ID

### Users

- GET /api/v1/users
    - Get all users
- GET /api/v1/users/{id}
    - Get user by ID
- POST /api/v1/users
    - Create a new user
- PUT /api/v1/users/{id}
    - Update user by ID
- DELETE /api/v1/users/{id}
    - Delete user by ID

### Orders

- POST /api/v1/orders
    - Create a new order

## Database Configuration

Ensure that you correctly configure the database connection parameters in the `config/database_config.json` file.

## Project Structure

- `app/`: Main application directory
  - `api/`: API-related code
  - `core/`: Core configurations
  - `db/`: Database-related code
  - `models/`: Data models
  - `schemas/`: Pydantic models
- `tests/`: Test directory
