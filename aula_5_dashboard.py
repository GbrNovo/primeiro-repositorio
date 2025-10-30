import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Meu primeiro Dashboard")
st.text("O nome do meu professor é Laerte")
st.button("Aperte o botão")
st.slider("Idade aqui", 0, 100, 25)
df = pd.read_csv("imoveis_brasil.csv")
st.dataframe(df)

file ="empresas_desempenho.csv"
df=pd.read_csv(file)

df_grouped = df.groupby("Setor")["Receita"].sum().reset_index()
fig = plt.figure(figsize=[8,5])
plt.bar(df_grouped["Setor"], df_grouped["Receita"])
plt.title("Gráfico de Barras Setor x Receita")
plt.xlabel("Ano")
plt.ylabel("Receita")
plt.show()

st.pyplot(fig)