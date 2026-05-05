#Possui as mesmas funções que a lista, menos o append e o pop, pois elas não aceitam acrescentar ou remover os elementos de sua lista.

categorias = ("Youngling", "Padawan", "Jedi", "Mestre")

for categoria in categorias:
    print(categoria)

#Se vc criar um nova tupla ele destroi a anterior e usar apenas os valores novos q vc inseriu
categorias = ("A", "B", "C", "D", "E")

for categoria in categorias:
    print(categoria)

categoria = input("Insira a categoria da sua CNH: ")

if categoria.upper() in categorias:
    print("Categoria existente!")
else:
    print("Categoria inexistente!")
