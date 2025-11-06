import matplotlib.pyplot as plt
import pandas as pd

file = "empresas_desempenho.csv"
df = pd.read_csv(file)
df.head()

# Gráfico de Linha

filtro=df["Setor"]=="Comércio"
df_com = df.loc[filtro]
plt.figure(figsize=[8,5])
plt.plot(df_com["Ano"], df_com["Receita"])
plt.title("Gráfico de Linha Receita x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita")
plt.show()

plt.style.use('default')
plt.figure(figsize=[10, 6])
plt.plot(
    df_com["Ano"], 
    df_com["Receita"], 
    color='black',
    linewidth=2,
    marker='o',
    markersize=7,
    markerfacecolor='red',
    markeredgecolor='black'
)
plt.title(
    "Evolução da Receita no Setor de Comércio",
    fontsize=16,
    fontweight='bold',
    color='black'
)
plt.xlabel("Ano", fontsize=14, color='black')
plt.ylabel("Receita (em Milhões/Bilhões)", fontsize=14, color='black')
plt.tick_params(axis='both', which='major', labelsize=12)
plt.grid(True, linestyle='-', alpha=0.5, color='lightgray')
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('black')
ax.spines['left'].set_color('black')
plt.show()

# Gráfico de Barras

df_grouped = df.groupby("Setor")["Receita"].sum().reset_index()
plt.figure(figsize=[8,5])
plt.bar(df_grouped["Setor"], df_grouped["Receita"])
plt.title("Gráfico de Barras Setor x Receita")
plt.xlabel("Ano")
plt.ylabel("Receita")
plt.show()

#Gráfico de Pizza

df_part = df.groupby("Setor")["ParticipacaoMercado"].mean().reset_index()
plt.figure(figsize=[8,5])
plt.pie(df_part["ParticipacaoMercado"], autopct="%1.1f%%")
plt.title("Gráfico de Pizza de Participação do Mercado")
plt.show()
