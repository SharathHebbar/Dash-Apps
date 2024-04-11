import datetime
import yfinance as yf
import pandas_datareader.data as web
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


"""
Dash App
"""
app = dash.Dash()
app.title = "Stock Visualization"

"""
App Layout
"""

app.layout = html.Div(
    children=[
        html.H1("Stock Viz Dashboard"),
        html.H4("Enter the Stock Name"),
        dcc.Input(
            id='input',
            value="AAPL",
            type='text'
        ),

        html.Div(id='output-graph')
    ]
)



"""
Callback Functions
"""

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [
        Input('input', 'value')
    ]
)
def update_graph(input_data):
    start = datetime.datetime(2018, 1, 1)
    end = datetime.datetime.now()

    try:
        
        df = yf.download(input_data, start=start, end=end)

        graph = dcc.Graph(
            id='graph',
            figure={
                'data': [
                    {
                        'x': df.index,
                        'y': df.Close,
                        'type': 'line',
                        'name': input_data
                    }
                ],
                'layout': {
                    'title': input_data
                }
            }
        )
    
    except:
        graph = html.Div("Error Retrieving Stock Data")

    return graph


if __name__ == '__main__':
    app.run_server()
