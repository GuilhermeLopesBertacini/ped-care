### Comandos Básicos do Rye

* **`rye init`**: Cria um novo projeto Python ou "adota" um projeto existente que já tenha um `pyproject.toml`.

* **`rye sync`**: O comando mais importante. Ele lê seu arquivo `pyproject.toml`, cria um ambiente virtual (se não existir) e instala/atualiza todos os pacotes para corresponder exatamente ao que está definido no projeto. É o seu comando para "instalar tudo".

* **`rye add <nome-do-pacote>`**: Adiciona um novo pacote ao seu projeto. Ele automaticamente edita o `pyproject.toml` e depois sincroniza o ambiente.
    * Para adicionar uma dependência de desenvolvimento (como `pytest`), use: `rye add --dev pytest`.

* **`rye remove <nome-do-pacote>`**: Remove um pacote do projeto, atualizando o `pyproject.toml` e o ambiente.

* **`rye run <comando>`**: Executa um comando dentro do ambiente virtual gerenciado pelo Rye. É assim que você roda seus scripts ou ferramentas.
    * Exemplo: `rye run python meu_script.py`
    * Exemplo: `rye run pytest`
