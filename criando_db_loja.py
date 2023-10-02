import pandas as pd
"""
    Aqui será criado o arquivo csv que servirá como banco de dados da loja virtual.
    Para isso será preciso instalar: pip install pandas
"""

# Dados fictícios de produtos
produtos = [
    {"id": 1, "nome": "Camiseta", "preco": 19.99, "estoque": 100},
    {"id": 2, "nome": "Calça Jeans", "preco": 49.99, "estoque": 50},
    {"id": 3, "nome": "Tênis", "preco": 79.99, "estoque": 30},
    {"id": 4, "nome": "Boné", "preco": 9.99, "estoque": 200},
]

# Dados fictícios de clientes
clientes = [
    {"id": 1, "nome": "João da Silva", "email": "joao@email.com", "telefone": "123456789"},
    {"id": 2, "nome": "Maria Souza", "email": "maria@email.com", "telefone": "987654321"},
    {"id": 3, "nome": "Pedro Oliveira", "email": "pedro@email.com", "telefone": "555555555"},
]

# Dados fictícios de pedidos
pedidos = [
    {"id": 1, "cliente_id": 1, "data": "2023-10-02", "produtos": [{"produto_id": 1, "quantidade": 2}]},
    {"id": 2, "cliente_id": 2, "data": "2023-10-03", "produtos": [{"produto_id": 2, "quantidade": 1}, {"produto_id": 4, "quantidade": 3}]},
    {"id": 3, "cliente_id": 1, "data": "2023-10-04", "produtos": [{"produto_id": 3, "quantidade": 1}]},
]

# Dados fictícios de pagamento
pagamentos = [
    {"pedido_id": 1, "valor": 39.98, "status": "Aprovado", "data_aprovacao": "2023-10-02"},
    {"pedido_id": 2, "valor": 129.96, "status": "Aprovado", "data_aprovacao": "2023-10-03"},
    {"pedido_id": 3, "valor": 79.99, "status": "Aprovado", "data_aprovacao": "2023-10-04"},
]


# Definindo o nome do arquivo csv
arquivo_csv = 'dados_loja_online.csv'

# Função para salvar dados em um arquivo CSV
def salvar_dados_csv():
    # Criar um DataFrame para cada conjunto de dados
    df_produtos = pd.DataFrame(produtos)
    df_clientes = pd.DataFrame(clientes)
    df_pedidos = pd.DataFrame(pedidos)
    df_pagamentos = pd.DataFrame(pagamentos)

    # Salvar DataFrames em um arquivo CSV
    df_produtos.to_csv('produtos.csv', index=False)
    df_clientes.to_csv('clientes.csv', index=False)
    df_pedidos.to_csv('pedidos.csv', index=False)
    df_pagamentos.to_csv('pagamentos.csv', index=False)

    print(f'Dados salvos em arquivos CSV individuais.')

# Chama a função para salvar os dados em arquivos CSV
salvar_dados_csv()