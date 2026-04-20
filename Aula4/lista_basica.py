#1 Criação de uma lista vazia
jedi = []
print(type(jedi))

#2 Criação de uma lista com os jedi Yoda, Luke, Obi-Wan, Anakin
jedis = ["Yoda", "Luke", "Obi-Wan", "Anakin"]

#3 Exibição de uma lista completa
print(jedis)

#4 Exibição de uma posição específica na lista
print(jedis[1])

#5 Exibição dos últimos elementos
print(jedis[-1])

#6 Exibição de um intervalo de elementos da lista
print(jedis[1:3])

#7 Exibição de cada item da lista
for nome in jedis:
    print(nome)

#8 Inserir um item no fim da lista
jedis.append('Luminara')
print(jedis)

#9 Inserir um item no fim da lista (cliente)
jedis.append(input("Digite o nome de um jedi: "))
print(jedis)

#10 Inserir um item em uma posição específica
jedis.insert(1, "Cebolinha")
print(jedis)

#11 Remover o último item da lista
jedis.pop()
print(jedis)

#12 Remover um item em uma posição específica
jedis.pop(1)
print(jedis)

#13 Remover um item específico
jedis.remove("Anakin")
print(jedis)

#14 Apagar a lista toda
jedis.clear()
print(jedis)
