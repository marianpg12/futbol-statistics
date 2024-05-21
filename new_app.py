#!/usr/bin/python3

import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
from PIL import Image

# Configuración básica de Streamlit
st.set_page_config(page_title="Football Dashboard", page_icon="⚽", layout="wide")

# Función para cargar datos
@st.cache_data
def load_data(file_path, delimiter=';', encoding='utf-8'):
    return pd.read_csv(file_path, delimiter=delimiter, encoding=encoding)

# Cargar archivos CSV
try:
    fixture = load_data('data/tpsresults.csv', delimiter=';', encoding='latin1')
    equipo = load_data('data/tpsteam.csv', delimiter=';', encoding='latin1')
    jugador = load_data('data/tpsplayer.csv', delimiter=';', encoding='latin1')
except FileNotFoundError as e:
    st.error(f"Error cargando el archivo: {e}")


# Función para categorizar resultados
def categorize_results(dataframe, final_resultado):
    wins, draws, losses = 0, 0, 0
    for result in dataframe[final_resultado].dropna().astype(str):
        try:
            home_score, away_score = map(int, result.split('-'))
            if home_score > away_score:
                wins += 1
            elif home_score < away_score:
                losses += 1
            else:
                draws += 1
        except ValueError:
            continue
    return wins, draws, losses

# Título y subtítulo
st.markdown(
    """
    <style>
    .main-title {
        font-size:50px;
        font-weight:bold;
        text-align:center;
        color:#4CAF50;
    }
    .sub-title {
        font-size:30px;
        text-align:center;
        color:#2E7D32;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h1 class="main-title">Mariano Galeano</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-title">TPS U.23 - Season 2022</h2>', unsafe_allow_html=True)
st.write("Fecha actual...", datetime.date.today())

st.text("Dataset >> ")

option = st.sidebar.selectbox(
    "Selecciona una opción:",
    ("Resultados de Partido", "Plantel", "Minutos Jugados")
    )

if st.sidebar.button("Trayectoria"):
    st.header("Trayectoria")
    st.markdown("""
    ### Tu Nombre
    **Perfil**:
    - Entrenador de futbolistas profesionales.
    - Experiencia en diferentes paises

    **Trayectoria**:
    - Club A (20XX - 20XX): Descripción de tus responsabilidades y logros.
    - Club B (20XX - 20XX): Descripción de tus responsabilidades y logros.
    - Certificaciones y cursos relevantes.
    """)
else:
    if option == "Resultados de Partido":
        st.header("Schedule | Resultados de Partido")
        st.dataframe(fixture)
        
        # Mostrar estadísticas de resultados
        if 'Final Result' in fixture.columns:
            st.subheader("Estadísticas de Resultados")
            wins, draws, losses = categorize_results(fixture, 'Final Result') # planilla + columna de argumento
            st.write(f"Partidos ganados: {wins}")
            st.write(f"Partidos empatados: {draws}")
            st.write(f"Partidos perdidos: {losses}")

            # Gráfico de resultados
            st.subheader("Gráfico de Resultados")
            fig, ax = plt.subplots()
            ax.pie([wins, draws, losses], labels=['Ganados', 'Empatados', 'Perdidos'], autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            st.pyplot(fig)

    elif option == "Plantel":
        st.header("Plantel - TPS U-23 Season 2023")
        st.dataframe(equipo)
    elif option == "Minutos Jugados":
        st.header("Minutos Jugados por Jugador")
        st.dataframe(jugador)
    
    # Gráfico de minutos jugados por jugador
        st.subheader("Gráfico de Minutos Jugados por Jugador")
        fig, ax = plt.subplots()
        sns.barplot(x='Name', y='Mins', data=jugador, ax=ax)
        plt.xticks(rotation=90)
        st.pyplot(fig)
    
        # Radar chart
        # Selecciona un jugador para mostrar su gráfico
        selected_player = st.selectbox("Selecciona un jugador", jugador['Name'])

        # Filtra los datos para el jugador seleccionado
        player_data = jugador[jugador['Name'] == selected_player].drop('Name', axis=1).values.flatten()
        # Ajusta los valores para que estén en el rango de 0 a 100 minutos
        player_data = np.clip(player_data, 0, 100)
        # Preparar los datos para el radar chart
        categories = jugador.columns[1:]
        pi = int(3.14)
        N = len(categories)
        values = player_data.tolist()
        values += values[:1]  # Para cerrar el gráfico

        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        # Crear el radar chart
        # Radar chart
        st.subheader("Minutos Jugados por Partido")
        fig, ax = plt.subplots(subplot_kw=dict(polar=True))
        ax.fill(angles, values, color='b', alpha=0.25)
        ax.plot(angles, values, color='b', linewidth=2)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)
        ax.set_title(f"Minutos Jugados por {selected_player}")
        st.pyplot(fig)

st.text("Dataset >> ")

#dataset = pd.read_csv('data/fm2023.csv')
pd.set_option("styler.render.max_elements", 828296)
#st.dataframe(dataset, height=400)  # height para el scroll vertical


# Estilo de la página
st.markdown(
    """
    <style>
    .reportview-container {
        background: #F5F5F5;
    }
    .sidebar .sidebar-content {
        background: #2E7D32;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
