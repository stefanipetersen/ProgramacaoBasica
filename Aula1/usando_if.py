
#Criar um programa que receba o RM e a idade de um aluno, e exiba uma mensagem confirmando o cadastro apenas caso o estudante seja maior de idade. Caso o aluno menor de idade contenha autorizacao dos pais ele pode partipar.

rm = input("Digite seu RM: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Seu cadastro foi realizado com sucesso, aluno RM {}".format(rm))
else:
    autorizacao = input("Você tem autorizacao dos seus pais? S-SIM, N-NÃO")
    if autorizacao == "S":
        print("Seu cadastro foi realizado com sucesso, aluno RM {}".format(rm))
        print("Será enviado um email aos seus responsáveis")
    else:
        print("Você não tem idade minima para participar")