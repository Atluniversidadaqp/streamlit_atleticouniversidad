import streamlit as st
import numpy as np
import pandas as pd
from Home_page import name_club, id_club
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from mplsoccer import (VerticalPitch, Pitch, create_transparent_cmap,
                       FontManager, arrowhead_marker, Sbopen)

#url_powerbi = '<iframe title="Plataforma Dirac v1.1" width="900" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiOWM0YmNkMGEtMzc4Ni00MTI4LTk0OGEtZmFhNzc5NTZiYTkxIiwidCI6IjBlMGNiMDYwLTA5YWQtNDlmNS1hMDA1LTY4YjliNDlhYTFmNiIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>'
#st.markdown(url_powerbi, unsafe_allow_html=True)

#----------------------
# Configurar la página para usar el ancho completo
st.set_page_config(layout="wide")

st.title(f'⚽ {name_club}')

#--------------    LECTURA Y LIMPIEZA DE DATOS DE EVENTOS -----------
df = pd.read_excel('Eventos_acumulados.xlsx')
#Añadir columna con segundos totales
df['seg_clic'] = df['Mins']*60 + df['Secs']
df['seg_star'] = df['seg_clic']-2
df['seg_end'] = df['seg_clic']+6
#Añadir columna con el tercio del campo
bins = [float('-inf'), 30, 70, float('inf')]
labels = ["1er tercio", "2do tercio", "3er tercio"]
df['zone'] = pd.cut(df['X'], bins=bins, labels=labels) #nueva columna usando pd.cut
#Excluir algunos eventos
df = df[~df['Event'].isin(['Pase_correcto', 'Pase_recibido', 'Pase_error','Presion', 'Lateral'])]
#
df['x'] = df['X']*1.2
df['y'] = df['Y']*0.8

# ------------- FUNCION GRAFICO --------------------------
def graph_barras(metrica, color):
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=df_stats['partido'],
            y=df_stats[metrica],
            marker_color=color,
            text=df_stats['rival'],
            name='valor'
        )
    )
    # Crear el gráfico de líneas
    fig.add_trace(
        go.Scatter(
            x=df_stats['partido'],
            y=[df_stats[metrica].mean()] * df_stats.shape[0],
            name='media',
            marker_color='red',
            mode='lines'
        )
    )
    # Personalizar el layout del gráfico
    fig.update_layout(
        width=350,
        height=280,
        title= f'Evolución {metrica}',
        #xaxis_title='Rivales',
        #yaxis_title='Cantidad',
    )
    st.plotly_chart(fig)
#------------------------------------------------------------

#----------------------- MENU LATERAL
menu_miclub = ['Rendimiento','Partidos','Análisis']
choice = st.sidebar.radio("Submenú - Mi club", menu_miclub, 2) #el 2 es el indice de la opcion por defecto

# Mostrar contenido basado en la elección del menu
#---------  VIDEOS DE LOS PARTIDOS COMPLETOS ---------
if choice == "Partidos":

    col11, col12, col13, col14= st.columns([1, 1, 1, 1])
    with col11:
        st.write('Liguilla _ vs Cantolao')
        #st.video("Atletico vs Cantolao - Liguilla fecha 2.MP4")
        st.video("https://www.youtube.com/watch?v=L_1jOs7mrNA")
    with col12:
        st.write('Liguilla _ vs Max Uhle')
        #st.video("Atletico vs Max Uhle - Liguilla fecha 1.MP4")
        st.video("https://www.youtube.com/watch?v=YwVLhyPjVlU")
    with col13:
        st.write('Fecha 9 _ vs White Star')
    with col14:
        st.write('Fecha 8 _ vs Max Uhle')
        #st.video("Atletico vs Max Uhle - fecha 8.MP4")
        st.video("https://www.youtube.com/watch?v=Ez9Io1DJlZI")
    
    col21, col22, col23, col24= st.columns([1, 1, 1, 1])
    with col21:
        st.write('Fecha 6 (2do tiempo) _ vs Huracancito')
        st.video("https://youtu.be/sw-12B5snyY")
    with col22:
        st.write('Fecha 6 (1er tiempo) _ vs Huracancito')
        st.video("https://youtu.be/GTEex2hz_pA")
    with col23:
        st.write('Fecha 5 (2do tiempo) _ vs Cantolao')
        st.video("https://www.youtube.com/watch?v=uu6iYYFmqHE")
    with col24:
        st.write('Fecha 5 (1er tiempo) _ vs Cantolao')
        st.video("https://www.youtube.com/watch?v=mHzgtogfxB8")

