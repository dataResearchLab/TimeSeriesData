from dash import Dash, dcc, html, Input, Output
from raceplotly.plots import barplot
import  pandas as pd
from data import  *
app = Dash(__name__)
app.layout = html.Div([
    html.H2('Data Comparison over Years'),
    html.P("Select an option:"),
    dcc.RadioItems(
        id='selection',
        options=["GDP", "Population"],
        value='GDP',
    ),
    dcc.Loading(dcc.Graph(id="graph"), type="cube")
])


@app.callback(
    Output("graph", "figure"),
    Input("selection", "value"))
def display_animated_graph(selection):
    if selection == 'GDP':
        data=get_gdp()
    else:
        data=get_pop()
    my_raceplot = barplot(data, item_column='name', value_column='value', time_column='year',)
    graph=my_raceplot.plot(item_label='Top Group', value_label='value', frame_duration=500)
    return graph

app.run_server(debug=True)
