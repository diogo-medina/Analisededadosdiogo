"""
Desafios (ugprade):
Média Escolar para 5 Estudantes
Use um for loop para iterar 5 vezes. Dentro do loop, realize a leitura das notas e a decisão
(if/elif/else) da média. Crie uma lista vazia (resultados = []). A cada repetição, adicione uma
string (ex: "Aluno 1 - Aprovado") a esta lista usando .append().
"""

# resultados = []

# for i in range(5):
#     nota1 = float(input("Digite a nota da primeira avaliação: "))
#     nota2 = float(input("Digite a nota da segunda avaliação: "))
#     media = (nota1 + nota2) / 2
#     print(f"A média do Aluno é: {media}")

#     if media >= 6:
#         status = "Aprovado"
#     elif media >= 3:
#         status = "Em recuperação"
#     else:
#         status = "Reprovado"

#     resultados.append(f"Aluno {i+1} - {status}")

# print("\nResultados finais:")
# for r in resultados:
#     print(r)

'''
Cadastro Seletivo de Candidatos
Use um for loop para iterar 5 vezes. Dentro do loop, use um if/else para checar se o
candidato é menor de 18 anos (rejeição). Crie uma lista principal: candidatos_validos = [].
Se o candidato for válido, crie um Dicionário (ex: candidato = {'nome': '...', 'email': '...'}).
Adicione este Dicionário à lista: candidatos_validos.append(candidato)
'''
candidatos_validos = []
ano_atual= 2026

for i in range (5):
     print("\nCandidato", i)
     nome = input("Digite o nome: ")
     ano_nascimento = int(input("Digite o ano de nascimento: "))
     idade = ano_atual - ano_nascimento

     if idade < 18:
            print("Candidato menor de 18 anos. Não pode participar.")
            continue
           
     telefone = input("Digite o telefone: ")
     email = input("Digite o email: ")
     candidato = {'nome': nome, 'idade': idade, 'telefone': telefone, 'email': email}
     candidatos_validos.append(candidato)


print("\nResultados finais:")
for r in candidatos_validos:
    print(r)