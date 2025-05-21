FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    libpq-dev \
    python3-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"

COPY pyproject.toml ./       
COPY poetry.lock ./      

RUN poetry config virtualenvs.create false

# 分开 install，便于 debug
RUN pip install wheel psycopg2-binary==2.9.9
RUN poetry install --no-interaction --no-ansi --verbose

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
