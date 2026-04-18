# Operador Lógico: OR
# Durante o aniversário de sua fundação, uma loja está presenteando clientes da seguinte forma:
# Todas as compras no valor superior à R$1000,00 receberão um desconto de 10%
# Clientes selecionados receberam o cupom FESTA, que também gera 10% de desconto na hora da compra, não importando o valor
# Os descontos não serão acumulativos
# Escreva um script em python que receba um cupom e o valor de uma compra do usuário e informe o valor da compra

gasto = float(input("Digite a quantidade gasta: "))
cupom = input("Se tiver digite seu cupom: ")

if gasto >= 1000 or cupom.upper() == "FESTA":
    gasto = int(gasto) * 0.9
    print("Você ganhou 10% de desconto, o seu novo valor de compra é de:" + str(f"{gasto:.2f}"))

else:
    print("Você não possui nenhum desconto")