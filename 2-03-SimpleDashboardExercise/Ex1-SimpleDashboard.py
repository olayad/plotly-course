#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('../Data/OldFaithful.csv')

trace = [go.Scatter(x=df['X'], y=df['Y'], mode='markers')]
layout = go.Layout(title='Old Faithful Eruption Intervals v Durations')

# THIS IS IF I JUST WANTED CHART
# fig = go.Figure(data=trace, layout=layout)
# pyo.plot(fig)

app.layout = html.Div([dcc.Graph(id='waka',
                                 figure={'data': trace,
                                         'layout': layout})])

if __name__ == '__main__':
    app.run_server()
