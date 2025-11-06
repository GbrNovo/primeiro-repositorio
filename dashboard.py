import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Dashboard - Mapa de Problemas",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Leitura e Limpeza dos Dados ---
# Nota: Certifique-se de que o arquivo 'wp_mapa_problemas.csv' esteja no mesmo diretório
# que o script Streamlit ou forneça o caminho completo.
try:
    file = "wp_mapa_problemas.csv"
    df = pd.read_csv(file, encoding='ISO-8859-1', delimiter=';')
except FileNotFoundError:
    st.error(f"Erro: O arquivo '{file}' não foi encontrado. Certifique-se de que ele está no diretório correto.")
    st.stop()
except Exception as e:
    st.error(f"Ocorreu um erro ao carregar o arquivo: {e}")
    st.stop()


cols = ['tipo', 'email', 'telefone', 'autorizacao', 'status', 'data_envio', 'resposta_texto', 'bairro']
df = df[cols]
df["resposta_texto"] = df["resposta_texto"].fillna("Não Respondido")
df['bairro'] = df['bairro'].str.strip() # Limpeza extra para o filtro

# --- Título do Dashboard ---
st.title("📍 Mapa de Problemas - Dashboard")

# --- Componente de Filtro ---
# Obtém a lista única e ordenada de bairros
bairros_unicos = sorted(df['bairro'].dropna().unique())

# Streamlit multiselect para selecionar bairros
st.markdown("#### Seleção de Filtros")
bairros_selecionados = st.multiselect(
    "Selecione o(s) bairro(s):",
    options=bairros_unicos,
    default=[] # Começa sem pré-seleção
)

# --- Lógica de Filtragem ---
if bairros_selecionados:
    df_filtrado = df[df['bairro'].isin(bairros_selecionados)]
    # Exibe a contagem de problemas após a filtragem
    st.info(f"Mostrando {len(df_filtrado)} problemas para os bairros selecionados.")
else:
    df_filtrado = df.copy()
    st.info(f"Mostrando todos os {len(df_filtrado)} problemas.")

# Verifica se o DataFrame filtrado não está vazio antes de gerar gráficos
if df_filtrado.empty:
    st.warning("Nenhum dado encontrado para os bairros selecionados.")
    st.stop()

# --- Geração dos Gráficos com Plotly ---

# 1. Gráfico de Pizza (Distribuição por Tipo)
fig_pizza = px.pie(
    df_filtrado, 
    names="tipo", 
    title="Distribuição de Problemas por Tipo",
    color_discrete_sequence=px.colors.qualitative.Set3,
    hole=.3 # Adiciona um buraco para melhor visualização
)
fig_pizza.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
fig_pizza.update_layout(margin=dict(t=50, b=0, l=0, r=0))


# 2. Gráfico de Barras (Quantidade por Tipo)
tipo_counts = df_filtrado.groupby(['tipo'])["status"].count().sort_values(ascending=False).reset_index(name='Quantidade')
fig_barras = px.bar(
    tipo_counts,
    x="tipo",
    y="Quantidade",
    title="Quantidade de Problemas por Tipo",
    text_auto=True,
    color="Quantidade",
    color_continuous_scale="Viridis"
)
fig_barras.update_layout(
    xaxis_title="Tipo de Problema", 
    yaxis_title="Quantidade",
    xaxis={'categoryorder':'total descending'}
)

# --- Layout e Exibição no Streamlit ---

# Cria duas colunas para posicionar os gráficos lado a lado
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_pizza, use_container_width=True)

with col2:
    st.plotly_chart(fig_barras, use_container_width=True)

# Exibe o DataFrame filtrado como um detalhe expansível
with st.expander("Ver Dados Filtrados"):
    st.dataframe(df_filtrado, use_container_width=True)
