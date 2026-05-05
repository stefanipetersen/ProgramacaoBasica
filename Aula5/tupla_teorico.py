#Para saber o tamanho de uma variável ou objeto basta colocar getsizeof.

#Importando o módulo sys
import sys

#A tupla apesar de ela ter um tamanho menor ele é imutável, não é possível adicionar ou remover os itens como as listas.
#Exemplo de uso que seria melhor usar a tupla: a estrutura da auto escola que só utiliza as mesmas categorias sempre (A,B,C,D,E)

lista = []
print("O objeto lista é do tipo {} e tem {} bytes".format(type(lista),sys.getsizeof(lista)))

tupla = ()
print("O objeto tupla é do tipo {} e tem {} bytes".format(type(tupla),sys.getsizeof(tupla)))

nome = "Stefani"
print("A variável nome é do tipo {} e tem {} bytes".format(type(nome),sys.getsizeof(nome)))

numero = 3
print("O número é do tipo {} e tem {} bytes".format(type(numero),sys.getsizeof(numero)))

numero_virgula = 3.6
print("O número é do tipo {} e tem {} bytes".format(type(numero_virgula),sys.getsizeof(numero_virgula)))





