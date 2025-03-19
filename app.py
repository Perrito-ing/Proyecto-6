import os
import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de la página: esta línea debe ser la primera en el script
st.set_page_config(page_title="Mi Aplicación Streamlit")

port = os.getenv('PORT', 8501)

# Cargar los datos
car_data = pd.read_csv("https://raw.githubusercontent.com/Perrito-ing/Proyecto-6/refs/heads/main/vehicles_us.csv")
#st.write(car_data.head())  # Muestra las primeras filas del CSV para ver si se carga bien

# Crear los botones
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Botón de histograma presionado')
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

plotly_button = st.button('Construir gráfico de dispersión')
if plotly_button:
    st.write('Botón de gráfico de dispersión presionado')
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


#////////////////////////////////////////////////////////
#
#car_data = pd.read_csv("https://raw.githubusercontent.com/Perrito-ing/Proyecto-6/refs/heads/main/vehicles_us.csv") # leer los datos
#hist_button = st.button('Construir histograma') # crear un botón
        
#if hist_button: # al hacer clic en el botón
#    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
#    fig = px.histogram(car_data, x="odometer")
#    st.plotly_chart(fig, use_container_width=True)


#plotly_button = st.button('Construir grafico de dispersión') # crear un botón
        
#if plotly_button: # al hacer clic en el botón
#    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
#    fig = px.scatter(car_data, x="odometer")
#    st.plotly_chart(fig, use_container_width=True)


#fig = px.histogram(car_data, x="odometer") # crear un histograma
#fig.show() # crear gráfico de dispersión
