import streamlit as st
import numpy as np
import pandas as pd

#url_powerbi = '<iframe title="Plataforma Dirac v1.1" width="900" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiOWM0YmNkMGEtMzc4Ni00MTI4LTk0OGEtZmFhNzc5NTZiYTkxIiwidCI6IjBlMGNiMDYwLTA5YWQtNDlmNS1hMDA1LTY4YjliNDlhYTFmNiIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>'
#st.markdown(url_powerbi, unsafe_allow_html=True)

#----------------------

st.title("Analisis de rival")

st.subheader('RIVAL: SPORTIVO HURACÁN')

#---------------------------
st.subheader('Fecha 1 liguilla _ Huracán vs Cantolao')

#--- LECTURA DE DATA
df_urls = pd.read_excel(urls.xlsx)
df_urls['nombre']=='Huracan_presion_ vs Cantolao'

#VIDEOS
#SIN BALON
col11, col12, col13, col14= st.columns([1, 1, 1, 1])
with col11:
    st.write('Presión')
    st.video(df_urls[df_urls['Nombre']=='Huracan presion vs Cantolao']['url'].values[0])
with col12:
    st.write('Ocasiones en contra')
    st.video(df_urls[df_urls['Nombre']=='Huracan remates en contra vs Cantolao']['url'].values[0])
with col13:
    st.write('Corner en contra')
    st.video(df_urls[df_urls['Nombre']=='Huracan corner en contra vs Cantolao']['url'].values[0])
with col14:
    st.write('Tiro libre en contra')
    st.video(df_urls[df_urls['Nombre']=='Huracan tiro libre en contra vs Cantolao']['url'].values[0])

#CON BALON
col11, col12, col13, col14= st.columns([1, 1, 1, 1])
with col11:
    st.write('Salida (saque de meta)')
    st.video(df_urls[df_urls['Nombre']=='Huracan saque de meta vs Cantolao']['url'].values[0])
with col12:
    st.write('Remates a favor')
    st.video(df_urls[df_urls['Nombre']=='Huracan remates a favor vs Cantolao']['url'].values[0])
with col13:
    st.write('Corner a favor')
    st.video(df_urls[df_urls['Nombre']=='Huracan corner a favor vs Cantolao']['url'].values[0])
with col14:
    st.write('Tiro libre a favor')
    st.video(df_urls[df_urls['Nombre']=='Huracan tiro libre a favor vs Cantolao']['url'].values[0])
st.write("-------------------------------------")
#---------------------------
st.subheader('Fecha 2 liguilla _ Huracán vs Max Uhle')


