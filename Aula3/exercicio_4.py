from math import factorial

minutos_atuais = int(input("Escreva os minutos atuais: "))
fatorial = minutos_atuais

for numero in range(1, minutos_atuais):
    fatorial = fatorial * numero

print(fatorial)
print(f"A senha é LIBERDADE{fatorial}")






