import pandas as pd
import numpy as np
import mysql.connector



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
print(precos_array_final)


# df_pedidos = pd.read_csv('C:\\Users\\diogo.durao\\Documents\\cursobigdata\\Analisededadosdiogo\\UC2\\aula5',sep=',',encoding='utf-8')
# print(df_pedidos)

# # Relacionando os DataFrames pela coluna 'id_cliente'
# df_relacionado = pd.merge(df_clientes, df_pedidos, on='id_cliente', how='inner')

# print(df_relacionado)


# Calcule a média:
media = np.mean(precos_array)
print(f"Média dos preços: R$ {media:.2f}")


# Obtenha a mediana:
mediana = np.median(precos_array)
print(f"Mediana dos preços: R$ {mediana:.2f}")


# Calcule a distância entre a média e a mediana:
distancia = (media - mediana) / mediana
print(f"Distância entre a média e a mediana: {distancia * 100:.2f}%")

if abs(distancia) <= 0.10:
    print("A média tende a ser uma medida de tendência central confiável.")
elif abs(distancia) < 0.25:
    print("A média pode estar sofrendo uma influência moderada de valores extremos.")
else:
    print("A média tende a não ser uma medida de tendência central confiável.")

# Verificando a direção da influência
if media > mediana:
    print("A influência é dos valores mais altos da distribuição.")
elif media < mediana:
    print("A influência é dos valores mais baixos da distribuição.")

# Visualizando a distribuição dos preços
import matplotlib.pyplot as plt  # Importando a biblioteca Matplotlib
import seaborn as sns  # Importando a biblioteca Seaborn    

sns.histplot(precos_array, kde=True) # kde=True adiciona a curva de densidade, traduzindo seria "Kernel Density Estimate"
plt.title('Distribuição dos Preços dos Produtos')
plt.show()  