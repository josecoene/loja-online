class Venda():
    def __init__(self, id_venda, cliente, vendedor):
        self.id_venda = id_venda
        self.cliente = cliente
        self.vendedor = vendedor
        self.itens = cliente.carrinho.copy()
        self.total = sum([produto.preco for produto in self.itens])

    def salvar_venda(self, nome_do_arquivo):
        with open(nome_do_arquivo, "w", encoding="utf-8") as f:
            f.write(f"Cliente: {self.cliente.get_nome()}\n")
            f.write(f"Vendedor: {self.vendedor.get_id()} - {self.vendedor.get_nome()}\n")
            f.write("--- Itens ---\n")
            for produto in self.itens:
                f.write(
                    f"Produto: {produto.get_nome()} - R${produto.get_preco()} - Quantidade: {produto.get_quantidade()}\n"
                )
            f.write(f"Total: R${self.total:.2f}\n")
