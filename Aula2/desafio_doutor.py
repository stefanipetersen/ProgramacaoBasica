# O Doutor estabeleceu a regra com seus alunos:
# Quem tiver a nota maior que 8,5 na sua prova semestral serão convidados para uma visita de campo na América do Sul.
# O aluno precisa preencher o email e a nota, se a nota estiver correta a mensagem "ENVIANDO CONVITE" deve ser apresentada

email = input("Digite o seu email: ")
nota = (input("Digite sua nota: "))
nota = float(nota)

if nota > 8.5:
    print("ENVIADO CONVITE PARA O EMAIL {}".format(email))

else:
    print("Sua nota não alcança o valor mínimo")