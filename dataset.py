import pandas as pd

#importando o dataset
ecom_sales = pd.read_csv('dados/ecom_sales.csv')
#agregação de dados por país, somando o valor total dos pedidos
ecom_sales_novo = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='Total Sales (R$)')
#print(ecom_sales.head())
print(ecom_sales_novo)