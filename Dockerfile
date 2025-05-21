FROM python:3.12-slim

WORKDIR /app

# 环境变量，防止写pyc文件，实时输出日志
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="${PATH}:/root/.local/bin"

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    libpq-dev \
    python3-dev \
    postgresql-client \
    git \
    tzdata \
    mypy \
    && rm -rf /var/lib/apt/lists/*

# 升级 pip
RUN pip install --upgrade pip

# 安装 Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY pyproject.toml ./       
COPY poetry.lock ./      

COPY . .

RUN poetry config virtualenvs.create false

# 分开安装，便于调试
RUN pip install wheel psycopg2-binary==2.9.9
RUN poetry install --no-interaction --no-ansi --verbose

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
