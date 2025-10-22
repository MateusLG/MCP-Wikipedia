# MCP Wikipedia com Claude

## 📖 Sobre o Projeto

Este é um projeto que demonstra a implementação de um servidor **MCP (Model Context Protocol)** escrito em Python.

O objetivo é criar ferramentas locais (neste caso, uma busca na Wikipedia) e permitir que um LLM (como o **Claude**) as utilize para responder a perguntas. O cliente (`cliente.py`) orquestra a conversa entre o usuário, a API do Claude e o servidor MCP local (`servidor.py`).

O desenvolvimento foi feito com base na documentação oficial do MCP e utiliza o gerenciador de pacotes **UV** para um gerenciamento de dependências rápido e moderno.

## 🛠️ Tecnologias Principais

* **Python**
* **FastMCP**: A biblioteca principal para criar o servidor MCP.
* **Anthropic (Claude)**: A biblioteca cliente para se conectar ao LLM.
* **Wikipedia**: A biblioteca usada para a ferramenta de busca.
* **UV**: Gerenciador de pacotes e ambientes virtuais (usado no lugar de `pip` e `venv`).
* **python-dotenv**: Para carregar segredos (chaves de API).

## 🚀 Como Executar

Siga estes passos para configurar e rodar o projeto localmente.

### 1. Pré-requisitos

* Ter o [Python](https://www.python.org/downloads/) instalado (versão 3.10 ou superior).
* Ter o [UV](https://github.com/astral-sh/uv) instalado. (Se preferir, pode usar `pip` e `venv` normalmente).
* Uma chave de API da [Anthropic (Claude)](https://console.anthropic.com/).

### 2. Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/MateusLG/MCP-Wikipedia.git](https://github.com/MateusLG/MCP-Wikipedia.git)
    cd MCP-Wikipedia
    ```

2.  **Crie e ative o ambiente virtual (com UV):**
    ```bash
    # Cria o ambiente virtual na pasta .venv
    uv venv
    
    # Ativa o ambiente (Windows)
    .\.venv\Scripts\activate
    
    # Ativa o ambiente (Linux/macOS)
    source .venv/bin/activate
    ```

3.  **Instale as dependências (com UV):**
    ```bash
    uv pip install -r requirements.txt
    ```

### 3. Configuração

1.  Crie um arquivo chamado `.env` na raiz do projeto.
2.  Adicione sua chave de API do Claude dentro dele:

    ```ini
    ANTHROPIC_API_KEY="sk-sua-chave-aqui..."
    ```

### 4. Execução

O projeto é dividido em um **cliente** e um **servidor**, mas o cliente foi programado para iniciar o servidor automaticamente.

Basta executar o script do cliente (`cliente.py`) e passar o script do servidor (`servidor.py`) como argumento:

```bash
python cliente.py servidor.py