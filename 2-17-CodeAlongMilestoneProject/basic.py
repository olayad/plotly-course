#!/usr/bin/env python3

from datetime import datetime as dt
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import plotly.graph_objs as go
from numpy import random

pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as web

app =  dash.Dash()

df = web.get_nasdaq_symbols()
# print(df.head())
# print()
stocks = [{'value': i, 'label': df.loc[i]['Security Name']} for i in df.index]
#
# start = '2017-04-22'
# end = '2018-04-22'
# f = web.DataReader(name='A', data_source='quandl', start=start, end=end)
# print(f.tail())
#
# y_axis = [price for price in f['Close']]
# print(y_axis)
# x_axis = [date for date in f.index]
# print(x_axis)
#
# print(x_axis[0])
# chart = dcc.Graph(id='graphy',
#                   figure={'data': [go.Scatter(x=x_axis,
#                                              y=y_axis,
#                                              mode='lines')],
#                           'layout': go.Layout(title='title',
#                                               hovermode='closest')
#                           })



app.layout = html.Div([
                html.H1(id='title', children='Stock Ticker Symbol'),
                html.Div([
                    html.Pre(id='pre1', children='Select stock symbols:')
                ], style={'width': '49%', 'display': 'inline-block'}),
                html.Div([
                    html.Pre(id='pre2', children='Select start and end dates:'),
                ], style={'width': '49%', 'display': 'inline-block'}),

                html.Div([
                    dcc.Dropdown(id='stock-dropdown',
                                 # options=[
                                 #     {'label': 'New York City', 'value': 'NYC'},
                                 #     {'label': 'Montréal', 'value': 'MTL'},
                                 #     {'label': 'San Francisco', 'value': 'SF'}
                                 # ],
                                 options=stocks,
                                 # value='MTL'
                                 ),
                ], style={'width': '49%', 'display': 'inline-block'}),
                html.Div([
                    dcc.DatePickerRange(
                        id='date-picker',
                        start_date=dt(1997, 5, 3),
                        end_date=dt.today())
                ], style={'width': '30%', 'display': 'inline-block'}),
                html.Div([html.Button('submit', id='submit-button')
                ], style={'width': '20%', 'display': 'inline-block'}),

                dcc.Graph(id='graphy',
                                  figure={'data': [go.Scatter(x=[],
                                                             y=[],
                                                             mode='lines')],
                                          'layout': go.Layout(title='title',
                                                              hovermode='closest')
                                          })
])


@app.callback(Output('graphy', 'figure'),
              [Input('submit-button', 'n_clicks')],
              [State('date-picker', 'start_date'),
               State('date-picker', 'end_date'),
               State('stock-dropdown', 'value')])
def callback_symbol(_, start_date, end_date, ticker):
    print('start:{}, end:{}, ticker:{}'.format(start_date, end_date, ticker))
    f = web.DataReader(name=ticker, data_source='quandl', start=start_date, end=end_date)
    print(f.tail())

    y_axis = [price for price in f['Close']]
    print(y_axis)
    x_axis = [date for date in f.index]
    print(x_axis)

    return {'data': [go.Scatter(x=x_axis,
                                y=y_axis,
                                mode='lines')],
            'layout': go.Layout(title='title',
                                hovermode='closest')}


if __name__ == "__main__":
    app.run_server()