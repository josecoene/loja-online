class Vendedor:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

    def get_nome(self):
        return self.nome

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Vendedor: {self.id} - {self.nome}"