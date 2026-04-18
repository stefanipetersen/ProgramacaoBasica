
transacoes_diarias = int(input("Quantas transações você realizou ao longo do seu dia? "))

gasto_total = 0

for transacoes in range(1, transacoes_diarias +1, 1):
    valor_transacoes = float(input("Qual o valor da sua {}ª transação: ".format(transacoes)))
    gasto_total = gasto_total + valor_transacoes

media = gasto_total / transacoes_diarias

print("O valor total de gastos de hoje foi de: R${}\nA média gasta foi de R${}".format(gasto_total, media))