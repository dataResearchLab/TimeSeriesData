import pandas as pd

def get_gdp():
    pass

def get_pop():
    import plotly.express as px
    df = px.data.gapminder()
    print(df.columns)
    df1 = df
    df1 = df1.rename(columns={'country': 'name', 'pop': 'value'})
    df1 = df1[['name', 'year', 'value']]
    df1 = df1.sort_values(['name', 'year'], ascending=True)
    df = df1[(df1.year > 1800)]
    return df