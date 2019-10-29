#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../Data/mocksurvey.csv')
list_of_col = [col for col in df.columns if col != 'Unnamed: 0']
print(list_of_col)

data = []
for response in list_of_col:
    print(response)
    trace = go.Bar(x=df[response], y=df['Unnamed: 0'], name=response, orientation='h')
    data.append(trace)
#
layout = go.Layout(title='mocksurvey', barmode='stack')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
