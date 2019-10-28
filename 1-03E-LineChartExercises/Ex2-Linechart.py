#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('../Data/2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']
data = []
# Use a for loop (or list comprehension to create traces for the data list)
for day in days:

    df2 = df[df['DAY'] == day]
    df2_y_value = df2['T_HR_AVG']
    df2_x_value = df2['LST_TIME']

    trace = go.Scatter(x=df2_x_value, y=df2_y_value, mode='lines', name=day)
    data.append(trace)

# Define the layout
# Create a fig from data and layout, and plot the fig

layout = go.Layout(title='Days')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)

