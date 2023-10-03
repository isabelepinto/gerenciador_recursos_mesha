import pandas as pd
import json
from datetime import datetime

# Leitura dos arquivos CSV
df_produtos = pd.read_csv('produtos.csv')
df_clientes = pd.read_csv('clientes.csv')
df_pedidos = pd.read_csv('pedidos.csv')
df_pagamentos = pd.read_csv('pagamentos.csv')

# Função para salvar dados em um arquivo CSV
def salvar_dados_csv():
    global df_clientes, df_produtos, df_pedidos, df_pagamentos  # Declare as variáveis como globais
    df_clientes.to_csv('clientes.csv', index=False)
    df_produtos.to_csv('produtos.csv', index=False)
    df_pedidos.to_csv('pedidos.csv', index=False)
    df_pagamentos.to_csv('pagamentos.csv', index=False)

# Função para adicionar pedidos a partir de um arquivo JSON
def adicionar_pedidos_de_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            novos_pedidos = json.load(arquivo)

        for novo_pedido in novos_pedidos:
            cliente_id = novo_pedido["cliente_id"]
            produtos = novo_pedido["produtos"]
            
            # Crie o novo pedido conforme sua lógica de negócios
            novo_id = df_pedidos['id'].max() + 1 if not df_pedidos.empty else 1
            data = datetime.now().strftime("%Y-%m-%d")
            
            # Adicione o novo pedido ao DataFrame df_pedidos
            novo_pedido = {
                "id": novo_id,
                "cliente_id": cliente_id,
                "data": data,
                "produtos": json.dumps(produtos),
            }
            df_pedidos = df_pedidos.concat(novo_pedido, ignore_index=True)
        
        # Salve os dados após adicionar os pedidos
        salvar_dados_csv()
        print("Pedidos adicionados com sucesso.")

    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

# Função para adicionar um novo cliente
def adicionar_cliente():
    global df_clientes  
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
    df_clientes = df_clientes.concat(novo_cliente, ignore_index=True)
    salvar_dados_csv()

# Função para adicionar um novo pedido
def adicionar_pedido():
    global df_pedidos, df_produtos  # Declare as variáveis como globais
    novo_id = df_pedidos['id'].max() + 1 if not df_pedidos.empty else 1
    
    cliente_id = int(input("Digite o ID do cliente: "))
    if cliente_id < 1 or cliente_id > len(df_clientes):
        print("Cliente não encontrado.")
        return
    
    data = datetime.now().strftime("%Y-%m-%d")
    
    produtos = []
    while True:
        produto_id = int(input("Digite o ID do produto: "))
        if produto_id < 1 or produto_id > len(df_produtos):
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
    df_pedidos = df_pedidos.concat(novo_pedido, ignore_index=True)
    salvar_dados_csv()

# Função para adicionar um novo produto
def adicionar_produto():
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
    novo_id = df_pagamentos['id'].max() + 1 if not df_pagamentos.empty else 1
    
    pedido_id = int(input("Digite o ID do pedido: "))
    if pedido_id < 1 or pedido_id > len(df_pedidos):
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
    df_pagamentos = df_pagamentos.concat(novo_pagamento, ignore_index=True)
    salvar_dados_csv()

# Função para listar os clientes e seus IDs
def listar_clientes():
    print("\nLista de Clientes:")
    for i, cliente in df_clientes.iterrows():
        print(f"ID: {cliente['id']}, Nome: {cliente['nome']}, Email: {cliente['email']}")

# Função para listar os pedidos de um cliente
def listar_pedidos_cliente(cliente_id, df_clientes, df_pedidos):
    print("\nPedidos do Cliente:")
    for i, pedido in df_pedidos[df_pedidos['cliente_id'] == cliente_id].iterrows():
        print(f"ID: {pedido['id']}, Cliente: {df_clientes.loc[df_clientes['id'] == cliente_id, 'nome'].values[0]}, Produto: {pedido['produtos']}")

# Função para listar os pagamentos de um cliente
def listar_pagamentos_cliente(cliente_id, df_clientes, df_pedidos, df_pagamentos):
    print("\nPagamentos do Cliente:")
    pedidos_do_cliente = df_pedidos[df_pedidos['cliente_id'] == cliente_id]['id']
    pagamentos_do_cliente = df_pagamentos[df_pagamentos['pedido_id'].isin(pedidos_do_cliente)]
    for i, pagamento in pagamentos_do_cliente.iterrows():
        print(f"ID: {pagamento['pedido_id']}, Valor: {pagamento['valor']}, Status: {pagamento['status']}, Data de Aprovação: {pagamento['data_aprovacao']}")

# Função para listar os produtos
def listar_produtos():
    print("\nLista de Produtos:")
    for i, produto in df_produtos.iterrows():
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Estoque: {produto['estoque']}")

# Função para listar todos os pedidos
def listar_pedidos():
    print("\nLista de Pedidos:")
    for i, pedido in df_pedidos.iterrows():
        print(f"ID: {pedido['id']}, Cliente: {pedido['cliente_id']}, Produto: {pedido['produtos']}, Quantidade: {pedido['quantidade']}, Valor Unitário: {pedido['valor_unitario']}, Total: {pedido['total']}")

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
                listar_pedidos_cliente(cliente_id, df_clientes, df_pedidos)  
            elif escolha_cliente == "3":
                cliente_id = int(input("Digite o seu ID de cliente: "))
                listar_pagamentos_cliente(cliente_id, df_clientes, df_pedidos, df_pagamentos)  
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
            print("5 - Adicionar Pedidos através de Json")
            print("6 - Listar Clientes")
            print("7 - Listar Pedidos")
            print("8 - Listar Produtos")
            print("9 - Listar Pagamentos")
            print("10 - Gerar Relatório")
            print("11 - Voltar")

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
                adicionar_pedidos_de_arquivo(input("Digite o nome do arquivo com a extensão: "))
            elif escolha_loja == "6":
                listar_clientes()
            elif escolha_loja == "7":
                listar_pedidos()
            elif escolha_loja == "8":
                listar_produtos()
            elif escolha_loja == "9":
                listar_pagamentos()
            elif escolha_loja == "10":
                gerar_relatorio()
            elif escolha_loja == "11":
                break
            else:
                print("Opção inválida.")

    elif escolha == "3":
        break

    else:
        print("Opção inválida.")