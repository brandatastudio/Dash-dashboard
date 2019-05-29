#!/usr/bin/env python

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()


df = pd.read_csv('information regarding the project/googleplaystore.csv' , sep = ",")


categorical_features = df[["App" , "Category" , "Android Ver" , "Type" , "Genres" , "Current Ver" , "Content Rating"]]
num_features = df[["Installs" , "Price" , "Size" ]]

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='xaxis',
                options=[{'label': i, 'value': i} for i in categorical_features],
                value='Category'
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis',
                options=[{'label': i, 'value': i} for i in num_features],
                value='Installs'
            )
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='barplot1')
], style={'padding':10})

@app.callback(
    Output('barplot1', 'figure'),
    [Input('xaxis', 'value'),
     Input('yaxis', 'value')])
def update_graph(xaxis_name, yaxis_name):
    return {
        'data':  [
        go.Bar(
        x = df[xaxis_name],
        y = df[yaxis_name]
            )],
        'layout': go.Layout(
        title = "pene"
        ,xaxis={'title': xaxis_name},
        yaxis ={'title' : yaxis_name})  }


if __name__ == '__main__':
    app.run_server()
