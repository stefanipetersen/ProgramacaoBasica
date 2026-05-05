#É possível fazer uma lista que contenha tuplas, é possível remover ou adicionar tuplas, mas os valores de dentro das tuplas não são modificáveis

inimigos = [(10, 5), (30, 3), (1, 50)]

while len(inimigos) > 0:
    x = int(input("Informe um valor para o eixo X: "))
    y = int(input("Informe um valor para o eixo Y: "))

    if (x, y) in inimigos:
        print("Você acertou um inimigo!")
        inimigos.remove((x, y))
    else:
        print("Você errou!")

    print(f"Agora restam {len(inimigos)} inimigos no mapa")


