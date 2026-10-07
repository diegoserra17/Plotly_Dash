from dash import Dash, html, dcc, dash_table
import pandas as pd


app = Dash()

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

#print(df)

app.layout = html.Div([
    html.Div(children='Datatable com Dash'),
    dash_table.DataTable(
        data=df.to_dict('records'),
        #paginação: 10 por página
        page_size=10, 
    )
])

if __name__ == '__main__':
    app.run(debug=True)