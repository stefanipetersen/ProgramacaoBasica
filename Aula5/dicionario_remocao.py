dicionario = {
    "Yoda":"Mestre Jedi",
    "Mace Windu": "Mestre Jedi",
    "Anakin Skywalker": "Cavaleiro Jedi",
    "R2-D2": "Dróide",
    "Dex": "Balconista"
}

print(dicionario)

#Para remover a chave do dicionário:
dicionario.pop("Yoda")
print(dicionario)

#Para remover o ultimo item do dicionário:
dicionario.popitem()
print(dicionario)

#Para limpar o dicionário basta:
dicionario.clear()
print(dicionario)