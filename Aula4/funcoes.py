#No Pycharm usamos def para as funções
def velocidade_media():
    distancia = float(input("Por favor, informe a distância em km: "))
    tempo = float(input("Por favor, informe a tempo em minutos: "))
    vm = distancia / tempo

    #O return é usado para quando o valor final da função vai ser utilizado em outras funções, métodos, loops, etc. Caso ele for chamado é preciso ter o return para o resultado da função ser armazenado e passado em diante.
    return vm

    #O print é apenas algo visual para sabermos o resultado
    print(f"A velocidade média foi de {vm:.2f} km/h")

#Sempre precisa chamar a função, sem chamar ela n vai ser executada
velocidade_media()

def velocidade_media_2(distancia, tempo):
    vm2 = distancia / tempo
    return vm2

velocidades_medias = []
for dia in ["segunda", "terça", "quarta", "quinta", "sexta"]:
    dist = float(input(f"Insira a distancia percorrida na {dia}: "))
    temp = float(input(f"Insira o tempo da viagem em horas: "))
    velocidades_medias.append(velocidade_media_2(dist, temp))

print(f"As velocidades médias da semana foram {velocidades_medias}")

