import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import base64

df = pd.read_csv('../Data/wheels.csv')
print(df.head())

app = dash.Dash()

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file,'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

# Por estudiar que significa base64 base 64 basebase base basebasse base base vase basebasebasebase











app.layout = html.Div([
                dcc.RadioItems(id='wheels',
                               options=[{'label': i, 'value': i} for i in df['wheels'].unique()],
                               value=1
                               ),
                html.Div(id='wheels-output'),

                html.Hr(),
                dcc.RadioItems(id='colors',
                               options=[{'label': i, 'value': i} for i in df['color'].unique()],
                               value='blue'
                               ),
                html.Div(id='colors-output')
], style={'fontFamily': 'helvetica', 'fontSize':18})


@app.callback(Output('wheels-output', 'children'),
              [Input('wheels', 'value')])
def callback_a(wheels_value):
    return "you chose {}".format(wheels_value)

@app.callback(Output('colors-output', 'children'),
              [Input('colors', 'value')])
def callback_b(colors_value):
    return "you chose {}".format(colors_value)

if __name__ == '__main__':
    app.run_server()