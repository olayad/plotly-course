#######
# This script creates a static matplotlib plot
######
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # create fake data:
# df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
# df.plot()
# plt.show()
#######
# At the terminal run:  python basic1.py
# Close the plot window to close the script
######

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(x=random_x, y=random_y, mode='markers',
        marker=dict(
            size=12,
            color='rgb(51,205,153)',
            symbol='pentagon',
            line={'width':2}))]

layout = go.Layout(title='waka',
                   xaxis={'title':'My X Axis'},
                   yaxis=dict(title='My Y axis'),
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='scatter.html')

