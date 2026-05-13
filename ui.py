import dash
from dash import dcc, html, Input, Output
from database import abrir_conexao
from queries import sortear, listar_linguagem, listar_bibliotecas, adicionar_ideias

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Gerador de projetos"),
    dcc.Dropdown(
        id="categoria",
        options=[
            {"label": "Projeto", "value": "projeto"},
            {"label": "Desafio", "value": "desafio"},
        ],
        placeholder="Selecione uma categoria"
    ),
    dcc.Dropdown(
        id="dificuldade",
        options=[
            {"label": "Iniciante", "value": "iniciante"},
            {"label": "Intermediário", "value": "intermediario"},
            {"label": "Avançado", "value": "avançado"},
        ],
        placeholder="Selecione a dificuldade"
    ),
    html.Button("Sortear!", id="btn-sortear"),
    html.Div(id="resultado")
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
        return "Selecione uma categoria e dificuldade antes de sortear!"
    conexao = abrir_conexao("ideias.db")
    ideia = sortear(conexao, categoria, dificuldade)
    if ideia is None:
        return "Nenhuma ideia encontrada para esses filtros!"
    return html.Div([
        html.H3(ideia[1]),
        html.P(ideia[2]),
        html.P(f"Categoria: {ideia[3]}"),
        html.P(f"Dificuldade: {ideia[4]}")
])

if __name__ == "__main__":
    app.run(debug=True)