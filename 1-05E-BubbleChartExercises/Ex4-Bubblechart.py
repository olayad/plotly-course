#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../Data/mpg.csv')
print(df)

data = [go.Scatter(x=df['displacement'],
                   y=df['acceleration'],
                   text=df['name'],     # what shows when mouse hovers over marker
                   mode='markers',
                   marker=dict(size=df['cylinders']*2, color=df['model_year'], showscale=True))]

layout = go.Layout(title='Acceleration vs Displacement',
                   hovermode='closest',
                   xaxis = dict(title = 'displacement'),
                   yaxis = dict(title = 'acceleration = seconds to reach 60mph'))
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
