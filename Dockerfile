FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
COPY main.py .

# Install Python dependencies with uv
RUN apk add --no-cache curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

# Copiar arquivos de dependência
COPY ./pyproject.toml /uv.lock ./

# Instalar dependências
RUN uv sync --frozen

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the application
CMD ["uv", "run", "main.py"]
