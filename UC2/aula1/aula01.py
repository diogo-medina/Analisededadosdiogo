import pandas as pd 

 
# # # Ler o arquivo Excel para um DataFrame 
# # df = pd.read_excel('base_invest.xlsx', sheet_name= 'Transacoes')
 
# # # Exibir as primeiras 5 linhas do DataFrame 
# # print(df.head()) # .tail imprime as ultimas


# # import pandas as pd
# # idades_lista = [25, 30, 22, 28]
# # idades_series = pd.Series([25, 30, 22, 28])
# # print(f"Lista:\n{idades_lista}\n")
# # print(f"Series:\n{idades_series}")

# notas = pd.Series([9.5, 8.0, 7.5, 9.0], index=['João', 'Maria', 'Pedro', 'Ana'])
# print(notas)


# Daqui, podemos realizar consultas mais específicas:
# print(notas['Maria']) # Acessando a nota de Maria
# print(notas['Pedro']) # Acessando a nota de Pedro
# print(notas.mean()) # Calculando a média das notas
# print(notas.median()) # calcula medinana
# print(notas.mode())  # calcula a moda
# print(notas[notas > 8]) # Filtrando notas maiores que 8
# print(notas.describe()) # Estatísticas descritivas das notas

# # Aumentar todas as notas em 10%
# notas_ajustadas = notas * 1.10
# print(notas_ajustadas)


# # Criar uma segunda Series para comparar
# notas_exame_final = pd.Series([10.0, 7.5, 8.0, 9.5], index=['João', 'Maria', 'Pedro', 'Ana'])
# # Calcular a diferença entre as notas
# diferenca = abs(notas_exame_final - notas_ajustadas)
# print(diferenca)

'''
Atividade Prática
Você recebeu um conjunto de dados de uma empresa de tecnologia voltada para aplicações
de investimentos. O objetivo é responder algumas perguntas importantes:
● Quais são as máximas e mínimas de operação de compra e venda das transações?
● Qual CNPJ tem o ativo de maior valor?
● Qual valor total em transações de cada participante?
Usando os conceitos de DataFrame e os comandos que aprendemos, crie um script que
carregue os dados e responda a essas perguntas
'''
df_transacoes= pd.read_excel('base_invest.xlsx', sheet_name=0)
compra=df_transacoes[df_transacoes['operacao'] == 'compra']
venda=df_transacoes[df_transacoes['operacao'] == 'venda']
print("\n",compra)
print("\n",venda)
print("\n",compra.min())
print("\n",compra.max())
print("\n",venda.min())
print("\n",venda.max())

max_compra_preco = compra['preco'].max()
min_compra_preco = compra['preco'].min()
max_venda_preco = venda['preco'].max()
min_venda_preco = venda['preco'].min()

print("--- Preços máximos e mínimos das operações ---")
print(f"Preço máximo de compra: {max_compra_preco}")
print(f"Preço mínimo de compra: {min_compra_preco}")
print(f"Preço máximo de venda: {max_venda_preco}")
print(f"Preço mínimo de venda: {min_venda_preco}")
print("\n")

df_preco= pd.read_excel('base_invest.xlsx', sheet_name=1)
df_ativo= pd.read_excel('base_invest.xlsx', sheet_name=2)


df_transacoes['valor_total']= df_transacoes['quantidade'] * df_transacoes['preco']

valor_por_ativo= df_transacoes.groupby('id_ativo')['valor_total'].sum()
print("\n",valor_por_ativo)

id_ativo_maior_valor= valor_por_ativo.idxmax()
cnpj_maior_valor= df_ativo[df_ativo['id_ativo']== id_ativo_maior_valor]['cnpj'].iloc[0]
print(f"\n o cnpj de maior valor é:{cnpj_maior_valor}")















