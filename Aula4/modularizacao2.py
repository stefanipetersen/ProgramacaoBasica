# Quando vamos chamar uma função que está em outro arquivo precisamos utilizar o import + o nome do arquivo que está contido a função desejada

import modularizacao1

# Para acionar a função desejada, nome do arquivo + . + nome da função + valores para a função
print(modularizacao1.somar(2,3))

# Um outro jeito de chamar a função específica que vc deseja é colocando from + nome do arquivo + import + nome da função

from modularizacao1 import subtrair, multiplicar

print(subtrair(6,3))
