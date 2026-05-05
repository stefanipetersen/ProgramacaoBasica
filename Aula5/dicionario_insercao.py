#Para inserir dados use .update({})
dicionario = {}

dicionario['André David'] = 'Professor'

print(dicionario)

dicionario.update({"Juquinha": "Professor"})
print(dicionario)

funcionarios = {}

while input("Quer inserir um funcionário? S-Sim, N-Não").upper() != "N":
    nome = input("Informe o nome do funcionário: ")
    funcao = input("Informe a função do funcionário: ")
    funcionarios.update({nome: funcao})

#Se vc adicionar o nome duas vezes, mas com funções diferentes, o sistema vai deixar o mesmo nome com a ultima função

print(funcionarios)