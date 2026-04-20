#Crie um programa onde o professor digite notas de uma quantidade indeterminado de alunos. Quando terminar, exibir a média aritmética.

notas = []

while input("Deseja inserir uma nota? S- Sim, N-Não ").upper() != "N":
    notas.append(float(input("Informe a nota: ")))

#A soma das notas dividido pela quantidade de notas
media_aritmetica = sum(notas) / len(notas)

print(f"Para as notas digitadas, a média foi de {media_aritmetica:.2f}")