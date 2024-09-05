import streamlit as st
import json

st.markdown('''
###    
    

\t Todos los datos utilizados han sido extraídos de la Oficina Nacional de Estadística e Información (ONEI), los cuales estaban estructurados en un formato de tipo csv, 
    para la realización del proyecto, por términos de comodidad y organización convertimos toda la información del formato csv a json, que puedes descargar desde aquí:
\t
''')


def descargar_json(ruta_archivo):
    with open(ruta_archivo, 'rb') as f:
        st.download_button(
            label="Descargar datos",
            data=f,
            file_name='inventario_ganado.json',
            mime='application/json'
        )
ruta = "D:\Ganaderia-en-Cuba-main\inventario_ganado.json"
descargar_json(ruta)