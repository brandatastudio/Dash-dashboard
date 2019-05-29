#!/usr/bin/env python

import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()
datause = pd.read_csv("datawind.csv" , sep = ",")

app.layout = html.Div([dcc.Graph(id = 'barplot', figure = {'data' : [
go.Bar(x = datause["State"] , y = datause["Wind Projects Online"])
] , 'layout' : go.Layout(title = 'mybigdick')} )
])

if __name__ == '__main__':
    app.run_server(debug=True)
