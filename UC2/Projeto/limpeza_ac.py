import pandas as pd

# 1. LER CSV CORRETAMENTE
df = pd.read_csv('Covid_AC.csv', sep=';', encoding='latin1')

print("Total de linhas:", len(df))
print("\nColunas:")
print(df.columns)

# 2. LIMPAR NOMES DAS COLUNAS
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
)

print("\nColunas após limpeza:")
print(df.columns)

# 3. LIMPAR ESPAÇOS EM COLUNAS DE TEXTO
for col in df.select_dtypes(include=['object', 'string']).columns:
    df[col] = df[col].astype(str).str.strip()

# 4. CONVERTER DATAS
df['vacina_dataaplicacao'] = pd.to_datetime(
    df['vacina_dataaplicacao'],
    errors='coerce'
)

df['paciente_datanascimento'] = pd.to_datetime(
    df['paciente_datanascimento'],
    errors='coerce'
)

# 5. CONVERTER IDADE PRA NÚMERO
df['paciente_idade'] = pd.to_numeric(
    df['paciente_idade'],
    errors='coerce'
)

# 6. TRATAR VALORES NULOS

# Idade vazia vira 0
df['paciente_idade'] = df['paciente_idade'].fillna(0)

# Datas inválidas ficam marcadas
df['paciente_datanascimento'] = df['paciente_datanascimento'].fillna('Data inválida')
df['vacina_dataaplicacao'] = df['vacina_dataaplicacao'].fillna('Data inválida')

# Textos vazios ou nulos viram "Não informado"
for col in df.select_dtypes(include=['object', 'string']).columns:
    df[col] = df[col].replace('', 'Não informado')
    df[col] = df[col].fillna('Não informado')

# Tratamentos específicos
df['paciente_endereco_cep'] = df['paciente_endereco_cep'].replace('nan', '00000-000')
df['paciente_endereco_cep'] = df['paciente_endereco_cep'].fillna('00000-000')

df['vacina_categoria_nome'] = df['vacina_categoria_nome'].replace('nan', 'Não informada')
df['vacina_categoria_nome'] = df['vacina_categoria_nome'].fillna('Não informada')

df['sistema_origem'] = df['sistema_origem'].replace('nan', 'Desconhecido')
df['sistema_origem'] = df['sistema_origem'].fillna('Desconhecido')

# 7. MARCAR DUPLICADOS
df['is_duplicado'] = df.duplicated(keep=False)

# 8. VERIFICAR VALORES NULOS
print("\n--- VALORES NULOS APÓS LIMPEZA ---")
print(df.isnull().sum())

# 9. RESUMO ESTATÍSTICO
print("\n--- RESUMO GERAL ---")
print(df.describe(include='all'))

print("\n--- RESUMO DA IDADE ---")
print(df['paciente_idade'].describe())

# 10. SALVAR CSV LIMPO
df.to_csv('covid_ac_limpo.csv', index=False, encoding='utf-8')

print("\nArquivo limpo salvo com sucesso: covid_ac_limpo.csv")