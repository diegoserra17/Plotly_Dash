import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc


app = Dash()

#1- Criando nosso DataFrame
df = pd.DataFrame({
    'Fruits': ['Maça','Laranja','Melão', 'Laranja', 'Uva', 'Melão'],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City': ['Gramado', 'São Luís', 'Gramado', 'Gramado', 'Curitiba', 'Curitiba']
    })

#print(df)

#2- Criando nosso gráfico
fig = px.bar(
    df,
    x='Fruits',
    y='Amount',
    color = 'City',
    barmode = 'group'
)

fig.show()
