#!/usr/bin/env python

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()


df = pd.read_csv("datawind.csv" , sep = ",")


features = df.columns

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='coloraxis',
                options=[{'label': i, 'value': i} for i in features],
                value='Total Investment ($ Millions)'
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis',
                options=[{'label': i, 'value': i} for i in features],
                value='Installed Capacity (MW)'
            )
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='barplot1')
], style={'padding':10})

@app.callback(
    Output('barplot1', 'figure'),
    [Input('coloraxis', 'value'),
     Input('yaxis', 'value')])
def update_graph(color_name, yaxis_name):
    return {
        'data':  [
        go.Bar(
        x = df['State'],
        y = df[yaxis_name],
            marker = {
                "color" : df[color_name],
                "colorbar" : dict(title = color_name),
                "colorscale" : 'Viridis'
                })],
        'layout': go.Layout(
        title = "pene"
        ,xaxis={'title': "state"},
        yaxis ={'title' : yaxis_name})  }


if __name__ == '__main__':
    app.run_server()
