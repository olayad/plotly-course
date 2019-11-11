import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
                html.Div([
                    dcc.RangeSlider(
                        id='my-slider',
                        min=-5,
                        max=5,
                        step=1,
                        value=[-5, 5],
                        marks={i: str(i) for i in range(-5, 6)})
                ], style={'border': '2px'}),
                html.H1(id='slider-output-container', style={'padding': 10})
            ])

@app.callback(Output('slider-output-container', 'children'),
              [Input('my-slider', 'value')])
def callback_result(value):
    return value[0] * value[1]

if __name__ == '__main__':
    app.run_server()