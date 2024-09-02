import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go


with open('inventario_ganado.json',encoding = "utf8") as json_data: 
    data = json.load(json_data)  
  
tab1, tab2, tab3 = st.tabs(["Producción de leche", "Ganado de Ordeño", "Producción avícola"])



with tab1:
    #Leche de vaca (Total)   
    st.header("Producción de leche de vaca en Cuba (1989-2022)")   

    produccion_leche_total = data["vacuno"]["Indicadores produccion leche"]["Produccion(Miles de litros)"]["Total"]
    produccion_leche_estatal = data["vacuno"]["Indicadores produccion leche"]["Produccion(Miles de litros)"]["Estatal"]
    produccion_leche_NOestatal = data["vacuno"]["Indicadores produccion leche"]["Produccion(Miles de litros)"]["No Estatal"]

    produccionDF = pd.DataFrame({  
        "Estatal": produccion_leche_estatal,
        "No Estatal": produccion_leche_NOestatal,
        "Total": produccion_leche_total
    })



    produccionDF = produccionDF.apply(pd.to_numeric)


    fig = px.area(produccionDF,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
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

    cabra_leche_total = data["ovino_caprino"]["Produccion de leche"]["Produccion de leche(litros)"]["Total"]
    cabra_estatal = data["ovino_caprino"]["Produccion de leche"]["Produccion de leche(litros)"]["Estatal"]
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

    fig = px.area(cabraE_NE,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
    fig.update_layout(width=800, height=600, 
                    yaxis_title = "Cantidad", xaxis_title = "Años", 
                    title = "Producción de leche de cabra (Total)",
                    legend=dict(
                        title=dict(text="Producción")
                    ),
                
                    )
    st.plotly_chart(fig)



    #Vaca vs Cabra
    st.header("¿Qué tipo de leche se ha producido más a lo largo de los años en Cuba?")  
    vaca_cabra = pd.DataFrame({  
        "Leche de vaca": produccion_leche_total,
        "Leche de cabra": cabra_leche_total    
    })


    vaca_cabra = vaca_cabra.apply(pd.to_numeric)

    fig = px.line(vaca_cabra,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
    fig.update_layout(width=800, height=600, 
                    yaxis_title = "Cantidad", xaxis_title = "Años", 
                    title = "Comparación de la producción de leche de vaca y leche de cabra ",
                    
                    legend=dict(
                        title=dict(text="Tipo")
                    )
                        
                    )
    st.plotly_chart(fig)


with tab2:
    st.header("Ganado de ordeño en Cuba")    
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
        title_text="Existencia promedio de vacas de ordeño (Miles de cabezas)",
        width=1300,  
        height=500,  
        margin=dict(l=100, r=100, t=100, b=100)
    )
        return fig  

    st.plotly_chart(crear_grafica(opciones))


    #Cabras de ordenno
    cabra_ordennoT = data["ovino_caprino"]["Produccion de leche"]["Cabras de ordeño(Cabezas)"]["Total"]
    cabra_ordennoE = data["ovino_caprino"]["Produccion de leche"]["Cabras de ordeño(Cabezas)"]["Estatal"]
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
        fig.update_layout( 
                    yaxis_title = "Cantidad", xaxis_title = "Tipo de ganado",             
                    legend=dict(
                        title=dict(text="Año")
                    )   ,
                    showlegend=False
                    )
        fig.update_traces(width=0.3,
                        marker_line_color="black",
                        marker_line_width=1.5, opacity=0.6)
        fig.data[0].marker.color = ["#AF8F6F", "#A9A9A9"]
            
        return fig  


    st.plotly_chart(crear_grafica(opciones2))
    
with tab3:  
    st.header("Produción avícola en Cuba") 
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