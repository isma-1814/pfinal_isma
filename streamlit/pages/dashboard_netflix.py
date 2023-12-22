import pandas as pd

import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_agg import RendererAgg

import requests
import seaborn as sns

@st.cache_data
def load_data(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    mijson = r.json()
    listado = mijson['valoraciones']
    df = pd.DataFrame.from_records(listado)
    return df

def info_box (texto, color=None):
    st.markdown(f'<div style = "background-color:#4EBAE1;opacity:70%"><p style="text-align:center;color:white;font-size:30px;">{texto}</p></div>', unsafe_allow_html=True)


matplotlib.use("agg")
lock = RendererAgg.lock


df = load_data('http://fastapi:8000/retrieve_data')

# Encabezado del Streamlit
st.title('Análisis de datos de películas/programas de TV en Netflix')

# Mostrar el DataFrame
st.write(df)


# Crear un histograma interactivo de las puntuaciones IMDb
st.header('Histograma Interactivo de Puntuaciones IMDb')
fig = px.histogram(df, x='imdb_score', marginal='rug')
st.plotly_chart(fig)


# Crear un gráfico de barras interactivo por año de lanzamiento
st.header('Gráfico de Barras Interactivo por Año de Lanzamiento')
fig = px.bar(df['release_year'].value_counts().reset_index(), x='release_year', y='count')
fig.update_layout(xaxis_title='Año', yaxis_title='Cantidad de Títulos')
st.plotly_chart(fig)


# Gráfico de caja interactivo para comparar las puntuaciones IMDb entre programas de TV y películas
st.header('Distribución de Puntuaciones IMDb por Tipo de Contenido')
fig = px.box(df, x='type', y='imdb_score', color='type')
fig.update_layout(xaxis_title='Tipo de Contenido', yaxis_title='Puntuación IMDb')
st.plotly_chart(fig)


# Gráfico de barras interactivas para visualizar la cantidad de títulos por calificación de certificación de edad
st.header('Cantidad de Títulos por Calificación de Certificación de Edad')
fig = px.bar(df['age_certification'].value_counts().reset_index(), x='count', y='age_certification')
fig.update_layout(xaxis_title='Cantidad de Títulos', yaxis_title='Calificación de Certificación de Edad')
st.plotly_chart(fig)


# Gráfico de líneas interactivas para mostrar la evolución de puntuaciones IMDb y votos a través de los años
st.header('Evolución de Puntuaciones IMDb y Votos a lo largo de los Años')
fig = px.line(df, x='release_year', y=['imdb_score', 'imdb_votes'], title='Puntuaciones IMDb y Votos a lo largo del Tiempo')
fig.update_layout(xaxis_title='Año de Lanzamiento', yaxis_title='Valor', legend_title='Variable')
st.plotly_chart(fig)
