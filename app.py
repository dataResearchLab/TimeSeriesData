from dash import Dash, dcc, html, Input, Output
from raceplotly.plots import barplot
import  pandas as pd
from data import  *
app = Dash(__name__)
app.layout = html.Div([

    dcc.RadioItems(
        id='selection',
        options=["Population","GDP"],
        value='Population',
    ),
    dcc.Loading(dcc.Graph(id="graph"), type="cube")
])

@app.callback(
    Output("graph", "figure"),
    Input("selection", "value"))
def display_animated_graph(selection):
    if selection == 'Population':
        data=get_pop()
    else:
        pass
    my_raceplot = barplot(data, item_column='name', value_column='value', time_column='year',)
    graph=my_raceplot.plot(item_label='Top Group', value_label='value', frame_duration=500)
    return graph

if __name__ == '__main__':
    app.run_server(debug=True)