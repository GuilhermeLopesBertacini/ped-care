FROM python:3.12-alpine

WORKDIR /app

# Install Python dependencies with uv
RUN apk add --no-cache curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:$PATH"

# Copiar arquivos de dependência
COPY pyproject.toml uv.lock ./

# Instalar dependências (sem instalar/buildar o projeto em si)
RUN uv sync --frozen --no-install-project

# Copiar código da aplicação
COPY main.py .
COPY app ./app

# Instalar o projeto (editable) agora que o código está presente
RUN uv sync --frozen

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the application
CMD ["uv", "run", "main.py"]