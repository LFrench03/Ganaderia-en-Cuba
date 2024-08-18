import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px


with open('inventario_ganado.json',encoding = "utf8") as json_data: 
    data = json.load(json_data)  

produccion_leche_total = data["vacuno"]["Indicadores produccion leche"]["Produccion(Mt)"]["Total"]
produccion_leche_estatal = data["vacuno"]["Indicadores produccion leche"]["Produccion(Mt)"]["Estatal"]
produccion_leche_NOestatal = data["vacuno"]["Indicadores produccion leche"]["Produccion(Mt)"]["No Estatal"]

produccionDF = pd.DataFrame({  
    "Estatal": produccion_leche_estatal,
    "No Estatal": produccion_leche_NOestatal,
    "Total": produccion_leche_total
})

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
produccionDF = produccionDF.apply(pd.to_numeric)
col1, col2 = st.columns(2)
with st.container():
    with col1:
        #Leche de vaca (Total) 
        fig = px.area(produccionDF, markers=True)
        fig.update_layout(width=800, height=600, 
                        yaxis_title = "Cantidad", xaxis_title = "Años", 
                        title = "Producción de leche de vaca (1989-2022)",
                        legend=dict(
                            title=dict(text="Producción")
                        )
                        )
        st.plotly_chart(fig)
    
    with col2:
        with st.expander("Contexto: "):
            st.write("Te la comes sin pretexto")

col1, col2 = st.columns(2)

with st.container():
    with col1: 
        #Leche de cabra (Total)   
        fig = px.area(cabraE_NE,markers=True)
        fig.update_layout(width=800, height=600, 
                        yaxis_title = "Cantidad", xaxis_title = "Años", 
                        title = "Producción de leche de cabra (1993-2011)",
                        legend=dict(
                            title=dict(text="Producción")
                        )
                        )
        st.plotly_chart(fig)

    with col2:
        with st.expander("Contexto: "):
            st.write("Te la comes sin pretexto")

vaca_cabra = pd.DataFrame({  
    "Leche de vaca": produccion_leche_total,
    "Leche de cabra": cabra_leche_total    
})

vaca_cabra = vaca_cabra.apply(pd.to_numeric)

col1, col2 = st.columns(2)

with st.container():
    with col1:
        fig = px.line(vaca_cabra,markers=True)
        fig.update_layout(width=800, height=600, 
                        yaxis_title = "Cantidad", xaxis_title = "Años", 
                        title = "Comparación de la producción de leche de vaca y leche de cabra ",
                        
                        legend=dict(
                            title=dict(text="Tipo")
                        )
                        
                        )
        st.plotly_chart(fig)
    with col2:
        with st.expander("Contexto: "):
            st.write("Te la comes sin pretexto")

data = {
    'Year': [2010, 2011, 2012, 2013],
    'Sales': [100, 120, 110, 130],
    'Profit': [50, 60, 55, 65]
}
df = pd.DataFrame(data)

df_melted = df.melt(id_vars='Year', var_name='Category', value_name='Value')



