#!/usr/bin/python3

import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.graph_objects as go
from PIL import Image
from streamlit import components

# Configuración básica de Streamlit
st.set_page_config(page_title="Football Dashboard", page_icon="⚽", layout="wide")

# Función para cargar datos
@st.cache_data
def load_data(file_path, delimiter=';', encoding='utf-8'):
    return pd.read_csv(file_path, delimiter=delimiter, encoding=encoding)

# Cargar archivos CSV
try:
    fixture = load_data('data/tps/tpsresults.csv', delimiter=',', encoding='latin1')
    equipo = load_data('data/tps/tpsteam.csv', delimiter=',', encoding='latin1')
    jugador = load_data('data/tps/tpsplayer.csv', delimiter=';', encoding='latin1')
    profile = load_data('data/tps/profile.csv', delimiter=',', encoding='latin1')
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
        color:#0000FF;
    }
    .sub-title {
        font-size:30px;
        text-align:center;
        color:#0000FF;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h1 class="main-title">Mariano Galeano</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-title">Season 2022/2023</h2>', unsafe_allow_html=True)



option = st.sidebar.selectbox(
    "2022 - TPS Turku",
    ("Games played", "Squad", "Player statistics")
)

if st.sidebar.button("Career"):
    
    
    # Crear las columnas para el radar chart y datos personales
    col1, col2 = st.columns([2, 1])
    
    # Columna izquierda para el radar chart
    with col1:
        # Leer el dataset
        dataset = pd.read_csv('data/tps/profile.csv', delimiter=",", encoding='utf-8')
        
        if 'Name' in dataset.columns:
            data = dataset[dataset['Name'] == 'Mariano Galeano']
            data = data.iloc[:, 1:]
             
            # Obtener los nombres de los atributos y los valores
            atributos = list(data.columns)
            values = data.values.flatten().tolist()
            values += values[:1]
            atributos += [atributos[0]]
            
            # Crear el Radar Chart
            fig = go.Figure(data=go.Scatterpolar(r=values, theta=atributos, fill='toself', text=atributos))
            
            # Personalizar el diseño del gráfico
            fig.update_layout(title='Perfil', polar=dict(radialaxis=dict(visible=True, range=[0, 20])))
            
            # Mostrar el gráfico en Streamlit
            st.plotly_chart(fig)
    
    # Columna derecha para los datos personales
    with col2:
        st.markdown("""
        <br>
        <br>
        <br>
        <br>
        <br>
                                                                                
        **Argentina**<br>
        Atfa Pro<br>
        H: 1.87<br>
        W: 85 kg<br>                        
        Age: 41<br>
        """, unsafe_allow_html=True)

    # Sección para la trayectoria de clubes
    st.markdown("""
    ### Trayectoria de Clubes
    #### 2022 Turun Palloseura- TPS Turku
    - Head Coach. Reserve team – U23
    - Sports Director: Mika Laurikainen. Contact: mika.laurikainen@tps.fi
    - Games: 22. Win 10 – Draw 5 – Loses 7. Average: 1.64 
    - Turku, Finland.
    
    #### 2021 Oulun Työväen Palloilijat - OTP Oulu
    - Head coach. First team
    - Games: 20. Win 9 – Draw 4 – Loses 7. Average: 1.55 
    - Top 50 – Best Argentinean coaches in foreign countries.
    - Oulu, Finland.
    
    #### 2018-19 Chongqing Dangdai Lifan FC.
    - Head coach. U-17
    - Champion League Chongqing regional 2018.
    - Chongqing, China.
    
    #### 2017 Maradona International Brand
    - Head coach. Youth team. Football Clinics.
    - Chongqing, China.
    
    #### 2016 UTC Cajamarca. Reserve Team
    - Head Coach: Pepo Salas
    - Assistant coach.
    - Cajamarca, Perú
    
    #### 2015 Club Deportivo Cuenca. First Team.
    - Head Coach: Alex Aguinaga
    """)

    # Sección para el porcentaje de puntos
    st.markdown("### Porcentaje de Puntos")
    
    # Crear un gráfico de barras
    colors = ['lightslategray'] * 5
    colors[2] = 'yellow'
    
    fig1 = go.Figure(data=[go.Bar(
        x=['Platense', 'Deportivo Cuenca', 'Chongqing Dangdai', 'OTP Oulu', 'TPS Turku'],
        y=[45, 53, 70, 63, 58],
        marker_color=colors
    )])
    
    fig1.update_layout(title_text='% Porcentaje de puntos')
    
    # Mostrar el gráfico de barras en Streamlit
    st.plotly_chart(fig1)


else:
    if option == "Games played":
        st.header("Schedule | Resultados de Partido")
        st.dataframe(fixture)
        
        # Mostrar estadísticas de resultados
        if 'Final Result' in fixture.columns:
            st.subheader("Estadísticas de Resultados")
            wins, draws, losses = categorize_results(fixture, 'Final Result') # planilla + columna de argumento
            st.write(f"Partidos ganados: {wins}")
            st.write(f"Partidos empatados: {draws}")
            st.write(f"Partidos perdidos: {losses}")

            st.subheader("Gráfico de Resultados")
            labels = ['Ganados', 'Empatados', 'Perdidos']
            values = [wins, draws, losses]

            # Crear el gráfico de pastel
            fig1 = go.Figure(data=[go.Pie(labels=labels, values=values)])
            st.plotly_chart(fig1)

    elif option == "Squad":
        st.header("Squad - TPS U-23")
        st.dataframe(equipo)
    elif option == "Player statistics":
        st.header("Mins played by player")
        st.dataframe(jugador)
    
        # Gráfico de minutos jugados por jugador
        st.subheader("Gráfico de Minutos Jugados por Jugador")
        fig, ax = plt.subplots()
        sns.barplot(x='Name', y='Mins', data=jugador, ax=ax)
        plt.xticks(rotation=90)
        st.pyplot(fig)


    
        # Radar chart
        selected_player = st.selectbox("Selecciona un jugador", jugador['Name'])

        # Filtra los datos para el jugador seleccionado
        player_data = jugador[jugador['Name'] == selected_player].drop('Name', axis=1).values.flatten()
        # Ajusta los valores para que estén en el rango de 0 a 100 minutos
        player_data = np.clip(player_data, 0, 100)
        # Preparar los datos para el radar chart
        categories = jugador.columns[1:]
        N = len(categories)
        values = player_data.tolist()
        values += values[:1]  # Para cerrar el gráfico

        angles = [n / float(N) * 2 * np.pi for n in range(N)]
        angles += angles[:1]

        # Crear el radar chart

        # Radar chart
        st.subheader("Minutos Jugados por Partido")


        

       # Crear el radar chart
        st.subheader("Minutos Jugados por Partido")
        fig, ax = plt.subplots(subplot_kw=dict(polar=True))
        ax.fill(angles, values, color='b', alpha=0.25)
        ax.plot(angles, values, color='b', linewidth=2)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)
        ax.set_title(f"Minutos Jugados por {selected_player}")
        st.pyplot(fig)

if st.sidebar.button("Blog"):
    st.write('<meta http-equiv="refresh" content="0;URL=https://marianogaleano7.wordpress.com/blog/" />', unsafe_allow_html=True) 



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
