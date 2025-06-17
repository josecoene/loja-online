class Cliente():
    def __init__(self, nome):
        self.nome = nome
        self.carrinho = []

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        return self.nome == nome

    def adicionar_no_carinho(self, produto):
        self.carrinho.append(produto)

    def remover_do_carinho(self, nome_produto):
        for produto in self.carrinho:
            if produto.get_nome().lower() == nome_produto.lower():
                self.carrinho.remove(produto)
                print(f"Produto '{nome_produto}' removido do carrinho")
                return
        print(f"Produto '{nome_produto}' não encontrado no carrinho")

    def __str__(self):
        return f"Cliente: {self.nome}"
