# PED CARE

Projeto desenvolvido durante um hackathon com o foco em facilitar o processo de
agendamento de consultas no contexto de saúde.

## 🚀 Setup com Docker

Este projeto utiliza Docker Compose para facilitar o desenvolvimento e deployment.

### Pré-requisitos

- Docker
- Docker Compose

### Configuração

Edite o arquivo .env com suas credenciais

### 🏃 Executando o projeto

**Iniciar os serviços:**
```bash
docker compose up --build
docker compose up -d
docker compose logs -f app
```

**Parar os serviços:**
```bash
docker compose down
```

**Parar e remover volumes (⚠️ apaga dados do banco):**
```bash
docker compose down -v
```

### 🌐 Acessando a aplicação

- **API**: http://localhost:8000
- **Documentação (Swagger)**: http://localhost:8000/docs
- **MySQL**: localhost:3306

### 📦 Serviços

O projeto contém dois serviços principais:

- **app**: Aplicação FastAPI (Python 3.12)
- **mysql**: Banco de dados MySQL 8.0

### 🛠️ Desenvolvimento

Os arquivos da pasta `app/` são montados como volume, permitindo hot-reload durante o desenvolvimento. Qualquer alteração no código será refletida automaticamente no container.

### 🔧 Comandos úteis

```bash
# Rebuild apenas o serviço app
docker compose build app

# Executar comando dentro do container
docker compose exec app bash

# Ver status dos containers
docker compose ps

# Reiniciar um serviço específico
docker compose restart app
```
