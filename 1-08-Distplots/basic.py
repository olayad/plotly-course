import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd
import numpy as np

x = np.random.randn(1000)
print(x)
print(type(x))
hist_data = [x]
print()
print(hist_data)
print(type(hist_data))

group_labels = ['distplot']

fig = ff.create_distplot(list(x), group_labels)

pyo.plot(fig)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# NOT WORKING, FOLLOWED INSTRUCTIONS FROM VIDEO, COULDN'T FIGURE OUT WHY
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!