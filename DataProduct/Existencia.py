import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go

with open('inventario_ganado.json',encoding = "utf8") as json_data: 
    data = json.load(json_data)  
    

tab1, tab2, tab3 = st.tabs(["Existencia del ganado", "Entregas a sacrificio", "Natalidad y Mortalidad"])

with tab1:
    st.header("¿Qué tipo de ganado ha predominado en Cuba en el período de 1993-2022?")
    
       
    def mostrar(graf):
        st.plotly_chart(graf)
        
    opciones = st.selectbox( "Seleccione una opción", ["All", "Total", "Estatal", "No Estatal"],)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    vacuno = data["vacuno"]["Total"]  
    porcino = data["porcino"]["Existencia(Mcabz)"]["Total"]
    ovino_caprino = data["ovino_caprino"]["Existencia(Mcabz)"]["Total"]["Total"]
    aves = data["aves"]["Existencia(Mcabz)"]["Existencia total de aves"]
    equido = data["equido"]["Existencia(Mcabz)"]["Total"]
    
    ganado = pd.DataFrame({
        "Vacuno": vacuno,
        "Porcino": porcino,
        "Ovino Caprino": ovino_caprino,
        "Aves": aves,
        "Equido": equido
    })
    
    total = px.line(ganado,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
    total.update_layout(width=800, height=600, 
                    yaxis_title = "Cantidad", xaxis_title = "Años", 
                    title = "〽️ Distribución del ganado en Cuba",
                    
                    legend=dict(
                        title=dict(text="Tipo de ganado")
                    )
                        
                    )
    
    if opciones == "All":
        mostrar(a)
    if opciones == "Total":
        mostrar(total)

    # elif opciones == "Cherna":
    #     mostrar_grafica_sin(Cherna)
    # elif opciones == "Túnidos":
    #     mostrar_grafica_sin(tunidos)
    # elif opciones == "Bonito":
    #     mostrar_grafica_sin(bonitos)
    # elif opciones == "Biajaiba":
    #     mostrar_grafica_sin(biajaiba)











        
    # with st.container(border=True):
    #     ternerasH = data["vacuno"]["Hembras"]["Terneras"]
    #     annojasH = data["vacuno"]["Hembras"]["Añojas"]
    #     novillasH = data["vacuno"]["Hembras"]["Novillas"]
    #     vacasH = data["vacuno"]["Hembras"]["Vacas"]
        
    #     ternerosM = data["vacuno"]["Machos"]["Terneros"]
    #     annojaosM = data["vacuno"]["Machos"]["Añojos"]
    #     toretesM = data["vacuno"]["Machos"]["Toretes"]
    #     toros_cebaM = data["vacuno"]["Machos"]["Toros de ceba"]
    #     bueyesM = data["vacuno"]["Machos"]["Bueyes"]
    #     sementalesM = data["vacuno"]["Machos"]["Sementales"]
    #     receladoresM = data["vacuno"]["Machos"]["Receladores"]


    #     vacasDF = pd.DataFrame({

    #         "Terneras": ternerasH,
    #         "Añojas": annojasH,
    #         "Novillas": novillasH,
    #         "Vacas": vacasH,
             
           
    #         "Terneros": ternerosM,
    #         "Añojos": annojaosM,
    #         "Toretes": toretesM,
    #         "Toros de ceba": toros_cebaM,
    #         "Bueyes": bueyesM,
    #         "Sementales": sementalesM,
    #         "Receladores": receladoresM     
    #     })
        
       

    #     opciones = st.select_slider("Seleccione un año",[x for x in range (1985,2023)])
    #     def crear_grafica(year):
    #         fig = px.bar(vacasDF)
            
           
    #         return fig  


    #     st.plotly_chart(crear_grafica(opciones))




# if opciones == "Selecione una especie":
#             mostrar_grafica_sin(peces_sum_line)
#         if opciones == "Pargo":
#             mostrar_grafica_sin(pargo)
#         elif opciones == "Cherna":
#             mostrar_grafica_sin(Cherna)
#         elif opciones == "Túnidos":
#             mostrar_grafica_sin(tunidos)
#         elif opciones == "Bonito":
#             mostrar_grafica_sin(bonitos)
#         elif opciones == "Biajaiba":
#             mostrar_grafica_sin(biajaiba)
            
#                 def mostrar_grafica_sin(g):
#         g.update_layout(showlegend=False)
#         st.plotly_chart(g, use_container_width=True)








































# def mostrar(g):
#     st.plotly_chart(g)

# #Vacuno
# existencia_vacunosT = data["vacuno"]["Total"]


# existencia_vacas = pd.DataFrame({  
#     "Total": existencia_vacunosT
# })


# existencia_vacas = existencia_vacas.apply(pd.to_numeric)


# vacuno = px.area(existencia_vacas,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
# vacuno.update_layout(width=1000, height=600, 
#                    yaxis_title = "Cantidad", xaxis_title = "Años", 

#                    legend=dict(
#                     title=dict(text="Tipo")
#                    )
                   
#                  )

# #Porcino
# existencia_porcinosT = data["porcino"]["Existencia(Mcabz)"]["Total"]
# existencia_porcinosE = data["porcino"]["Existencia(Mcabz)"]["Estatal"]
# existencia_porcinosNE = {}

# for year in existencia_porcinosT:
#     if existencia_porcinosT[year] and existencia_porcinosE[year]:
#         existencia_porcinosNE[year] = round(float(existencia_porcinosT[year]) - float(existencia_porcinosE[year]), 1)
        
# existencia_cerdos = pd.DataFrame({  
#     "Total": existencia_porcinosT,
#     "Estatal": existencia_porcinosE,
#     "No Estatal": existencia_porcinosNE
# })


# existencia_cerdos = existencia_cerdos.apply(pd.to_numeric)


# porcino = px.area(existencia_cerdos,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
# porcino.update_layout(width=1000, height=600, 
#                    yaxis_title = "Cantidad", xaxis_title = "Años", 

#                    legend=dict(
#                     title=dict(text="Tipo")
#                    )
                   
#                  )


# #Ovino Caprino
# existencia_o_cT = data["ovino_caprino"]["Existencia(Mcabz)"]["Total"]["Total"]
# existencia_o_cE = data["ovino_caprino"]["Existencia(Mcabz)"]["Estatal"]["Total"]
# existencia_o_cNE = {}

# for year in existencia_o_cT:
#     if existencia_o_cT[year] and existencia_o_cE[year]:
#         existencia_o_cNE[year] = round(float(existencia_o_cT[year]) - float(existencia_o_cE[year]), 1)
        
# existencia_OC = pd.DataFrame({  
#     "Total": existencia_o_cT,
#     "Estatal": existencia_o_cE,
#     "No Estatal": existencia_o_cNE
# })


# existencia_OC = existencia_OC.apply(pd.to_numeric)


# oc = px.area(existencia_OC,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
# oc.update_layout(width=1000, height=600, 
#                    yaxis_title = "Cantidad", xaxis_title = "Años", 

#                    legend=dict(
#                     title=dict(text="Tipo")
#                    )
                   
#                  )