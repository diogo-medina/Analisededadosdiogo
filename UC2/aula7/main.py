# Importe o seu módulo.
# Assumimos aqui que 'statistic.py' está no mesmo diretório.
import pandas as pd
import mysql.connector
from statistic import calcular_medidas_descritivas, gerar_painel_boxplot

# 1. Definir o caminho do arquivo
# Ajuste o caminho para onde o seu arquivo está
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

# 2. Carregar os dados
try:
    query_produtos= "SELECT preco FROM produtos"
    dados= obter_dados_do_banco(query_produtos)
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
    print(f"Erro: O arquivo {query_produtos} não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")