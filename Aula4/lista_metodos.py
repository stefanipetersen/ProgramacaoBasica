#1 Valores fora de ordem
valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5, 3.5]

#Exibição da lista
print("1- A lista foi criada assim: {}".format(valores))

#2 Contagem de elementos 1
contagem = valores.count(1)
print(f"2- A contagem de números 1 foi de {contagem}")

#3 Invertendo a lista
valores.reverse()
print(f"3- A lista invertida ficou assim: {valores}")

#4 Ordenando a lista (não é possível ordenar se a lista tiver um str)
valores.sort()
print(f"4- A lista em ordem crescente: {valores}")

valores.sort(reverse=True)
print(f"4- A lista em ordem decrescente: {valores}")

#5 Tamanho da lista
len(valores)
quantidade = len(valores)
print(f"5- Quantidade de elementos na lista: {quantidade}")

#6 Soma dos elementos
soma = sum(valores)
print(f"6- A soma dos valores da lista é: {soma}")


