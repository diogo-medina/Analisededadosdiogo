import time
# 1. DEFINIÇÃO da função

def dar_boas_vindas():
        
    print("-"*40)
    print(" Bem-vindo ao nosso aplicativo!")
    print("-"*40)


 # 2. CHAMADA da função
# O código abaixo só será executado se você "chamar" a função pelo nome:

print("Início do programa.")
print('por favor, aguarde...')
time.sleep(2)
dar_boas_vindas() # <-- Isso executa o código dentro da função
print("Meio do programa.")
dar_boas_vindas() # <-- Podemos chamar de novo!
print("Fim do programa.")



# 'nome_da_pessoa' é um PARÂMETRO.
# É uma variável que só existe dentro da função.
def boas_vindas_personalizado(nome_da_pessoa):
 print("-"*40)
 print(f"Olá, {nome_da_pessoa}! Seja bem-vindo(a)! ��")
 print("-"*40)
# Ao chamar a função, passamos o ARGUMENTO (o valor)
boas_vindas_personalizado("Maria")
boas_vindas_personalizado("João")

def somar (a,b):
    soma = a + b
    subtr= a - b
    return soma,subtr

import random # Sempre no topo do arquivo!
def gerar_dados(qtd, min_val, max_val):
 """
 Gera uma LISTA de números aleatórios.
 - qtd: quantos números queremos na lista
 - min_val: o valor mínimo (inclusivo)
 - max_val: o valor máximo (inclusivo)
 """
 
 # A estrutura a seguir se chama "List Comprehension".
 # É um jeito rápido de criar uma lista usando um loop.
#  lista_de_dados = [random.randint(min_val, max_val) for _ in range(qtd)] 
lista_de_dados=[]

for _ in range(qtd):
        numero= random.randint(min_val, max_val)
        lista_de_dados.append(numero)
        
 
return lista_de_dados

# Testando a função
dados_aleatorios = gerar_dados(10, 1, 100) # Gera 5 números entre 1 e 100
print(f"Dados gerados:  {dados_aleatorios}")

