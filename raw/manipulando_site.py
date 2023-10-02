import pandas as pd
import json
from datetime import datetime
"""
    Aqui será criado o arquivo csv que servirá como banco de dados da loja virtual.
    Para isso será preciso instalar: pip install pandas e pip install json
"""


# Leitura dos arquivos CSV
df_produtos = pd.read_csv('produtos.csv')
df_clientes = pd.read_csv('clientes.csv')
df_pedidos = pd.read_csv('pedidos.csv')
df_pagamentos = pd.read_csv('pagamentos.csv')


# Função para salvar dados em um arquivo CSV
def salvar_dados_csv():
    df_clientes.to_csv('clientes.csv', index=False)  # Atualize o arquivo CSV de clientes
    df_produtos.to_csv('produtos.csv', index=False)  # Atualize o arquivo CSV de produtos
    df_pedidos.to_csv('pedidos.csv', index=False)  # Atualize o arquivo CSV de pedidos
    df_pagamentos.to_csv('pagamentos.csv', index=False)  # Atualize o arquivo CSV de pagamentos


# Função para adicionar um novo cliente
def adicionar_cliente():
    global df_clientes
    # Obtenha o próximo ID incremental
    novo_id = df_clientes['id'].max() + 1 if not df_clientes.empty else 1
    
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    
    novo_cliente = {
        "id": novo_id,
        "nome": nome,
        "email": email,
        "telefone": telefone,
    }
    df_clientes = df_clientes.append(novo_cliente, ignore_index=True)
    salvar_dados_csv()


# Função para adicionar um novo pedido
def adicionar_pedido():
    global df_pedidos
    # Obtenha o próximo ID incremental
    novo_id = df_pedidos['id'].max() + 1 if not df_pedidos.empty else 1
    
    cliente_id = int(input("Digite o ID do cliente: "))
    if cliente_id < 0 or cliente_id >= len(df_clientes):
        print("Cliente não encontrado.")
        return
    
    # Obtenha a data atual
    data = datetime.now().strftime("%Y-%m-%d")
    
    produtos = []
    while True:
        produto_id = int(input("Digite o ID do produto: "))
        if produto_id < 0 or produto_id >= len(df_produtos):
            print("Produto não encontrado.")
            continue
        
        quantidade = int(input("Digite a quantidade do produto: "))
        produtos.append({"produto_id": produto_id, "quantidade": quantidade})
        
        mais_produtos = input("Adicionar mais produtos? (S/N): ").lower()
        if mais_produtos != "s":
            break
    
    produtos_json = json.dumps(produtos)
    
    novo_pedido = {
        "id": novo_id,
        "cliente_id": cliente_id,
        "data": data,
        "produtos": produtos_json,
    }
    df_pedidos = df_pedidos.append(novo_pedido, ignore_index=True)
    salvar_dados_csv()


# Função para adicionar um novo produto
def adicionar_produto():
    global df_produtos
    # Obtenha o próximo ID incremental
    novo_id = df_produtos['id'].max() + 1 if not df_produtos.empty else 1
    
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite o estoque do produto: "))
    
    novo_produto = {
        "id": novo_id,
        "nome": nome,
        "preco": preco,
        "estoque": estoque,
    }
    df_produtos = df_produtos.append(novo_produto, ignore_index=True)
    salvar_dados_csv()


# Função para adicionar um novo pagamento
def adicionar_pagamento():
    global df_pagamentos
    # Obtenha o próximo ID incremental
    novo_id = df_pagamentos['id'].max() + 1 if not df_pagamentos.empty else 1
    
    pedido_id = int(input("Digite o ID do pedido: "))
    if pedido_id < 0 or pedido_id >= len(df_pedidos):
        print("Pedido não encontrado.")
        return

    valor = float(input("Digite o valor do pagamento: "))
    status = input("Digite o status do pagamento: ")
    data_aprovacao = input("Digite a data de aprovação do pagamento (formato yyyy-mm-dd): ")
    
    novo_pagamento = {
        "id": novo_id,
        "pedido_id": pedido_id,
        "valor": valor,
        "status": status,
        "data_aprovacao": data_aprovacao,
    }
    df_pagamentos = df_pagamentos.append(novo_pagamento, ignore_index=True)
    salvar_dados_csv()


# Função para listar os clientes e seus IDs
def listar_clientes():
    print("\nLista de Clientes:")
    for i, cliente in df_clientes.iterrows():
        print(f"ID: {cliente['id']}, Nome: {cliente['nome']}, Email: {cliente['email']}")


# Função para listar os pedidos de um cliente
def listar_pedidos_cliente(cliente_id):
    print("\nPedidos do Cliente:")
    for i, pedido in df_pedidos[df_pedidos['cliente_id'] == cliente_id].iterrows():
        print(f"ID: {pedido['id']}, Produto: {pedido['produto']}, Quantidade: {pedido['quantidade']}, Valor Unitário: {pedido['valor_unitario']}, Total: {pedido['total']}")


