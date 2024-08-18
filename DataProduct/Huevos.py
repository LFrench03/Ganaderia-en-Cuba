import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go


with open('inventario_ganado.json',encoding = "utf8") as json_data: 
    data = json.load(json_data)  


#Producc huevos
produccion_huevos_total = data["aves"]["Produccion de huevos(MMU)"]["Total"]
produccion_huevos_estatal = data["aves"]["Produccion de huevos(MMU)"]["Empresas avicolas "]
produccion_huevos_NOestatal = {}

       
for year in produccion_huevos_total:
    if produccion_huevos_total[year] and produccion_huevos_estatal[year]:
        produccion_huevos_NOestatal[year] = round(float(produccion_huevos_total[year]) - float(produccion_huevos_estatal[year]), 1)

huevos = pd.DataFrame({
    "Estatal": produccion_huevos_estatal,
    "No Estatal": produccion_huevos_NOestatal,
    "Total": produccion_huevos_total,
})

huevos = huevos.apply(pd.to_numeric)



#Huevos x gallina
huevos_gallina = data["aves"]["Indicadores seleccionados de gallinas ponedoras"]["Huevos por gallina(U)"]
egg = pd.DataFrame({  
    "Huevos por gallina": huevos_gallina  
})


egg = egg.apply(pd.to_numeric)


#Carne de ave
produccion_carne = data["aves"]["Entregas a sacrificio"]["Empresas avicolas estatales"]["Produccion total de carne de ave"]

carneDF = pd.DataFrame({  
    "Producción de carne de ave": produccion_carne  
})


carneDF = carneDF.apply(pd.to_numeric)


fig = px.area(huevos,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
fig.update_layout(
                yaxis_title = "Cantidad", xaxis_title = "Años", 
                title = "Producción total de huevos (1989-2022)",
                legend=dict(
                    title=dict(text="Producción")
                )
                )

st.plotly_chart(fig)



col1, col2 = st.columns(2)

with col1:
    
    fig = px.line(egg,markers=True,color_discrete_sequence=["rgb(179,205,227)"])
    fig.update_layout(width=800, height=600, 
                    yaxis_title = "Cantidad", xaxis_title = "Años", 
                    title = "Cantidad de huevos por gallina producidos (1985-2022)",
                    
                    legend=dict(
                        title=dict(text="Tipo")
                    ),
                    showlegend=False
                    )
    st.plotly_chart(fig)


    
with col2:
    
    fig = px.line(carneDF,markers=True,color_discrete_sequence=["rgb(179,226,205)"])
    fig.update_layout(width=800, height=600, 
                    yaxis_title = "Cantidad", xaxis_title = "Años", 
                    title = "Producción de carne de ave (1985-2006)",
                    
                    legend=dict(
                        title=dict(text="Tipo")
                    ),
                    showlegend=False
                    )
    st.plotly_chart(fig)
 
 

