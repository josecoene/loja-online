from Cliente import Cliente
from Vendedor import Vendedor
from Produto import Produto

def coletar_dados_venda():
    print("--- CADASTRO DO CLIENTE ---")
    nome_cliente = input("Digite o nome do cliente: ")
    cliente = Cliente(nome_cliente)

    print("--- CADASTRO DO VENDEDOR ---")
    nome_vendedor = input("Digite o nome do vendedor: ")
    id_vendedor = int(input("Digite o id do vendedor: "))
    vendedor = Vendedor(nome_vendedor, id_vendedor)

    print("\n --- ADICIONAR PRODUTOS AO CARRINHO ---")
    while True:
        acao = input("\nDigite 'a' para adicionar, 'r' para remover e 'f' para finalizar: ".lower())

        if acao == 'a':
            nome_produto = input("Nome do produto: ")
            preco = float(input("Preço do produto: R$"))
            quantidade = int(input("Quantidade: "))
            produto = Produto(nome_produto, preco=preco, quantidade=quantidade)
            cliente.adicionar_no_carinho(produto=produto)
            print(f"{nome_produto} adicionado.")

        elif acao == 'r':
            nome_produto = input("Nome do produto a remover: ")
            cliente.remover_do_carinho(nome_produto=nome_produto)

        elif acao == 'f':
            break

        else:
            print("Opção inválida. Use 'a', 'r' ou 'f'.")

    id_venda = int(input("\nDigite o id da venda: "))

    return id_venda, cliente, vendedor
