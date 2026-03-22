# """ Controle de Pesca
# Crie um programa que ajude um pescador a controlar sua produtividade. Toda vez que ele
# traz um peso de peixes maior que o estabelecido pelo regulamento (100 quilos), ele deve
# pagar uma multa de R$ 4,00 por quilo excedente.
# ● O programa deve ler o peso de peixes (em quilos) pescado no dia.
# ● Você deve criar uma função (ex: calcular_multa(peso_total)) que recebe o peso e
# retorna o valor da multa (que pode ser 0.0 se estiver dentro do limite).
# ● Se o valor da multa retornado for maior que zero, mostre a multa.
# ● Caso contrário, mostre a mensagem "Peso dentro do limite. Nenhuma multa a
# pagar."
# ● Pergunte o peso de várias pescarias feitas ao longo da semana. O loop para quando
# o usuário digitar 0. Ao final, mostre o total de multa acumulado no dia.
# """


# def calcular_multa(peso_total):
#     if peso_total > 100:
#         excesso = peso_total - 100
#         return excesso * 4 
#     else:
#         return 0.0


# total_acumulado = 0
# peso = -1  


# while peso != 0:
#     print("-" * 30)
#     peso = float(input("Digite o peso da pescaria em kg (ou 0 para encerrar): "))

#     if peso == 0:
#         break  

    
#     multa_atual = calcular_multa(peso)

    
#     if multa_atual > 0:
#         print(f"⚠️ Atenção! Peso excedido. Multa: R$ {multa_atual:.2f}")
#     else:
#         print("✅ Peso dentro do limite. Nenhuma multa a pagar.")

    
#     total_acumulado += multa_atual

# print("-" * 30)
# print(f"💰 TOTAL DE MULTAS ACUMULADO NO DIA: R$ {total_acumulado:.2f}")

# """"
# Calculadora de IMC
# Crie um programa que leia a altura e o peso de N pessoas (pergunte ao usuário quantas
# pessoas são). Para cada pessoa, mostre seu IMC e a classificação.
# ● Fórmula: IMC = PESO / (ALTURA * ALTURA)
# ● Obrigatório (Função 1): Crie uma função calcular_imc(peso, altura) que receberá
# os valores e retornará o IMC calculado.
# ● Obrigatório (Função 2): Crie outra função obter_classificacao(imc) que recebe o
# valor do IMC (calculado pela função 1) e retorna uma string com a classificação.
# ○ Valores de Referência:
# ■ Menor que 18.5: "Abaixo do peso"
# ■ 18.5 a 24.9: "Peso normal"
# ■ 25.0 a 29.9: "Sobrepeso"
# ■ 30.0 ou mais: "Obesidade"
# ● O programa principal deve pedir N, fazer um loop N vezes, pedir peso e altura,
# chamar as duas funções e imprimir o resultado formatado.
# """""

# def calcular_imc(peso, altura):
#     imc = peso / (altura * altura)
#     return imc

# def obter_classificacao(imc):
#     if imc < 18.5:
#         return "Abaixo do peso"
#     elif imc >= 18.5 and imc <= 24.9:
#         return "Peso normal"
#     elif imc >= 25.0 and imc <= 29.9:
#         return "Sobrepeso"
#     else:
#         return "Obesidade"

# n = int(input("Quantas pessoas deseja avaliar? "))

# for i in range(n):
#     print(f"\n--- Dados da {i+1}ª pessoa ---")
    
#     p = float(input("Digite o peso (kg): "))
#     a = float(input("Digite a altura (m): "))
#     meu_imc = calcular_imc(p, a)

#     minha_classe = obter_classificacao(meu_imc)
    
#     print(f"IMC: {meu_imc:.2f} | Classificação: {minha_classe}")

# print("\nPrograma finalizado!")

"""
Conversor de Temperatura
Crie um programa que permita ao usuário converter temperaturas entre Celsius e
Fahrenheit.
● Função 1: Crie uma função celsius_para_fahrenheit(temp_c) que recebe a
temperatura em Celsius e retorna o valor em Fahrenheit.
○ Fórmula: F = (C * 9/5) + 32
● Função 2: Crie uma função fahrenheit_para_celsius(temp_f) que recebe a
temperatura em Fahrenheit e retorna o valor em Celsius.
○ Fórmula: C = (F - 32) * 5/9
● O programa principal deve perguntar ao usuário qual conversão ele quer fazer (ex:
"1 para C->F" ou "2 para F->C"), pedir o valor, chamar a função correta e mostrar o
resultado.
Desafio: Criar uma única função que faça qualquer uma das conversões,
sempre perguntando ao usuário qual é desejada
"""

