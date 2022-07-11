import pandas as pd
import numpy as np
from sklearn import hmm


df_encceja_2020 = pd.read_csv(f"/home/alecy/Documents/datasets/microdados_encceja_2020/DADOS/MICRODADOS_ENCCEJA_NACIONAL_REGULAR_2020.csv", sep=",", encoding="latin-1", error_bad_lines=False, low_memory=False)

# Filtro por alunos que estiverem presentes na prova
df_encceja_2020 = df_encceja_2020.loc[df_encceja_2020["TP_PRESENCA_LC"] == 1]
df_encceja_2020 = df_encceja_2020.loc[df_encceja_2020["TP_PRESENCA_MT"] == 1]
df_encceja_2020 = df_encceja_2020.loc[df_encceja_2020["TP_PRESENCA_CN"] == 1]
df_encceja_2020 = df_encceja_2020.loc[df_encceja_2020["TP_PRESENCA_CH"] == 1]

# Filtro alunos que não tiveram problema com a redação
df_encceja_2020 = df_encceja_2020.loc[df_encceja_2020["TP_STATUS_REDACAO"] == 1]

# Eliminando colunas não necessárias
df_encceja_2020 = df_encceja_2020.drop([
    "TP_CERTIFICACAO", 
    "IN_PROVA_LC",
    "IN_PROVA_MT", 
    "IN_PROVA_CN", 
    "IN_PROVA_CH",
    "CO_PROVA_LC",
    "CO_PROVA_MT",
    "CO_PROVA_CN",
    "CO_PROVA_CH",
    "TX_RESPOSTAS_LC",
    "TX_RESPOSTAS_MT",
    "TX_RESPOSTAS_CN",
    "TX_RESPOSTAS_CH",
    "TX_GABARITO_LC",
    "TX_GABARITO_MT",
    "TX_GABARITO_CN",
    "TX_GABARITO_CH",
    "NU_NOTA_COMP1",
    "NU_NOTA_COMP2",
    "NU_NOTA_COMP3",
    "NU_NOTA_COMP4",
    "NU_NOTA_COMP5",
    "SG_UF_PROVA",
    "NO_ENTIDADE_CERTIFICADORA",
    "TP_PRESENCA_LC",
    "TP_PRESENCA_MT",
    "TP_PRESENCA_CN",
    "TP_PRESENCA_CH",
    "NU_ANO",
    "TP_STATUS_REDACAO",
], axis=1)

# Criar coluna de média
df_encceja_2020["MEDIA_NOTA"] = (df_encceja_2020["NU_NOTA_LC"] + df_encceja_2020["NU_NOTA_MT"] + df_encceja_2020["NU_NOTA_CN"] + df_encceja_2020["NU_NOTA_CH"] + df_encceja_2020["NU_NOTA_REDACAO"])/5

# Criar coluna de aprovação
df_encceja_2020["APROVADO"] = np.where((df_encceja_2020["IN_APROVADO_LC"] + df_encceja_2020["IN_APROVADO_MT"] + df_encceja_2020["IN_APROVADO_CN"] + df_encceja_2020["IN_APROVADO_CH"] == 4.0), 1, 0)

# Deletar colunas utilizadas para o cálculo
# Eliminando colunas não necessárias
df_encceja_2020 = df_encceja_2020.drop([
    "NU_NOTA_LC", 
    "NU_NOTA_MT",
    "NU_NOTA_CN", 
    "NU_NOTA_CH", 
    "NU_NOTA_REDACAO",
    "IN_APROVADO_LC",
    "IN_APROVADO_MT",
    "IN_APROVADO_CN",
    "IN_APROVADO_CH",
], axis=1)

for column in df_encceja_2020.columns:
    print(column, df_encceja_2020.dtypes[column])

print(df_encceja_2020.head(10))

# Substituir Nan por 0
df_encceja_2020 = df_encceja_2020.fillna("Q")

print(df_encceja_2020.head(10))


# Convertendo colunas de letras para números
for column in df_encceja_2020.columns:
    if df_encceja_2020.dtypes[column] == "object":
        df_encceja_2020[column] = [ ord(x) for x in df_encceja_2020[column] ]

print(df_encceja_2020.head(10))