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
make docker-run
```

**Parar os serviços:**
```bash
make docker-stop
```

**Parar e remover volumes (⚠️ apaga dados do banco):**
```bash
make docker-down
```

### 🌐 Acessando a aplicação

Caso não tenha definido as portas do projeto no arquivo .env:

- **API**: http://localhost:8000
- **Documentação (Swagger)**: http://localhost:8000/docs
- **MySQL**: localhost:3306

### 📦 Serviços

O projeto contém dois serviços principais:

- **app**: Aplicação FastAPI (Python 3.12)
- **mysql**: Banco de dados MySQL 8.0

### 🛠️ Desenvolvimento

Os arquivos da pasta `app/` são montados como volume, permitindo hot-reload durante o desenvolvimento. Qualquer alteração no código será refletida automaticamente no container.

Uma opção mais simples, sem o uso do docker, consiste em utilizar o uv - gerenciador de pacotes e projetos. Para isso, basta executar:

```bash
make run
```