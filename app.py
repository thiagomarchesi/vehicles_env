import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header("Dashboard de Visualização de Dados")

st.write(car_data)

hist_button = st.button

if hist_button:
    st.write('Criando um gráfico histograma para o conjunto de dados')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados')
    fig = px.scatter(car_data, x="type", y="price")
    st.plotly_chart(fig, use_container_width=True)
