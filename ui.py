import dash
from dash import dcc, html, Input, Output
import plotly.express as px
from database import abrir_conexao
from queries import sortear, listar_linguagem, listar_bibliotecas, adicionar_ideias

app = dash.Dash(__name__)

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Dev Project Generator</title>
        {%favicon%}
        {%css%}
        <link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap" rel="stylesheet">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                background: #020818;
                color: #e0e0ff;
                font-family: 'Syne', sans-serif;
                min-height: 100vh;
                background-image: radial-gradient(ellipse at 20% 20%, #051533 0%, transparent 50%),
                                  radial-gradient(ellipse at 80% 80%, #020d24 0%, transparent 50%);
            }
            .header {
                padding: 48px 64px 32px;
                border-bottom: 1px solid rgba(255,255,255,0.06);
            }
            .header h1 {
                font-size: 48px;
                font-weight: 800;
                background: linear-gradient(135deg, #a78bfa, #60a5fa, #34d399);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                letter-spacing: -1px;
            }
            .header p {
                color: rgba(255,255,255,0.4);
                font-family: 'Space Mono', monospace;
                font-size: 13px;
                margin-top: 8px;
            }
            .main {
                padding: 48px 64px;
                max-width: 1400px;
            }
            .cards-row {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 20px;
                margin-bottom: 48px;
            }
            .stat-card {
                background: rgba(255,255,255,0.03);
                border: 1px solid rgba(255,255,255,0.08);
                border-radius: 16px;
                padding: 24px;
                position: relative;
                overflow: hidden;
            }
            .stat-card::before {
                content: '';
                position: absolute;
                top: 0; left: 0; right: 0;
                height: 2px;
            }
            .stat-card.purple::before { background: linear-gradient(90deg, #a78bfa, transparent); }
            .stat-card.blue::before { background: linear-gradient(90deg, #60a5fa, transparent); }
            .stat-card.green::before { background: linear-gradient(90deg, #34d399, transparent); }
            .stat-label {
                font-family: 'Space Mono', monospace;
                font-size: 11px;
                color: rgba(255,255,255,0.4);
                text-transform: uppercase;
                letter-spacing: 2px;
            }
            .stat-value {
                font-size: 40px;
                font-weight: 800;
                margin-top: 8px;
            }
            .stat-card.purple .stat-value { color: #a78bfa; }
            .stat-card.blue .stat-value { color: #60a5fa; }
            .stat-card.green .stat-value { color: #34d399; }
            .section-title {
                font-family: 'Space Mono', monospace;
                font-size: 11px;
                color: rgba(255,255,255,0.4);
                text-transform: uppercase;
                letter-spacing: 3px;
                margin-bottom: 16px;
            }
            .filters-row {
                display: grid;
                grid-template-columns: 1fr 1fr auto;
                gap: 16px;
                align-items: end;
                margin-bottom: 40px;
            }
            .filter-group { display: flex; flex-direction: column; gap: 8px; }
            .resultado-card {
                background: rgba(255,255,255,0.03);
                border: 1px solid rgba(255,255,255,0.08);
                border-radius: 20px;
                padding: 36px;
                position: relative;
                overflow: hidden;
                animation: fadeIn 0.4s ease;
                margin-bottom: 48px;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
            .resultado-card::before {
                content: '';
                position: absolute;
                top: 0; left: 0; right: 0;
                height: 2px;
                background: linear-gradient(90deg, #a78bfa, #60a5fa, #34d399);
            }
            .resultado-titulo {
                font-size: 28px;
                font-weight: 800;
                color: #fff;
                margin-bottom: 12px;
            }
            .resultado-desc {
                color: rgba(255,255,255,0.6);
                font-size: 15px;
                line-height: 1.7;
                margin-bottom: 24px;
            }
            .badges { display: flex; gap: 10px; }
            .badge {
                font-family: 'Space Mono', monospace;
                font-size: 11px;
                padding: 6px 14px;
                border-radius: 100px;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            .badge-cat { background: rgba(167,139,250,0.15); color: #a78bfa; border: 1px solid rgba(167,139,250,0.3); }
            .badge-dif { background: rgba(52,211,153,0.15); color: #34d399; border: 1px solid rgba(52,211,153,0.3); }
            .graficos-row {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
                margin-bottom: 48px;
            }
            .grafico-card {
                background: rgba(255,255,255,0.03);
                border: 1px solid rgba(255,255,255,0.08);
                border-radius: 16px;
                padding: 24px;
            }
            .tabela-card {
                background: rgba(255,255,255,0.03);
                border: 1px solid rgba(255,255,255,0.08);
                border-radius: 16px;
                padding: 24px;
                margin-bottom: 48px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                font-family: 'Space Mono', monospace;
                font-size: 13px;
            }
            th {
                color: rgba(255,255,255,0.4);
                text-align: left;
                padding: 12px 16px;
                border-bottom: 1px solid rgba(255,255,255,0.08);
                text-transform: uppercase;
                letter-spacing: 2px;
                font-size: 11px;
            }
            td {
                padding: 12px 16px;
                color: #e0e0ff;
                border-bottom: 1px solid rgba(255,255,255,0.04);
            }
            tr:hover td { background: rgba(255,255,255,0.02); }
            
            .dark-dropdown .Select-control {
                background-color: #051533 !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
                border-radius: 10px !important;
            }
            .dark-dropdown .is-focused > .Select-control,
            .dark-dropdown .is-open > .Select-control {
                background-color: #051533 !important;
                border-color: #a78bfa !important;
                box-shadow: 0 0 0 1px rgba(167, 139, 250, 0.5) !important;
            }
            .dark-dropdown .Select-value-label,
            .dark-dropdown .has-value.Select--single > .Select-control .Select-value .Select-value-label,
            .dark-dropdown .Select-value-label[role="option"] {
                color: #e0e0ff !important;
                font-weight: 700 !important;
            }
            .dark-dropdown .Select-input > input {
                color: #e0e0ff !important;
            }
            .dark-dropdown .Select-placeholder {
                color: rgba(255, 255, 255, 0.4) !important;
            }
            .dark-dropdown .Select-menu-outer {
                background-color: #0d1b3e !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
                border-radius: 10px !important;
                margin-top: 4px;
            }
            .dark-dropdown .Select-option {
                background-color: #0d1b3e !important;
                color: #e0e0ff !important;
            }
            .dark-dropdown .Select-option:hover,
            .dark-dropdown .Select-option.is-focused {
                background-color: rgba(96, 165, 250, 0.2) !important;
            }
            .dark-dropdown .Select-arrow,
            .dark-dropdown .Select-clear {
                color: rgba(255, 255, 255, 0.5) !important;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

def get_stats():
    conexao = abrir_conexao("ideias.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM ideias")
    total_ideias = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM linguagens")
    total_linguagens = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM estudos")
    total_estudos = cursor.fetchone()[0]
    return total_ideias, total_linguagens, total_estudos

def get_grafico_dificuldade():
    conexao = abrir_conexao("ideias.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT dificuldade, COUNT(*) FROM ideias GROUP BY dificuldade")
    dados = cursor.fetchall()
    labels = [d[0] for d in dados]
    values = [d[1] for d in dados]
    fig = px.pie(
        names=labels,
        values=values,
        color_discrete_sequence=["#a78bfa", "#60a5fa", "#34d399"],
        hole=0.5
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"color": "#e0e0ff", "family": "Space Mono"},
        legend={"font": {"color": "#e0e0ff"}},
        margin={"t": 20, "b": 20, "l": 20, "r": 20}
    )
    return fig

def get_grafico_categoria():
    conexao = abrir_conexao("ideias.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT categoria, COUNT(*) FROM ideias GROUP BY categoria")
    dados = cursor.fetchall()
    labels = [d[0] for d in dados]
    values = [d[1] for d in dados]
    fig = px.bar(
        x=labels,
        y=values,
        color=labels,
        color_discrete_sequence=["#a78bfa", "#60a5fa", "#34d399"],
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"color": "#e0e0ff", "family": "Space Mono"},
        showlegend=False,
        margin={"t": 20, "b": 20, "l": 20, "r": 20},
        xaxis={"gridcolor": "rgba(255,255,255,0.05)"},
        yaxis={"gridcolor": "rgba(255,255,255,0.05)"}
    )
    return fig

def get_todas_ideias():
    conexao = abrir_conexao("ideias.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT nome_ideias, categoria, dificuldade FROM ideias")
    return cursor.fetchall()

total_ideias, total_linguagens, total_estudos = get_stats()

app.layout = html.Div([
    html.Div([
        html.H1("Dev Project Generator"),
        html.P("// sorteia seu próximo projeto com base nos seus filtros")
    ], className="header"),

    html.Div([
        html.Div([
            html.Div([
                html.Div("Ideias cadastradas", className="stat-label"),
                html.Div(str(total_ideias), className="stat-value"),
            ], className="stat-card purple"),
            html.Div([
                html.Div("Linguagens", className="stat-label"),
                html.Div(str(total_linguagens), className="stat-value"),
            ], className="stat-card blue"),
            html.Div([
                html.Div("Estudos disponíveis", className="stat-label"),
                html.Div(str(total_estudos), className="stat-value"),
            ], className="stat-card green"),
        ], className="cards-row"),

        html.Div("// sortear ideia", className="section-title"),
        html.Div([
            html.Div([
                html.Div("Categoria", className="section-title"),
                dcc.Dropdown(
                    id="categoria",
                    options=[
                        {"label": "Projeto", "value": "projeto"},
                        {"label": "Desafio", "value": "desafio"},
                    ],
                    placeholder="Selecione...",
                    className="dark-dropdown"
                ),
            ], className="filter-group"),
            html.Div([
                html.Div("Dificuldade", className="section-title"),
                dcc.Dropdown(
                    id="dificuldade",
                    options=[
                        {"label": "Iniciante", "value": "iniciante"},
                        {"label": "Intermediário", "value": "intermediario"},
                        {"label": "Avançado", "value": "avançado"},
                    ],
                    placeholder="Selecione...",
                    className="dark-dropdown"
                ),
            ], className="filter-group"),
            html.Button("→ Sortear", id="btn-sortear", style={
                "background": "linear-gradient(135deg, #1d4ed8, #2563eb)",
                "border": "none",
                "color": "#fff",
                "padding": "12px 32px",
                "borderRadius": "10px",
                "fontSize": "15px",
                "fontWeight": "700",
                "fontFamily": "Syne, sans-serif",
                "cursor": "pointer",
                "letterSpacing": "0.5px",
                "height": "38px",
                "alignSelf": "end"
            }),
        ], className="filters-row"),

        html.Div(id="resultado"),

        html.Div("// estatísticas", className="section-title"),
        html.Div([
            html.Div([
                html.Div("Ideias por dificuldade", className="section-title"),
                dcc.Graph(figure=get_grafico_dificuldade(), config={"displayModeBar": False})
            ], className="grafico-card"),
            html.Div([
                html.Div("Ideias por categoria", className="section-title"),
                dcc.Graph(figure=get_grafico_categoria(), config={"displayModeBar": False})
            ], className="grafico-card"),
        ], className="graficos-row"),

        html.Div("// todas as ideias", className="section-title"),
        html.Div([
            html.Table([
                html.Thead(html.Tr([
                    html.Th("Nome"),
                    html.Th("Categoria"),
                    html.Th("Dificuldade"),
                ])),
                html.Tbody([
                    html.Tr([
                        html.Td(ideia[0]),
                        html.Td(ideia[1]),
                        html.Td(ideia[2]),
                    ]) for ideia in get_todas_ideias()
                ])
            ])
        ], className="tabela-card"),

    ], className="main")
])

@app.callback(
    Output("resultado", "children"),
    Input("btn-sortear", "n_clicks"),
    Input("categoria", "value"),
    Input("dificuldade", "value"),
    prevent_initial_call=True
)
def realizar_sortio(n_clicks, categoria, dificuldade):
    if n_clicks is None or categoria is None or dificuldade is None:
        return html.Div("Selecione uma categoria e dificuldade antes de sortear!", style={
            "color": "rgba(255,255,255,0.3)",
            "fontFamily": "Space Mono, monospace",
            "fontSize": "13px",
            "marginBottom": "48px"
        })
    conexao = abrir_conexao("ideias.db")
    ideia = sortear(conexao, categoria, dificuldade)
    if ideia is None:
        return html.Div("Nenhuma ideia encontrada para esses filtros!", style={
            "color": "rgba(255,255,255,0.3)",
            "fontFamily": "Space Mono, monospace",
            "fontSize": "13px",
            "marginBottom": "48px"
        })
    return html.Div([
        html.Div(ideia[1], className="resultado-titulo"),
        html.Div(ideia[2], className="resultado-desc"),
        html.Div([
            html.Span(ideia[3], className="badge badge-cat"),
            html.Span(ideia[4], className="badge badge-dif"),
        ], className="badges")
    ], className="resultado-card")

if __name__ == "__main__":
    app.run(debug=True)