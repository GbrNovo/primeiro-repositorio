import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Dashboard de Problemas Reportados",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Carregamento e Preparação dos Dados ---
@st.cache_data
def load_data(file_path):
    """
    Carrega o dataset, faz limpeza e conversão de tipos de dados.
    Usa encoding='ISO-8859-1' e delimiter=';'.
    """
    try:
        df = pd.read_csv(
            file_path,
            sep=';',
            encoding='ISO-8859-1'
        )

        # 1. Conversão e Limpeza de Dados Geográficos
        # Garante que 'longitude' e 'latitude' sejam numéricas
        for col in ['longitude', 'latitude']:
            if col in df.columns:
                # Trata a substituição de vírgula por ponto (comum em CSVs) e converte para float
                df[col] = df[col].astype(str).str.replace(',', '.', regex=False)
                df[col] = pd.to_numeric(df[col], errors='coerce') # 'coerce' transforma falhas em NaN

        # Renomeia colunas para o padrão st.map (latitude=lat, longitude=lon)
        # O Streamlit aceita 'latitude' e 'longitude' também, mas a renomeação ajuda a garantir
        df.rename(columns={'latitude': 'lat', 'longitude': 'lon'}, inplace=True)

        # Remove linhas que não puderam ser convertidas (coordenadas inválidas)
        df.dropna(subset=['lat', 'lon'], inplace=True)

        # 2. Limpeza de Colunas de Texto
        df['tipo'] = df['tipo'].fillna('Não Informado')
        df['status'] = df['status'].fillna('Desconhecido')

        return df
    except Exception as e:
        st.error(f"Erro ao carregar ou processar o arquivo. Detalhes do erro: {e}")
        return pd.DataFrame() # Retorna um DataFrame vazio em caso de erro

DATA_FILE = 'wp_mapa_problemas.csv'
df = load_data(DATA_FILE)

# --- Título do Dashboard ---
st.title("🗺️ Dashboard de Problemas Reportados")
st.markdown("Análise da distribuição, status e localização dos problemas cadastrados.")

if df.empty:
    st.stop() # Para a execução se o DataFrame estiver vazio

# --- Sidebar para Filtros ---
st.sidebar.header("⚙️ Filtros")

# Filtro por Tipo de Problema
tipos_unicos = ['Todos'] + sorted(df['tipo'].unique().tolist())
tipo_selecionado = st.sidebar.selectbox(
    "Filtrar por Tipo:",
    tipos_unicos
)

# Filtro por Status
status_unicos = ['Todos'] + sorted(df['status'].unique().tolist())
status_selecionado = st.sidebar.multiselect(
    "Filtrar por Status:",
    status_unicos,
    default=['Todos']
)

# Aplicação dos Filtros
df_filtrado = df.copy()

if tipo_selecionado != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['tipo'] == tipo_selecionado]

if 'Todos' not in status_selecionado:
    df_filtrado = df_filtrado[df_filtrado['status'].isin(status_selecionado)]

# ----------------------------------------------------
# --- NOVIDADE: MAPA DE PROBLEMAS ---
# ----------------------------------------------------
st.header("📍 Mapa de Problemas")

if not df_filtrado.empty:
    # Seleciona apenas as colunas necessárias para o mapa
    df_mapa = df_filtrado[['lat', 'lon', 'tipo']].copy()
    
    # st.map exige as colunas 'lat' e 'lon' (ou 'latitude' e 'longitude')
    st.map(df_mapa, zoom=12) 
    
    st.info(f"O mapa exibe **{len(df_mapa):,}** problemas com coordenadas válidas após a aplicação dos filtros.")
else:
    st.warning("Nenhum problema com coordenadas válidas para exibir no mapa com os filtros aplicados.")

st.markdown("---")
# ----------------------------------------------------


# --- Métricas Principais (Cards) ---
total_problemas = len(load_data(DATA_FILE)) # Usando o df original (completo)
problemas_filtrados = len(df_filtrado)

st.header("Sumário Executivo")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total de Problemas no Arquivo",
        value=f"{total_problemas:,}",
        delta="Base de dados completa",
        delta_color="off"
    )

with col2:
    st.metric(
        label="Problemas Exibidos (Filtro)",
        value=f"{problemas_filtrados:,}",
        delta=f"Representa {problemas_filtrados/total_problemas:.1%} do total",
        delta_color="inverse" if problemas_filtrados < total_problemas else "off"
    )

if 'Finalizado' in df['status'].unique():
    total_finalizados = df['status'].value_counts().get('Finalizado', 0)
    with col3:
        st.metric(
            label="Total de Problemas Finalizados",
            value=f"{total_finalizados:,}",
            delta=f"Percentual: {total_finalizados/total_problemas:.1%}",
            delta_color="normal"
        )
else:
    with col3:
        st.info("Nenhum problema com status 'Finalizado' encontrado na base.")

st.markdown("---")

# --- Visualizações (Gráficos) ---
st.header("Análise Detalhada (Dados Filtrados)")

col_graf_1, col_graf_2 = st.columns(2)

# 1. Gráfico de Distribuição por Tipo
with col_graf_1:
    st.subheader("Distribuição por Categoria ('tipo')")
    if not df_filtrado.empty:
        tipo_counts = df_filtrado['tipo'].value_counts().head(10)
        fig_tipo, ax_tipo = plt.subplots(figsize=(8, 6))

        cores = [mcolors.CSS4_COLORS[c] for c in list(mcolors.CSS4_COLORS.keys())[10::15]] 

        ax_tipo.bar(tipo_counts.index, tipo_counts.values, color=cores[:len(tipo_counts)])
        ax_tipo.set_ylabel("Contagem de Problemas")
        ax_tipo.set_title("Top 10 Tipos de Problemas")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        st.pyplot(fig_tipo)
    else:
        st.warning("Nenhum dado para exibir com os filtros aplicados.")

# 2. Gráfico de Distribuição por Status
with col_graf_2:
    st.subheader("Distribuição por Status")
    if not df_filtrado.empty:
        status_counts = df_filtrado['status'].value_counts()
        fig_status, ax_status = plt.subplots(figsize=(8, 6))

        cor_map = {
            'Finalizado': 'green',
            'Encaminhado': 'blue',
            'pendente': 'orange',
            'aguardando': 'gray',
            'Em Andamento': 'yellowgreen'
        }
        cores_status = [cor_map.get(s, 'darkred') for s in status_counts.index]

        ax_status.bar(status_counts.index, status_counts.values, color=cores_status)
        ax_status.set_ylabel("Contagem de Problemas")
        ax_status.set_title("Distribuição de Status dos Problemas")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        st.pyplot(fig_status)


# --- Tabela de Dados (RAW Data) ---
st.markdown("---")
st.header("📊 Dados Detalhados (Filtrados)")
st.dataframe(df_filtrado)