#>>>>>>>>>>>>>>> SCRIPT AULA (SKEW/KURTOSIS) <<<<<<<<<<<<<<<<<<<<

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import mysql.connector
from statistic import calcular_medidas_descritivas, gerar_painel_boxplot

### NA PRÁTICA ###

def obter_dados_do_banco(query):
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="vendas_online"
        )
        cursor = conexao.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()


query_pedidos = "SELECT * FROM Pedidos"
df_pedidos = pd.DataFrame(obter_dados_do_banco(query_pedidos),
                            columns=['id_pedido', 'id_cliente','data_pedido', 'valor_total', 
                                     'id_produto', 'quantidade'])

precos_pedidos_array = df_pedidos['valor_total'].to_numpy()

precos_pedidos_array_final = np.array(precos_pedidos_array).astype(float)
print(precos_pedidos_array_final)

### ASSIMETRIA ###

# precos_pedidos_array_final = pedidos_df['valor_total']

# 1. Calcular Assimetria
precos_pedidos_serie = pd.Series(precos_pedidos_array_final)
assimetria = precos_pedidos_serie.skew()
print(f"Assimetria dos Valores Totais: {assimetria:.4f}")

# 2. Relembrar Média e Mediana para contextualizar
media = precos_pedidos_serie.mean()
mediana = precos_pedidos_serie.median()
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")

# 3. Análise da Assimetria
if assimetria >= -0.5 and assimetria <= 0.5:
    analise_assimetria = "Simétrica (ou Quase Simétrica). Média e Mediana são próximas."
elif assimetria > 0.5:
    analise_assimetria = "Positiva. A cauda se estende para a direita (valores maiores). Média > Mediana."
else:
    analise_assimetria = "Negativa. A cauda se estende para a esquerda (valores menores). Média < Mediana."

print(f"\nConclusão da Assimetria: {analise_assimetria}")

### CURTOSE ###

# 1. Calcular Curtose
curtose_excesso = precos_pedidos_serie.kurtosis()

# 2. Calcular a Curtose Real
curtose_real = curtose_excesso + 3
print(f"Curtose em Excesso (Pandas): {curtose_excesso:.4f}")
print(f"Curtose Real (Referência 3.0): {curtose_real:.4f}")

# 3. Análise da Curtose
if curtose_real >= 2.5 and curtose_real <= 3.5:
    analise_curtose = "Mesocúrtica. Distribuição próxima da normal (dados uniformes no entorno da média)."
elif curtose_real < 2.5:
    analise_curtose = "Platicúrtica. Dados mais dispersos em relação à média. Caudas finas e Outliers comuns."
else: # curtose_real > 3.5
    analise_curtose = "Leptocúrtica. Dados extremamente concentrados no centro e caudas pesadas. Outliers muito comuns."

print(f"\nConclusão da Curtose: {analise_curtose}")

try:
    query_pedidos = "SELECT * FROM Pedidos"
    dados= obter_dados_do_banco( query_pedidos)
    df= pd.DataFrame(dados, columns=['preco'])
    
    # 3. Preparar o array para a análise
    precos_array_final = df['preco'].astype(float).values
    
    # 4. Chamar a função de cálculo do seu módulo
    medidas_calculadas = calcular_medidas_descritivas(precos_array_final)
    
    # 5. Chamar a função de visualização do seu módulo
    if medidas_calculadas:
        gerar_painel_boxplot(
            precos_array_final, 
            medidas_calculadas, 
            titulo_boxplot='Boxplot de Preços (vendas_produtos.csv)', 
            caminho_salvar='Relatorio_Precos.png'
        )

except FileNotFoundError:
    print(f"Erro: O arquivo {precos_pedidos_array_final} não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")