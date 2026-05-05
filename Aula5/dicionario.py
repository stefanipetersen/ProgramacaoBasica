#O dicionário é uma estrutura de chave e valor, ou seja, é uma estrutura que associa um dado a outro dado.

dicionario = {
    "Yoda":"Mestre Jedi",
    "Obi-Wan":"Mestre Jedi",
    "Anakin":"Cavaleiro Jedi",
    "Grogu":"Youngling"
}

for nome, categoria in dicionario.items():
    print(f"O personagem {nome} é um {categoria}")

print(type(dicionario))
print(dicionario)
print(dicionario["Yoda"])
print(dicionario.get("Anakin"))
print(dicionario.get("Stefani"))
print(dicionario.items())

produto = {
    "nome":"cafeteira",
    "preço":100.00,
    "fornecedor": ["Fornecedor Supimpa", "Fornecedor Maneiro", "Fornecedor Legal"]
}
print(produto)
print(produto.keys())
print(produto.values())
print(len(produto.values()))
print(100.00 in produto.values())
print("cafeteira" in produto.values())

for chave in produto.keys():
    print(chave)
    print(produto[chave])
