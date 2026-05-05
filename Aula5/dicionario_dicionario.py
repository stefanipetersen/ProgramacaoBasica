
#É possível adicionar um dicionário dentro do outro

contatos = {
    "Clark Kent":
        {"Celular": "123456",
         "Email": "super@krypton.com"},
    "Bruce Wayne":
        {"Celular": "654321",
         "Email": "bat@caverna.com"}
}

for itens in contatos.items():
    print(itens)

#Desempacotando os valores de dentro do dicionario
for nome, formas_contato in contatos.items():
    print(f"{nome}")
    for tipo, contato in formas_contato.items():
        print(f"{tipo}: {contato}")
    print("----------------------")