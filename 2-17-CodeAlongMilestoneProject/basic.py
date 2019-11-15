#!/usr/bin/env python3

from datetime import datetime as dt
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from numpy import random

pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as web

app =  dash.Dash()

symbols = web.get_nasdaq_symbols()

print(symbols.head())

app.layout = html.Div([
                html.H1(id='title', children='Stock Ticker Symbol'),
                html.Div([
                    html.Pre(id='pre1', children='Select stock symbols:')
                ], style={'width': '49%', 'display': 'inline-block'}),
                html.Div([
                    html.Pre(id='pre2', children='Select start and end dates:'),
                ], style={'width': '49%', 'display': 'inline-block'}),

                html.Div([
                    dcc.Dropdown(
                        id='stock-dropdown',
                        options=[
                            {'label': 'New York City', 'value': 'NYC'},
                            {'label': 'Montréal', 'value': 'MTL'},
                            {'label': 'San Francisco', 'value': 'SF'}
                        ],
                        value='MTL'
                    ),
                ], style={'width': '49%', 'display': 'inline-block'}),
                html.Div([
                    dcc.DatePickerRange(
                        id='date-picker-range',
                        start_date=dt(1997, 5, 3),
                        end_date_placeholder_text='Select a date!')
                ], style={'width': '30%', 'display': 'inline-block'}),
                html.Div([html.Button('Submit', id='submit-button')
                ], style={'width': '20%', 'display': 'inline-block'}),

])

if __name__ == "__main__":
    app.run_server()