import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../Data/mpg.csv')
# print(df)
print(df.columns)

data = [go.Scatter(x=df['horsepower'],
                   y=df['mpg'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=df['weight']/100, color=df['cylinders'], showscale=True))] # this turns it into a bubble chart, the factor is scale factor of the bubble

layout = go.Layout(title='Bubble Chart', hovermode='closest')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
