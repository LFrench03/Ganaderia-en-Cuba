import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go


with open('inventario_ganado.json',encoding = "utf8") as json_data: 
    data = json.load(json_data)  

#Vacas de ordenno    
vacas_ordenno_E = data["vacuno"]["Indicadores produccion leche"]["Existencia promedio de vacas de ordeño(Mcabz)"]["Estatal"]
vacas_ordenno_NE = data["vacuno"]["Indicadores produccion leche"]["Existencia promedio de vacas de ordeño(Mcabz)"]["No Estatal"]
vacas_ordenno_T = data["vacuno"]["Indicadores produccion leche"]["Existencia promedio de vacas de ordeño(Mcabz)"]["Total"]


vacas_ordennoDF = pd.DataFrame({    
    "No Estatal": vacas_ordenno_NE,
    "Estatal": vacas_ordenno_E,    
    "Total": vacas_ordenno_T,
})

    
vacas_ordennoDF = vacas_ordennoDF.apply(pd.to_numeric)


opciones = st.select_slider("Seleccione un año",[x for x in range (1989,2023)])
colors = ['#EEEDEB', '#E0CCBE', '#AF8F6F']
def crear_grafica(year):
    fig = go.Figure(data = go.Pie(labels=["No Estatal", "Estatal", "Total"], values = vacas_ordennoDF.loc[str(year)]))
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='black', width=1.5)))
    fig.update_layout(
    title_text="Existencia promedio de vacas de ordeño (Miles por cabeza)",
    width=1300,  
    height=500,  
    margin=dict(l=100, r=100, t=100, b=100)
)
    return fig  

st.plotly_chart(crear_grafica(opciones))


#Cabras de ordenno
cabra_ordennoT = data["ovino_caprino"]["Produccion de leche"]["Cabras de ordeño"]["Ttotal"]
cabra_ordennoE = data["ovino_caprino"]["Produccion de leche"]["Cabras de ordeño"]["Estatal"]
cabra_ordennoNE = {}

for year in cabra_ordennoT:
    if cabra_ordennoT[year] and cabra_ordennoE[year]:
        cabra_ordennoNE[year] = round(float(cabra_ordennoT[year]) - float(cabra_ordennoE[year]), 1)

cabra_ordennoDF = pd.DataFrame({
    "No Estatal": cabra_ordennoNE,
    "Estatal": cabra_ordennoE,
    "Total": cabra_ordennoT,
})

cabra_ordennoDF = cabra_ordennoDF.apply(pd.to_numeric)


opciones1 = st.select_slider("",[x for x in range (1993,2012)])
colors = ['#EEEDEB', '#C7C8CC', '#A9A9A9']
def crear_grafica(year):
    fig = go.Figure(data = go.Pie(labels=["No Estatal", "Estatal", "Total"], values = vacas_ordennoDF.loc[str(year)]))
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='black', width=1.5)))
    fig.update_layout(
    title_text="Existencia promedio de cabras de ordeño (Miles por cabeza)",
    width=2000,  
    height=500,  
   
)
    return fig  

st.plotly_chart(crear_grafica(opciones1))



#Ordenno vacas vs cabras
st.header("Existencia promedio de vacas y cabras de ordeño (Miles por cabeza)")

ordenno_cabras_vacasDF = pd.DataFrame({
    "Vacas" : vacas_ordenno_T,
    "Cabras": cabra_ordennoT,
})

ordenno_cabras_vacasDF = ordenno_cabras_vacasDF.apply(pd.to_numeric)

val = ordenno_cabras_vacasDF.values
list(val)



opciones2 = st.select_slider("  ",[x for x in range (1993,2012)])


def crear_grafica(year):
    
    fig = px.bar(ordenno_cabras_vacasDF.loc[str(year)])
    fig.update_layout(width=600, height=600, 
                   yaxis_title = "Cantidad", xaxis_title = "Tipo de ganado",             
                   legend=dict(
                    title=dict(text="Año")
                   )   ,
                   showlegend=False
                 )
    fig.update_traces(width=0.4,
                      marker_line_color="black",
                      marker_line_width=1.5, opacity=0.6)
    fig.data[0].marker.color = ["#AF8F6F", "#A9A9A9"]
    
    return fig  


st.plotly_chart(crear_grafica(opciones2))

