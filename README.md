# Aplicação CRUD usando MongoDB em Python

Este projeto é uma aplicação simples de CRUD (Create, Read, Update, Delete) utilizando MongoDB com Python. A aplicação permite gerenciar uma coleção de usuários no banco de dados hospedado no MongoDB Atlas.

## Estrutura do Projeto

- `crud.py`: Contém as funções para realizar operações CRUD no banco de dados.
- `main.py`: Gerencia a conexão com o banco de dados e fornece uma interface de linha de comando para interagir com o sistema.

## Funcionalidades

1. **Criar Usuário**: Permite adicionar um novo usuário à coleção.
2. **Ler Usuários**: Exibe todos os usuários armazenados na coleção.
3. **Atualizar Usuário**: Permite atualizar as informações de um usuário existente.
4. **Deletar Usuário**: Remove um usuário da coleção.

## Como Usar

1. Certifique-se de ter o Python instalado.
2. Instale as dependências necessárias:
   ```powershell
   pip install pymongo python-dotenv