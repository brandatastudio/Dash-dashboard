#!/usr/bin/env python

import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash()
datause = pd.read_csv("datawind.csv" , sep = ",")

#making sure that the dropdown menu has column names as arguments




app.layout = html.Div([
dcc.Graph(
       id = 'barplot1'),
dcc.Dropdown(
       id="dropmenu" ,
       options=[{'label' : i , 'value' : i } for i in datause.columns.values
],
       value='Total Investment ($ Millions)')

],
)

@app.callback(Output(component_id = 'barplot1', component_property = 'figure'),
              [Input(component_id = 'dropmenu' , component_property = 'value')])
def update_figure(dropmenuinput):

    potato = dropmenuinput
    return {
        'data':  [
        go.Bar(
        x = datause["State"],
        y = datause[potato])],
        'layout': go.Layout(
        title = "pene"
        ,xaxis={'title': "state"},
        yaxis ={'title' : potato})  }


if __name__ == '__main__':
    app.run_server(debug=True)
