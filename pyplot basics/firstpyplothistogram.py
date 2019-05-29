#!/usr/bin/env python

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("datawind.csv" , sep = ",")
data = [go.Histogram(x = df['Installed Capacity (MW)'])]
layout = go.Layout(title = "histogram")
fig = go.Figure(data = data , layout = layout)
pyo.plot(fig)










import dash
# We create the first object, that will represent our dashboard and to which we will add components afterwards
app =dash.Dash()
