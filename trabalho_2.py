import pandas as pd

# df_censo_2019 = pd.read_csv(f"microdados_censo_escolar_2019/2019/dados/microdados_ed_basica_2019.csv", sep=";", encoding="latin-1", error_bad_lines=False, low_memory=False)
# df_censo_2020 = pd.read_csv(f"microdados_censo_escolar_2020/2020/dados/microdados_ed_basica_2020.CSV", sep=";", encoding="latin-1", error_bad_lines=False, low_memory=False)
# df_censo_2021 = pd.read_csv(f"microdados_censo_escolar_2021/2021/dados/microdados_ed_basica_2021.csv", sep=";", encoding="latin-1", error_bad_lines=False, low_memory=False)
df_encceja_2020 = pd.read_csv(f"/home/alecy/Documents/datasets/microdados_encceja_2020/DADOS/MICRODADOS_ENCCEJA_NACIONAL_PPL_2020.csv", sep=",", encoding="latin-1", error_bad_lines=False, low_memory=False)

# Filtro por alunos que estiverem presentes na prova
df_encceja_2020.loc[df_encceja_2020["TP_PRESENCA_LC"] == 1]
df_encceja_2020.loc[df_encceja_2020["TP_PRESENCA_MT"] == 1]
df_encceja_2020.loc[df_encceja_2020["TP_PRESENCA_CN"] == 1]
df_encceja_2020.loc[df_encceja_2020["TP_PRESENCA_CH"] == 1]

# Filtro alunos que não tiveram problema com a redação
df_encceja_2020.loc[df_encceja_2020["TP_STATUS_REDACAO"] == 1]

# Eliminando colunas não necessárias
df_encceja_2020 = df_encceja_2020.drop([
    "TP_CERTIFICACAO", 
    "TP_FAIXA_ETARIA", 
    "TP_SEXO", 
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
], axis=1)

# df = pd.concat([df_censo_2019, df_censo_2020, df_censo_2021])

for column in df_encceja_2020.columns:
    print(column, df_encceja_2020.dtypes[column])

print(df_encceja_2020.head(10))