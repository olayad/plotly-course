#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../Data/abalone.csv')
print(df)

batch1 = np.random.choice(df['rings'], 30, replace=False)
batch2 = np.random.choice(df['rings'], 20, replace=False)
data = [go.Box(y=batch1, name='batch1'), go.Box(y=batch2, name='batch2')]

pyo.plot(data)
print()
print(batch1)
print(batch2)
# take two random samples of different sizes:



# create a data variable with two Box plots:











# add a layout




# create a fig from data & layout, and plot the fig
