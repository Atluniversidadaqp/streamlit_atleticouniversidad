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
#SIN BALON
col11, col12, col13, col14= st.columns([1, 1, 1, 1])
with col11:
    st.write('Presión')
    st.video("Huracan_presion_ vs Cantolao.MP4")
with col12:
    st.write('Ocasiones en contra')
    st.video("Huracan_remates en contra_ vs Cantolao.MP4")
with col13:
    st.write('Corner en contra')
    st.video("Huracan_corner en contra_ vs Cantolao.MP4")
with col14:
    st.write('Tiro libre en contra')
    st.video("Huracan_tiro libre en contra_ vs Cantolao.MP4")

#CON BALON
col11, col12, col13, col14= st.columns([1, 1, 1, 1])
with col11:
    st.write('Salida (saque de meta)')
    st.video("Huracan_saque de meta_ vs Cantolao.MP4")
with col12:
    st.write('Remates a favor')
    st.video("Huracan_remates a favor_ vs Cantolao.MP4")
with col13:
    st.write('Corner a favor')
    st.video("Huracan_corner a favor_ vs Cantolao.MP4")
with col14:
    st.write('Tiro libre a favor')
    st.video("Huracan_tiro libre a favor_ vs Cantolao.MP4")
st.write("-------------------------------------")
#---------------------------
st.subheader('Fecha 2 liguilla _ Huracán vs Max Uhle')


