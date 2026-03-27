
# carro=False
# combustivel=False

# if not carro and not combustivel:
#     print("Meu fusquinha está rodando.")
# else:
#     print("nao sobrou nada pro fusquinha.")


# print('*'*15)



# if not carro and not combustivel:
#     print("Meu fusquinha está rodando.")
# elif carro==False or combustivel==False:
#     print("não sobrou nada pro fusquinha.")
# else:
#     print('erro de execução.')

# melhorando codigo com match case

# semana = 3

# if semana == 1:
#  print("Domingo")
# elif semana == 2:
#  print("Segunda-feira")
# elif semana == 3:
#  print("Terça-feira")
# elif semana == 4:
#  print("Quarta-feira")
# elif semana == 5:
#  print("Quinta-feira")
# elif semana == 6:
#  print("Sexta-feira")
# elif semana == 7:
#  print("Sábado")
# else: # O 'else' funciona como o 'default'
#  print("Dia inválido")


# semana = int(input("informe o dia da semana:"))
# if semana == 1:
#  print("Domingo")
# elif semana == 2:
#  print("Segunda-feira")
# elif semana == 3:
#  print("Terça-feira")
# elif semana == 4:
#  print("Quarta-feira")
# elif semana == 5:
#  print("Quinta-feira")
# elif semana == 6:
#  print("Sexta-feira")
# elif semana == 7:
#  print("Sábado")
# else: # O 'else' funciona como o 'default'
#  print("Dia inválido")

# mes = int(input("informe o mes:"))

# match mes:
#     case 1:
#         print("janeiro")
#     case 2:
#         print("fevereiro")
#     case 3:
#         print("março")
#     case 6:
#         print("junho")
#     case _:
#         print("mês invalído")

# try:
#  numero_mes = int(input("Digite um número de 1 a 12: "))
#  match numero_mes:
#     case 1:
#         print("O número 1 corresponde a Janeiro.")
#     case 12:
#         print("O número 12 corresponde a Dezembro.")
#     case _:
#         print(f"Número {numero_mes} inválido. Digite entre 1 e 12.")

# except ValueError:
#      print("Entrada inválida. Por favor, digite um número inteiro.")

     
try:
 nome_mes = int(input("digite um numero de 1 a 12:"))
 match nome_mes:
    case 1:
        print("janeiro")
    case 2:
        print("fevereiro")
    case 3: 
        print("março")
    case 4:
        print("abril")
    case 5:
        print("maio")
    case 6:
        print("junho")
    case 7:
        print("julho")
    case 8: 
        print("agosto")
    case 9:
        print("setembro")
    case 10:
        print("outubro")
    case 11:
        print("novembro")
    case 12:
        print("dezembro")
    case _: 
        print(" mes invalido ")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")



