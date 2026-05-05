# Para usar o comentário ou anotação use o #

# Variável: Representa um espaço de memória
# Diferente do Java vc não precisa especificar o tipo da variável e não precisa do ;
# Vc pode mudar a variável quando quiser

numero = 100
valor = 234.12
soma = numero + valor
print(soma)

# Para juntar texto com número é necessário alterar o tipo de dado do numero para texto (str)
# Tipos de dados: int - números inteiros (5), float - números decimais (12.55),
# Tipos de dados: str - textos ou strings ("Paulo" / 'Paulo, 13 anos')
# Tipos de dados: bool - lógicos (True/False)

mensagem = "Hello World"

print(mensagem + " " + str(soma))

# Operações de Entrada de Dados (input)
nome = input("Qual o seu nome? ")
idade = int (input("Qual a sua idade? "))
altura = float (input("Qual a sua altura? "))

# Da pra printar o texto sem alterar o tipo utilizando vírgula
print(nome,idade,altura)

# Da pra printar o texto utilizando f no ínicio junto com as {} para n precisar colocar o tipo de dado tbm
print(f"O seu nome é {nome} possui {idade} anos e mede {altura} metros")

# Da pra printar o texto utilizando .format no final
print("O seu nome é {} possui {} anos e mede {}".format(nome, idade, altura))

#versão velha utilizavam nesse formato
print("O seu nome é {} e sua idade é de {} anos".format(nome,idade))

# OPERADORES ARITMÉTICOS

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

print(a + b)            # Adição
print(a - b)            # Subtração
print(a * b)            # Multiplicação
print(a / b)            # Divisão (resulta em float)
print(a // b)           # Divisão inteira (resulta em int)
print(a % b)            # Resto de uma divisão (mod)
print(a ** b)           # Potência

# Ordem de Prioridade:
# 1º  ( )
# 2º  **
# 3º  *  /  //  %
# 4º  +  -
