import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header("Dashboard de Visualização de Dados")

st.write(car_data)

hist_button = st.button('Criar histograma')

bins = [0, 10000, 20000, 30000, 40000, 50000, 100000]

if hist_button:
    
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
      
    fig = px.histogram(car_data, y="price", bins=bins, opacity=0.5)
    
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados')
    fig = px.scatter(car_data, x="type", y="price")
    st.plotly_chart(fig, use_container_width=True)