# -------------- GRAFICOS DE ESTADISTICAS DEL EQUIPO ---------
elif choice == "Rendimiento":
    df_stats = pd.read_excel('stats_equipo.xlsx')

    col31, col32, col33= st.columns([1,1,1])
    with col31:
        graph_barras('pase_error', 'white')
    with col32:
        graph_barras('regate_error', 'blue')
    with col33:
        graph_barras('perdidas', 'red')

    col41, col42, col43= st.columns([1,1,1])
    with col41:
        graph_barras('tiros_al arco', 'yellow')
    with col42:
        graph_barras('regate_completado', 'pink')
    with col43:
        graph_barras('recuperaciones', 'green')

# ---------- ANALISIS DE EVENTOS SEGUN LA ZONA + VIDEO ------
elif choice == 'Análisis':
    
    # Barra lateral
    partidos = df.Match.unique()
    n_partid = len(partidos)
    events = df.Event.unique()
    zona = list(df.zone.unique())

    match = st.sidebar.selectbox(
        "Partido",
        partidos,
        0) #mostrar ultimo partido por defecto: n_partid-1
    type_event = st.sidebar.selectbox(
        "Evento",
        events,
        1)
    pitch_zone = st.sidebar.selectbox(
        "Zona del campo",
        ['Todo']+zona,
        0)
    #data
    df = df[df.Match==match]
    df = df[df.Event==type_event]
    if pitch_zone == 'Todo':
        pass
    else:
        df = df[df.zone==pitch_zone]   

    # ---------AÑADIR CAMPOGRAMA
    miscolores = [
    '#1f77b4',  # Azul
    '#ff7f0e',  # Naranja
    '#2ca02c',  # Verde
    '#d62728',  # Rojo
    '#9467bd',  # Púrpura
    '#8c564b',  # Marrón
    '#e377c2',  # Rosa
    '#7f7f7f',  # Gris
    '#bcbd22',  # Lima
    '#17becf',  # Cian
    '#1a1a1a',  # Negro
    '#ff00ff',  # Magenta
    '#00ffff',  # Cyan
    '#ffff00',  # Amarillo
    '#0000ff',  # Azul
    '#ff0000',  # Rojo
    '#008000',  # Verde
    '#800080',  # Púrpura
    '#008080',  # Teal
    '#800000'   # Marrón
    ]
    total_events = ['Pase_correcto', 'Pase_recibido', 'Regate_correcto', 'Pase_error',
       'Recuperacion', 'Carrera', 'Falta_recibida', 'Tiro_libre',
       'Tiro_fuera', 'Bloqueo', 'Saque_meta', 'Perdida', 'Regate_error',
       'Falta_realizada', 'Tiro_arco', 'Off-side', 'Corner', 'Presion',
       'Lateral', 'Tiro_bloqueado']
    color_map = dict(zip(total_events, miscolores))

    # Crear el campo de fútbol
    pitch = Pitch(pitch_color='grass', line_color='white', half=False)
    fig, ax = pitch.draw(figsize=(4, 3))
    # Graficar los eventos
    for event in df['Event'].unique():
        event_data = df[df['Event'] == event]
        pitch.scatter(event_data['x'], event_data['y'],
                    s=30, c=color_map[event], label=event, ax=ax)
    # Añadir leyenda
    plt.legend()
    plt.title('Eventos del Partido')
    st.pyplot(fig)


    #----- VISUALIZAR VIDEOS DE LOS EVENTOS SELECCIONADOS
    start_time_events = df[df.Event==type_event]['seg_star'].values
    end_time_events = df[df.Event==type_event]['seg_end'].values
    urls = df[df.Event==type_event]['Video'].values
    
    n_events = len(start_time_events)
    if pitch_zone != 'Todo':
        #for i in range(n_events):
        #    st.video(urls[i], start_time=star_time_events[i],
        #             end_time=end_time_events[i], loop=0, muted=0)
        for i in range(0, n_events, 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < n_events:
                    cols[j].video(urls[i + j], start_time=start_time_events[i + j], end_time=end_time_events[i + j], loop=0, muted=0)