# def celsius_para_fahrenheit(temp_c):
#     fahrenheit = (temp_c * 9/5) + 32
#     return fahrenheit

# def fahrenheit_para_celsius(temp_f):
#     celsius= ( temp_f - 32) * 5/9
#     return celsius

# opcao = int(input("Digite 1 para C->F ou 2 para F->C:"))

# temperatura = float(input(" digite a temperatura:"))
# if opcao == 1:
#      resultado = celsius_para_fahrenheit(temperatura)
#      unidade = "°F"
# else:
#      resultado = fahrenheit_para_celsius(temperatura)
#      unidade = "°C"
     

    
# print(f"O resultado é: {resultado:.2f}{unidade}") 



# def conversor():
#     print("Digite 1 para C->F ou 2 para F->C")
#     opcao = int(input("Digite a opção: "))
#     temperatura = float(input("Digite a temperatura: "))

#     if opcao == 1:
#         resultado = (temperatura * 9/5) + 32
#         unidade = "°F"
#     else:
#         resultado = (temperatura - 32) * 5/9
#         unidade = "°C"

#     print(f"O resultado é: {resultado:.2f}{unidade}") 



# conversor()

"""
Verificador de Ano Bissexto
Crie uma função chamada eh_bissexto(ano):
● A função deve receber um ano (inteiro) como parâmetro.
● Ela deve retornar True (Booleano) se o ano for bissexto, e False caso contrário.
● Regras do ano bissexto: É divisível por 4, exceto para anos divisíveis por 100, a
menos que sejam também divisíveis por 400. (Ex: 2000 e 2400 são bissextos; 1900
e 2100 não são).
● No programa principal, peça um ano ao usuário e imprima "O ano X É bissexto" ou
"O ano X NÃO é bissexto", baseado no retorno da função.
"""

# def eh_bissexto(ano):
    
#     if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#         return True
#     else:
#         return False
    
# ano = int(input("Digite um ano: "))

# if eh_bissexto(ano):
#     print(f"O ano {ano} É bissexto")
# else:
#     print(f"O ano {ano} NÃO é bissexto")
"""
Contagem de Caracteres
Crie uma função chamada contar_caractere(texto, caractere_procurado):
● A função deve receber uma string texto e uma string caractere_procurado (de um só
caractere).
● Ela deve retornar o número de vezes que o caractere_procurado aparece no texto.
(Não diferencie maiúsculas de minúsculas!)
● Dica: Use um loop for para percorrer o texto e use .lower() para tratar os caracteres.
● No programa principal, peça ao usuário uma frase e uma letra, e mostre o resultado
da contagem.
"""

# def contar_caractere(texto, caractere_procurado):
#     contagem=0

#     for letra in texto:
#         if letra.lower() == caractere_procurado.lower():
#             contagem += 1
#     return contagem

# frase= input("digite uma frase:")
# letra= input(" Digite uma letra que deseja contar :")

# quantidade= contar_caractere(frase, letra)
# print(f" A letra '{letra}' aparece {quantidade}  vez(es) na frase ")

"""
 Simulador de Dado
Usando o módulo random, crie uma função rolar_dado(lados).
● A função deve receber o número de lados do dado (ex: 6, 10, 20).
● Ela deve retornar um número aleatório entre 1 e o número de lados (use
random.randint(1, lados)).
● No programa principal, crie um "simulador de batalha":
○ Peça ao usuário para "Rolar para o Ataque (d20)". Chame a função
rolar_dado(20).
○ Peça ao usuário para "Rolar para o Dano (d8)". Chame a função
rolar_dado(8).
○ Imprima os resultados de cada rolagem
"""

# import random

# def rolar_dado(lados):
#     return random.randint(1, lados)

# input("Rolar para o Ataque (d20). Pressione Enter...")
# ataque = rolar_dado(20)
# print(f"Resultado do Ataque: {ataque}")

# input("Rolar para o Dano (d8). Pressione Enter...")
# dano = rolar_dado(8)
# print(f"Resultado do Dano: {dano}")



