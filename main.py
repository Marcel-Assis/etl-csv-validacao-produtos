import csv
#1
with open('produtos.csv', 'r') as file:
    leitor = csv.DictReader(file)
    for linha in leitor:
        print(linha)
#2
with open('produtos.csv', 'r') as file:
    leitor = csv.DictReader(file)
    for linha in leitor:
        if float(linha['preco']) <= 0:
            print(f"{linha['nome']} inválido")
        else:
            print(f"{linha['nome']} válido")
#3
produtos_validos = []
with open('produtos.csv', 'r') as file:
    leitor = csv.DictReader(file)
    for linha in leitor:
        if float(linha['preco']) <= 0:
            print(f"{linha['nome']} inválido")
        else:
            print(f"{linha['nome']} válido")
            produtos_validos.append({"nome": linha["nome"], "preco": float(linha['preco'])})
print(produtos_validos)
#4
with open('produtos_limpos.csv', 'w', newline="") as file:
    colunas = ["nome", "preco"]
    escritor = csv.DictWriter(file, fieldnames=colunas)
    escritor.writeheader()
    escritor.writerows(produtos_validos)