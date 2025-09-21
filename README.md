# PED CARE

Projeto desenvolvido durante um hackathon com o foco em facilitar o processo de
agendamento de consultas no contexto de saúde.

### Pré-requisitos

Antes de começar, você precisa ter o [Rye](https://rye.astral.sh/) instalado na sua máquina.

### Instalação e Execução do Projeto

1.  **Clone o repositório:**

    ```bash
    git clone <url-do-seu-repositorio>
    cd ped-care
    ```

2.  **Instale as dependências:**
    O Rye vai ler o arquivo `pyproject.toml`, criar um ambiente virtual e instalar tudo o que for necessário com um único comando.

    ```bash
    rye sync
    ```

3.  **Execute a aplicação:**
    Use o `rye run` para executar o servidor dentro do ambiente virtual gerenciado por ele.

    ```bash
    rye run uvicorn app.main:app --reload
    ```

A aplicação estará rodando em `http://127.0.0.1:8000`.