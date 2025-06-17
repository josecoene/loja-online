class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco

    def get_quantidade(self):
        return self.quantidade

    def set_quantidade(self, quantidade):
        self.quantidade = quantidade

    def set_preco(self, preco):
        self.preco = preco

    def set_nome(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Produto: {self.nome} - R${self.preco} - Quantidade: {self.quantidade}"