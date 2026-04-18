alimentos_consumidos = int(input("Digite a quantidade de alimentos consumidos hoje: "))

total_calorias = 0

for alimento in range(1, alimentos_consumidos + 1, 1):
    caloria = int(input("Informe a quantidade de calorias do seu {}º alimento: ".format(alimento)))
    total_calorias = total_calorias + caloria

print("Foram consumidas {} calorias ao longo do seu dia".format(total_calorias))
