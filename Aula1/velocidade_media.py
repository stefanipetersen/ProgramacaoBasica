print("Calculo de velocidade media")

distancia = float(input("Digite a distancia percorrida: "))

tempo = float(input("Digite o tempo decorrido: "))

velocidade_media = distancia / tempo

#para deixar apenas dois numeros depois da virgula, coloca {:.2f}

print("A sua velocidade media foi de: {:.2f}km/h".format(velocidade_media))
print(f"A sua velocidade media foi de: {velocidade_media:.2f}km/h")

