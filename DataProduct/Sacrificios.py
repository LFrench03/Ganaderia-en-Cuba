import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go

st.write("Existencia")

  

with open('inventario_ganado.json',encoding = "utf8") as json_data: 
    data = json.load(json_data)  


vacasT = data["vacuno"]["Sacrificios"]["Cabezas(M)"]["Total"]
vacasE = data["vacuno"]["Sacrificios"]["Cabezas(M)"]["Estatal"]
vacasNE = {}

for year in vacasT:
    if vacasT[year] and vacasE[year]:
        vacasNE[year] = round(float(vacasT[year]) - float(vacasE[year]), 1)



cerdosT = data["porcino"]["Entregas a sacrificio"]["Total"]["Cabezas(Mcabz)"]
cerdosE = data["porcino"]["Entregas a sacrificio"]["Total"]["Cabezas(Mcabz)"]["Total"]
cerdosNE = {}

for year in cerdosT:
    if cerdosT[year] and cerdosE[year]:
        cerdosNE[year] = round(float(cerdosT[year]) - float(cerdosE[year]), 1)
        

ocT = data["ovino_caprino"]["Entregas a sacrificio"]["Cantidad(Mcabz)"]["Total"]
ocE = data["ovino_caprino"]["Entregas a sacrificio"]["Cantidad(Mcabz)"]["Estatal"]
ocNE = {}

for year in ocT:
    if ocT[year] and ocE[year]:
        ocNE[year] = round(float(ocT[year]) - float(ocE[year]), 1)

avesT = data["aves"]["Entregas a sacrificio"]["Pollos de ceba entrega a sacrificio"]["Cantidad(Mcabz)"]


df = pd.Dataframe({
    "Vacas Estatal": vacasE,
    "Vacas No Estatal": vacasNE

    
})


# opciones = st.select_slider("Seleccione un año",[x for x in range (1993,2012)])

  
# def crear_grafica(year):
        
#     fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")
   
#     fig.data[0].marker.color = ["#AF8F6F", "#A9A9A9"]
        
#     return fig  


# st.plotly_chart(crear_grafica(opciones2))




