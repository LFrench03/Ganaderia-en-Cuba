import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go


with open('inventario_ganado.json',encoding = "utf8") as json_data: 
    data = json.load(json_data)  
  
#Leche de vaca (Total)   
st.header("Producción de leche de vaca en Cuba (1989-2022)")   

produccion_leche_total = data["vacuno"]["Indicadores produccion leche"]["Produccion(Mt)"]["Total"]
produccion_leche_estatal = data["vacuno"]["Indicadores produccion leche"]["Produccion(Mt)"]["Estatal"]
produccion_leche_NOestatal = data["vacuno"]["Indicadores produccion leche"]["Produccion(Mt)"]["No Estatal"]

produccionDF = pd.DataFrame({  
    "Estatal": produccion_leche_estatal,
    "No Estatal": produccion_leche_NOestatal,
    "Total": produccion_leche_total
})



produccionDF = produccionDF.apply(pd.to_numeric)


fig = px.area(produccionDF,markers=True)
fig.update_layout(width=800, height=600, 
                   yaxis_title = "Cantidad", xaxis_title = "Años", 
                   title = "Producción de leche de vaca (Total)",
                   legend=dict(
                    title=dict(text="Producción")
                   )
                 )


st.plotly_chart(fig)


#Leche de cabra (Total)   
st.header("Producción de leche de cabra en Cuba (1993-2011)")   

cabra_leche_total = data["ovino_caprino"]["Produccion de leche"]["Produccion de leche"]["Total"]
cabra_estatal = data["ovino_caprino"]["Produccion de leche"]["Produccion de leche"]["Estatal"]
cabra_NOestatal = {}

for year in cabra_leche_total:
    if cabra_leche_total[year] and cabra_estatal[year]:
        cabra_NOestatal[year] = round(float(cabra_leche_total[year]) - float(cabra_estatal[year]), 1)

cabraE_NE = pd.DataFrame({
    "Estatal": cabra_estatal,
    "No Estatal": cabra_NOestatal,
    "Total": cabra_leche_total,
})

cabraE_NE = cabraE_NE.apply(pd.to_numeric)

fig = px.area(cabraE_NE,markers=True)
fig.update_layout(width=800, height=600, 
                   yaxis_title = "Cantidad", xaxis_title = "Años", 
                   title = "Producción de leche de cabra (Total)",
                   legend=dict(
                    title=dict(text="Producción")
                   )
                 )
st.plotly_chart(fig)



#Vaca vs Cabra
st.header("¿Qué tipo de leche se ha producido más a lo largo de los años en Cuba?")  
vaca_cabra = pd.DataFrame({  
    "Leche de vaca": produccion_leche_total,
    "Leche de cabra": cabra_leche_total    
})


vaca_cabra = vaca_cabra.apply(pd.to_numeric)

fig = px.line(vaca_cabra,markers=True)
fig.update_layout(width=800, height=600, 
                   yaxis_title = "Cantidad", xaxis_title = "Años", 
                   title = "Comparación de la producción de leche de vaca y leche de cabra ",
                   
                   legend=dict(
                    title=dict(text="Tipo")
                   )
                   
                 )
st.plotly_chart(fig)

