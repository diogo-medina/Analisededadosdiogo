#listas:

#indices  0 ou-5   1 ou -4  2 ou -3  3 ou -4  4 ou -5
nome= [' matheus', 'alice', 'caio','larissa','diogo']

print(nome[4]) # [] usa para chamar o nome, sem precisar chamar todos


# LISTAS:

nome = ['Matheus','Alice','Caio','Larissa','Miguel','Rafael']

nome1 = nome[0]

print(nome[-1])
print(nome[-2])
print(nome[-3])
print(nome[-4])
print(nome1)

primeira_parte=nome[0:3]
print(primeira_parte)
segunda_parte=nome[3:6]
print(segunda_parte)

print(len(nome))


#TUPLAS:
nomes_tupla=tuple(nome)
print(nomes_tupla)
#SETS:
nomes_set=set(nome)
print(nomes_set)
#DICIONÁRIOS:
nomes_dict={1:'Matheus',
            2: 'Alice',
            3: 'Caio',
            4: 'Larissa',
            5:'Miguel',
            6: 'Rafael'}
            

