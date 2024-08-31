FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-dev --no-interaction --no-ansi

COPY . .

RUN chmod +x /app/*.sh

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "your_project_name.wsgi:application"]