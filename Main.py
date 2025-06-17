from Venda import Venda
from Arquivo_aux import gerar_nome_arquivo
from Entrada import coletar_dados_venda

def main():
    id_venda, cliente, vendedor = coletar_dados_venda()
    venda = Venda(id_venda, cliente=cliente, vendedor=vendedor)

    nome_arquivo = ()
    nome_arquivo = gerar_nome_arquivo()
    venda.salvar_venda(nome_arquivo)

if __name__ == "__main__":
    main()
