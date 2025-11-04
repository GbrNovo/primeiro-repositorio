import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# --- Leitura e limpeza dos dados ---
file = "wp_mapa_problemas.csv"
df = pd.read_csv(file, encoding='ISO-8859-1', delimiter=';')

cols = ['tipo', 'email', 'telefone', 'autorizacao', 'status', 'data_envio', 'resposta_texto', 'bairro']
df = df[cols]
df["resposta_texto"] = df["resposta_texto"].fillna("Não Respondido")

# --- Inicialização do app ---
app = Dash(__name__)
app.title = "Dashboard - Mapa de Problemas"

# --- Gráficos com Plotly ---
fig_pizza = px.pie(
    df, 
    names="tipo", 
    title="Distribuição de Problemas por Tipo",
    color_discrete_sequence=px.colors.qualitative.Set3
)

tipo_counts = df.groupby(['tipo'])["status"].count().sort_values(ascending=False).reset_index()
fig_barras = px.bar(
    tipo_counts,
    x="tipo",
    y="status",
    title="Quantidade de Problemas por Tipo",
    text_auto=True,
    color="status",
    color_continuous_scale="Blues"
)
fig_barras.update_layout(xaxis_title="Tipo de Problema", yaxis_title="Quantidade")

# --- Layout do dashboard ---
app.layout = html.Div([
    html.H1("📍 Mapa de Problemas - Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.P("Selecione o bairro:", style={'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='bairro-dropdown',
            options=[{'label': b, 'value': b} for b in sorted(df['bairro'].dropna().unique())],
            placeholder="Todos os bairros",
            multi=True
        ),
    ], style={'width': '50%', 'margin': 'auto'}),

    html.Div([
        dcc.Graph(id='grafico-pizza', figure=fig_pizza),
        dcc.Graph(id='grafico-barras', figure=fig_barras),
    ])
])

# --- Callbacks interativos ---
from dash.dependencies import Input, Output

@app.callback(
    [Output('grafico-pizza', 'figure'),
     Output('grafico-barras', 'figure')],
    [Input('bairro-dropdown', 'value')]
)
def atualizar_graficos(bairros_selecionados):
    df_filtrado = df.copy()
    if bairros_selecionados:
        df_filtrado = df[df['bairro'].isin(bairros_selecionados)]
    
    fig_pizza = px.pie(
        df_filtrado,
        names="tipo",
        title="Distribuição de Problemas por Tipo",
        color_discrete_sequence=px.colors.qualitative.Set3
    )

    tipo_counts = df_filtrado.groupby(['tipo'])["status"].count().sort_values(ascending=False).reset_index()
    fig_barras = px.bar(
        tipo_counts,
        x="tipo",
        y="status",
        title="Quantidade de Problemas por Tipo",
        text_auto=True,
        color="status",
        color_continuous_scale="Blues"
    )
    fig_barras.update_layout(xaxis_title="Tipo de Problema", yaxis_title="Quantidade")
    return fig_pizza, fig_barras


# --- Executa o servidor ---
if __name__ == "__main__":
    app.run(debug=True)