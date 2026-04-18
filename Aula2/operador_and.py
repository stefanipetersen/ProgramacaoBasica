
# Operador Lógico: AND
#Para acessar um sistema, o usuário deve digitar o username darth_vader e a senha 1138
# Crie um script que receba e valide estas informações de acesso

# Para ajustar as letras do usuário em maiúscula ou miníscula basta colocar o .lower() na variável do usuário

username = input("Digite o seu nome de usuário: ")
senha = input("Digite sua senha: ")

if username.lower() == "darth_vader" and senha == "1138":
    print("Login realiado com sucesso")

else:
    print("Login não autorizado")

