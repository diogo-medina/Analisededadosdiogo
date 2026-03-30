import pandas as pd 

 
# Ler o arquivo Excel para um DataFrame 
df = pd.read_excel('base_invest.xlsx', sheet_name= 'Transacoes')
 
# Exibir as primeiras 5 linhas do DataFrame 
print(df.head()) # .tail imprime as ultimas