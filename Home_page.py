import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

# ENCABEZADO: escudo Melgar + escudo Liga1
colA, colB, colC = st.columns([5, 1, 5])
with colA:
    pass
with colB:
    st.image('logo_atluniversidad.png', use_column_width=True)
with colC:
    #st.image('logo_copaperu.png', use_column_width=True)
    pass

#Lectura de datos
id_club = 4010101
df_clubs = pd.read_excel('db_club.xlsx')
dicc = df_clubs.set_index('id_club')['name_club'].to_dict()
name_club = dicc[id_club]

#FORMATO
st.header(f'Bienvenido, {name_club}!!')
st.write('RESULTADOS:')

df_resultados = pd.read_excel('Resultados_partidos.xlsx')
df_resultados = df_resultados.sort_values('fecha', ascending=False)

df_resultados['Resultado'] = df_resultados.apply(lambda row: '✅' if row['gol'] > row['gol_against'] else('➖' if row['gol']==row['gol_against'] else '❌'), axis=1)


dicc_ver_table = {'fecha':st.column_config.DateColumn('Fecha',format="DD/MM/YYYY"),
                    'id_distrito':None, 'id_club1':None, 'id_club2':None, 'name_club1':None, 'name_club2':'Rival',
                    'gol':'G', 'gol_against':'G_contra'}
st.dataframe(df_resultados, column_config=dicc_ver_table)


colD, colE, colF = st.columns([4, 4, 1])
with colD:
    pass
with colE:
    pass
with colF:
    st.image('logo-dirac.png', use_column_width=True)




