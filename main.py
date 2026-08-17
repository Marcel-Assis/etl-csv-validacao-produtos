import csv


def ler_csv(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)


def validar_produto(linha):
    try:
        preco_numero = float(linha['preco'])
        return preco_numero > 0
    except (ValueError, KeyError):
        return False


def salvar_csv(caminho_arquivo_saida, lista_dados_validados, colunas):
    with open(caminho_arquivo_saida, 'w', newline='') as file:
        escritor = csv.DictWriter(file, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(lista_dados_validados)


def main():
    caminho_arquivo = 'produtos.csv'
    linhas = ler_csv(caminho_arquivo)
    produtos_validos = []
    colunas = ['nome', 'preco', 'quantidade']

    for linha in linhas:
        if validar_produto(linha):
            novo_produto = {chave: linha[chave] for chave in colunas}
            produtos_validos.append(novo_produto)

    salvar_csv('produtos_validados.csv', produtos_validos, colunas)

    total = len(linhas)
    validos = len(produtos_validos)
    descartados = total - validos
    print(f"{total} produtos lidos, {validos} válidos, {descartados} descartados")


if __name__ == "__main__":
    main()