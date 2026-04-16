import pandas as pd
import numpy as np
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

def obter_dados_do_banco(query):
    try:
        conexao = mysql.connector.connect(
            host="localhost",
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

# Usando a função
query_produtos = "SELECT * FROM produtos WHERE preco > 100"
dados_filtrados = obter_dados_do_banco(query_produtos)

# if dados_filtrados:
#     for produto in dados_filtrados:
#         print(produto)

#####################


query_clientes = "SELECT * FROM clientes"
df_clientes = pd.DataFrame(obter_dados_do_banco(query_clientes),columns=['id_cliente', 'nome_clientes', 'email'])
# print(df_clientes)

query_produtos = "SELECT * FROM produtos"
df_produtos = pd.DataFrame(obter_dados_do_banco(query_produtos),columns=['id_produto', 'nome', 'categoria', 'preco','estoque'])

precos_array= df_produtos['preco'].to_numpy()


precos_array_final= np.array(precos_array).astype(float)
# print(precos_array_final)



## Continuando exatamente de onde paramos na aula passada (histograma), vamos calcular os quartis e verificar se a média está dentro da faixa interquartil (entre Q1 e Q3).

# media = np.mean(precos_array)
# mediana = np.median(precos_array)

# q1 = np.percentile(precos_array_final,25)
# q2 = np.percentile(precos_array_final, 50)
# q3 = np.percentile(precos_array_final, 75)

# print(f"\nPrimeiro Quartil (Q1): R$ {q1:.2f}")
# print(f"Segundo Quartil (Mediana/Q2): R$ {q2:.2f}")
# print(f"Terceiro Quartil (Q3): R$ {q3:.2f}")

# if q1 <= media <= q3:
#     print("\nA média está DENTRO da faixa interquartil (entre Q1 e Q3).")
# else:
#     print("\nA média está FORA da faixa interquartil (fora de Q1 e Q3).")

# plt.axvline(x=q1, color='green', linestyle='--', label=f'Q1: R$ {q1:.2f}')
# plt.axvline(x=q3, color='orange', linestyle='--', label=f'Q3: R$ {q3:.2f}')
# plt.axvline(x=media, color='red', linestyle='-', label=f'Média: R$ {media:.2f}')
# plt.axvline(x=mediana, color='purple', linestyle='-', label=f'Mediana: R$ {mediana:.2f}')
# plt.legend()
# plt.show()

# ##################################################

#Calcular Q1 e Q3
Q1 = np.percentile(precos_array_final, 25)
Q3 = np.percentile(precos_array_final, 75)

# Calcular IQR
IQR = Q3 - Q1

# Calcular Limites
limite_superior = Q3 + (1.5 * IQR)
limite_inferior = Q1 - (1.5 * IQR)

print(f"\n--- Limites de Outliers (Preços dos Produtos) ---")
print(f"Q1 (25%): R$ {Q1:.2f}")
print(f"Q3 (75%): R$ {Q3:.2f}")
print(f"IQR: R$ {IQR:.2f}")
print(f"Limite Superior (LS): R$ {limite_superior:.2f}")
print(f"Limite Inferior (LI): R$ {limite_inferior:.2f}")

# Identificação de Outliers Superiores e Inferiores
outliers_superiores = df_produtos[df_produtos['preco'] > limite_superior]
outliers_inferiores = df_produtos[df_produtos['preco'] < abs(limite_inferior)]

# Exibir Outliers Superiores Ordenados (Decrescente)
print(f"\n--- Outliers Superiores ({len(outliers_superiores)} produtos) ---")
print(outliers_superiores[['nome', 'preco']].sort_values(by='preco', ascending=False))

# Exibir Outliers Inferiores Ordenados (Crescente)
print(f"\n--- Outliers Inferiores ({len(outliers_inferiores)} produtos) ---")
print(outliers_inferiores[['nome', 'preco']].sort_values(by='preco', ascending=True))

# Garante que os DataFrames de outliers não estão vazios antes de plotar
if not outliers_inferiores.empty or not outliers_superiores.empty:
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6)) # 1 linha, 2 colunas
    
    # 1ª Posição: Outliers Inferiores (Crescente)
    axes[0].bar(outliers_inferiores['nome'], outliers_inferiores['preco'])
    axes[0].set_title('Outliers Inferiores (Preços Mais Baixos)')
    axes[0].set_ylabel('Preço (R$)')
    axes[0].tick_params(axis='x', rotation=45, labelsize=8)
    axes[0].grid(axis='y', linestyle='--')
    
    # 2ª Posição: Outliers Superiores (Decrescente)
    # Ordenamos novamente para garantir a visualização correta
    outliers_superiores_plot = outliers_superiores.sort_values(by='preco', ascending=False)
    axes[1].barh(outliers_superiores_plot['nome'], outliers_superiores_plot['preco'])
    axes[1].set_title('Outliers Superiores (Preços Mais Altos)')
    axes[1].set_ylabel('Preço (R$)')
    axes[1].tick_params(axis='x', rotation=45, labelsize=8)
    axes[1].grid(axis='y', linestyle='--')
    
    plt.tight_layout() # Ajusta automaticamente os parâmetros de subplot para dar preenchimento
    plt.show()

else:
    print("\nNão houve outliers superiores ou inferiores para plotar.")