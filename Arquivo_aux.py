import os

def gerar_nome_arquivo(base_nome="venda", extensao=".txt"):
    i = 1
    while True:
        nome_arquivo = f"{base_nome}_{i}{extensao}"
        if not os.path.exists(nome_arquivo):
            return nome_arquivo
        i += 1