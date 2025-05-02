# Inventory-Management

# 📦 Sistema de Gerenciamento de Estoque (Flask + SQLite)

Este é um sistema básico de gerenciamento de estoque feito com Python, Flask e SQLite. Ele permite adicionar, listar, editar e remover produtos de um banco de dados.

## 🚀 Funcionalidades

- ✅ Listar todos os produtos
- ➕ Adicionar novos produtos
- 📝 Editar produtos existentes
- 🗑️ Remover produtos do estoque

## 🛠️ Tecnologias utilizadas

- Python 3.13+
- Flask
- SQLite3
- HTML (com Jinja2)

## 📁 Estrutura do projeto

estoque_flask/

├── app.py

├── estoque.db # Gerado automaticamente

├── templates/

│ ├── index.html

│ ├── adicionar.html

│ └── editar.html

├── static/ # (opcional) arquivos CSS, JS, imagens

├── venv/ # Ambiente virtual

└── requirements.txt # (opcional)


## ⚙️ Como executar o projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seuusuario/estoque_flask.git
   cd estoque_flask

2. **Crie o ambiente virtual**
   
    -No Windows:
   
    .\venv\Scripts\activate
   
    -No Linux/macOS:

    source venv/bin/activate

3. **Instale as dependências**

    pip install flask
  
4. **Execute a aplicação**

    python app.py
  
5. **Acesse no navegador**

    http://127.0.0.1:5000

## 🗃️ Banco de dados
O banco estoque.db será criado automaticamente com a tabela produtos, que possui os seguintes campos:

id (inteiro, chave primária)

nome (texto)

descricao (texto)

quantidade (inteiro)

preco (decimal)

## 📌 Próximas melhorias
 Validação de formulário

 Campo de busca por nome

 Filtro por quantidade baixa

 Tela de login para administradores

Feito com ❤️ usando Flask e SQLite.
