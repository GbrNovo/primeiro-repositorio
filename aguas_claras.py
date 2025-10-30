import pandas as pd
file = "wp_mapa_problemas.csv"

df = pd.read_csv(file, encoding='ISO-8859-1', delimiter=';')
df.head()
df["tipo"].unique()
df.columns
cols=['tipo', 'email', 'telefone',
       'autorizacao', 'status',  'data_envio',
       'resposta_texto',  'bairro']
df=df[cols]
df["resposta_texto"] = df["resposta_texto"].fillna("Não Respondido")
df.groupby(['tipo'])["status"].count()