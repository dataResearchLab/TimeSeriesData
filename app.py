import dash
from dash import html,dcc


app = dash.Dash()
app.layout = html.Div(children=[
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Delhi'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Mumbai'},
            ],
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
