resposta = ""
tentativas = 0

while resposta != "42":
    resposta = input("Qual é a resposta da vida, do universo e tudo mais?")
    tentativas = tentativas + 1

print("Você acertou!\nQue incrível!")
print(f"Você utilizou {tentativas} tentativas")

