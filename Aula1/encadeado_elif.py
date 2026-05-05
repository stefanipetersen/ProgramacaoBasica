
#Uma empresa de telefonia está realizando uma promoção, onde os clientes podem receber bônus para navegação na internet com base em uma pontução.
# 1000 pontos -> 3gb de bônus
# 500 pontos -> 1,5gb de bônus
# 200 pontos -> 500mb de bônus
# Crie um programa que receba o número de pontos e informe ao cliente quantos bônus ele receberá.

pontuacao = int(input("Informe a pontuacao do usuário: "))

if pontuacao > 1000:
    print("Parabéns! Você ganhou 3gb de bônus!")
elif pontuacao >= 500:
    print("Parabéns! Você ganhou 1,5gb de bônus!")
elif pontuacao >= 200:
    print("Parabéns! Você ganhou 500mb de bônus!")

else:
    print("Infelizmente você não possui nenhum bônus")