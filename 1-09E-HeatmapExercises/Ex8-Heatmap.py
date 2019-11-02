#######
# Objective: Using the "flights" dataset available
# from the data folder as flights.csv
# create a heatmap with the following parameters:
# x-axis="year"
# y-axis="month"
# z-axis(color)="passengers"
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools
import pandas as pd

# Create a DataFrame from  "flights" data
df = pd.read_csv('../Data/flights.csv')
print(df)
print(df.columns)

data = [go.Heatmap(x=df['year'], y=df['month'], z=df['passengers'], colorscale='Jet')]
layout = go.Layout(title='heatmap')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