# Função para listar os pagamentos de um cliente
def listar_pagamentos_cliente(cliente_id):
    print("\nPagamentos do Cliente:")
    pedidos_do_cliente = df_pedidos[df_pedidos['cliente_id'] == cliente_id]['id']
    pagamentos_do_cliente = df_pagamentos[df_pagamentos['pedido_id'].isin(pedidos_do_cliente)]
    for i, pagamento in pagamentos_do_cliente.iterrows():
        print(f"ID: {pagamento['id']}, Valor: {pagamento['valor']}, Status: {pagamento['status']}, Data de Aprovação: {pagamento['data_aprovacao']}")


# Função para listar os produtos
def listar_produtos():
    print("\nLista de Produtos:")
    for i, produto in df_produtos.iterrows():
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Estoque: {produto['estoque']}")


# Função para listar todos os pedidos
def listar_pedidos():
    print("\nLista de Pedidos:")
    for i, pedido in df_pedidos.iterrows():
        print(f"ID: {pedido['id']}, Cliente: {pedido['cliente']}, Produto: {pedido['produto']}, Quantidade: {pedido['quantidade']}, Valor Unitário: {pedido['valor_unitario']}, Total: {pedido['total']}")


# Função para listar todos os pagamentos
def listar_pagamentos():
    print("\nLista de Pagamentos:")
    for i, pagamento in df_pagamentos.iterrows():
        print(f"ID: {pagamento['id']}, Pedido ID: {pagamento['pedido_id']}, Valor: {pagamento['valor']}, Status: {pagamento['status']}, Data de Aprovação: {pagamento['data_aprovacao']}")


# Função para calcular o total da compra
def calcular_total_compra():
    return df_pedidos['total'].sum()


# Função para gerar um relatório de pedidos
def gerar_relatorio():
    print("\nRelatório de Pedidos:")
    for i, pedido in df_pedidos.iterrows():
        print(f"ID: {pedido['id']}, Cliente: {pedido['cliente']}, Produto: {pedido['produto']}, Quantidade: {pedido['quantidade']}, Valor Unitário: {pedido['valor_unitario']}, Total: {pedido['total']}")
    total_compra = calcular_total_compra()
    print(f"Total da Compra: {total_compra}")


# Exemplo de uso
while True:
    print("\nOpções:")
    print("1 - Menu do Cliente")
    print("2 - Menu da Loja")
    print("3 - Sair")

    escolha = input("Escolha uma opção: ")


    if escolha == "1":
        # Menu do Cliente (acesso limitado)
        while True:
            print("\nMenu do Cliente:")
            print("1 - Listar Produtos")
            print("2 - Listar Meus Pedidos")
            print("3 - Listar Meus Pagamentos")
            print("4 - Voltar")

            escolha_cliente = input("Escolha uma opção: ")

            if escolha_cliente == "1":
                listar_produtos()
            elif escolha_cliente == "2":
                cliente_id = int(input("Digite o seu ID de cliente: "))
                listar_pedidos_cliente(cliente_id)
            elif escolha_cliente == "3":
                cliente_id = int(input("Digite o seu ID de cliente: "))
                listar_pagamentos_cliente(cliente_id)
            elif escolha_cliente == "4":
                break
            else:
                print("Opção inválida.")


    elif escolha == "2":
        # Menu da Loja (permissão total)
        while True:
            print("\nMenu da Loja:")
            print("1 - Adicionar Cliente")
            print("2 - Adicionar Pedido")
            print("3 - Adicionar Produto")
            print("4 - Adicionar Pagamento")
            print("5 - Listar Clientes")
            print("6 - Listar Pedidos")
            print("7 - Listar Produtos")
            print("8 - Listar Pagamentos")
            print("9 - Gerar Relatório")
            print("10 - Voltar")

            escolha_loja = input("Escolha uma opção: ")

            if escolha_loja == "1":
                adicionar_cliente()
            elif escolha_loja == "2":
                adicionar_pedido()
            elif escolha_loja == "3":
                adicionar_produto()
            elif escolha_loja == "4":
                adicionar_pagamento()
            elif escolha_loja == "5":
                listar_clientes()
            elif escolha_loja == "6":
                listar_pedidos()
            elif escolha_loja == "7":
                listar_produtos()
            elif escolha_loja == "8":
                listar_pagamentos()
            elif escolha_loja == "9":
                gerar_relatorio()
            elif escolha_loja == "10":
                break
            else:
                print("Opção inválida.")
    
    
    elif escolha == "3":
        break
    
    else:
        print("Opção inválida.")
