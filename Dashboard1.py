import dash
from dash import dcc 
from dash import html 
from graficas import * 

app = dash.Dash()

app.layout = html.Div([
    html.H1('Dashboard 1', style={'textAlign':'center'}),
    html.H3('Integrantes del Equipo:'),
    html.Ul([
        html.Li('Daniel Arturo González González (A01650928)'),
        html.Li('Sebastian Rodriguez Flores (A01655204)')
        ]),
    dcc.Graph(
        id='graph_1',
        figure=graficodebarras(),
        style={'width': '50%'}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)