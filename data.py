import pandas as pd

def get_gdp():
    df = pd.read_excel('gdp.xls')
    df1 = pd.melt(df, id_vars=['Country Name'],
                  var_name="Date", value_name="Value")
    df1 = df1.rename(columns={'Country Name': 'name', 'Date': 'year', 'Value': 'value'})
    df1 = df1.sort_values(['name', 'year', 'value'], ascending=True)
    df = df1
    df.year = df.year.astype(int).fillna(0)
    df.value = df.value.astype(float).fillna(0.0)
    df.value = df.value.apply(lambda x: x / 1000000)
    return df

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