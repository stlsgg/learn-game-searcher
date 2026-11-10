FROM python:3.14-slim
COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /bin/
WORKDIR /app
COPY uv.lock pyproject.toml ./
RUN uv sync --frozen --no-dev
COPY . .
# CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0"]
CMD ["uv", "run", "fastapi", "run", "main.py", "--host", "0.0.0.0"]
