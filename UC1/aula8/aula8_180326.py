

# # # lista01=[100, 'cem', '%$', 2039.323, True, None,]
# # # #           [0]    [1] [2]  [3] ...
# # # for i in lista01:
# # #     print(i,':',type(i))

# # # nomes_att=[ 'daniela correia', 'luciene silva','rafael fernandes']
# # # dani=nomes_att[0][8:]
# # # luciene=nomes_att[1][8:]
# # # rafael=nomes_att[2][7:]
# # # sobrenomes=[]



# # # # for i  in nomes_att:
# # # #     for j in nomes_att[0]:
# # # #         sobrenomes.append(nomes_att)
# # # # print(sobrenomes)
# # # nome4='miguel'
# # # nome5='luciene'
# # # nomes_att.insert(2,nome4)
# # # nomes_att.append(nome5)
# # # nomes_att.append(nome5)
# # # #nomes_att.remove('luciene')
# # # print(nomes_att.index('luciene'))
# # # #nomezinhos=nomes_att.copy()
# # # nomes_att.clear()
# # # print(nomes_att)





# # ## TUPLAS ###

# pares=(40,20,2,18,14,34,96,30,20,58)
# # print(pares[3])
# # print(pares[3:])
# # print(pares[3:8])
# # print(len(pares))
# # pares=pares+(44,)
# # print(pares)
# lista_pares=list(pares)
# print(lista_pares)
# lista_pares.append(102)
# lista_pares.sort()
# lista_pares=tuple(lista_pares)
# print(lista_pares)

# ### SETS ###
# impares={33,5,17,11,27,11,71,79,99,15}
# print(impares)
# print(type(impares))
# impares_02={11,3,23,83,15,73}
# intersecao=impares.intersection(impares_02)
# print(intersecao)

# filme={
#     'nome':'V for Vendetta',
#     'ano': 2005,
#     'genero':'Ação', #Thriller/Drama
#     'faixa_etaria':16
# }
# print(filme)
# print(type(filme))

# print(filme.keys())
# print(filme.values())
# print(len(filme))

# filme['duracao']='130min'
# filme['genero']='Thriller/Drama'
# filme['genero']=None



'''Vamos desenvolver um programa que leia 5 nomes de filmes e armazene nas quatro 
formas, mostrando as diferenças na prática. '''
#Coleta dos Dados: 
dados_entrada = [] 
print("Digite 5 nomes de filmes:") 
for i in range(5): 
    nome = input(f"Filme {i+1}: ") 
    dados_entrada.append(nome) # Usando LISTA para coletar os dados 
     
print("-" * 30) 
 
#Armazenamento e Exibição: 
# 1. LISTA: 
lista_filmes = dados_entrada
print(lista_filmes) 
 
# 2. TUPLA: 
tupla_filmes = tuple(dados_entrada) 
print(tupla_filmes)
# 3. SET:  
set_filmes = set(dados_entrada) 
print(set_filmes)
# 4. DICIONÁRIO: Usando o índice como chave (ex: 1: 'Filme A') 
dicionario_filmes = {} 
for i in range(len(dados_entrada)): # Repetição pelo tamanho da lista 
    # Usando o índice (i+1) como CHAVE e o nome como VALOR 
    dicionario_filmes[i + 1] = dados_entrada[i]  
 
print(f"LISTA (Flexível): {lista_filmes}") 
print(f"TUPLA (Fixa): {tupla_filmes}") 
print(f"SET (Apenas Únicos): {set_filmes}") 
print(f"DICIONÁRIO (Chave: Valor): {dicionario_filmes}")
