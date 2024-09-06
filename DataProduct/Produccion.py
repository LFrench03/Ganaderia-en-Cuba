import streamlit as st
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go

@st.cache_data
def convert_df(df):
    return df.to_csv().encode("utf-8")

with open('inventario_ganado.json',encoding = "utf8") as json_data: #Cargar Json
    data = json.load(json_data)  
  
tab1, tab2, tab3 = st.tabs(["Producción de leche", "Producción avícola", "Alimentación del ganado"]) #Tabulaciones
with tab1:
    with st.container(border=True):   
        col1, col2 = st.columns(2)
        with col1:
            #Datos Leche de Vaca Total
            produccion_leche_total = data["vacuno"]["Indicadores produccion leche"]["Produccion(Miles de litros)"]["Total"]
            produccion_leche_estatal = data["vacuno"]["Indicadores produccion leche"]["Produccion(Miles de litros)"]["Estatal"]
            produccion_leche_NOestatal = data["vacuno"]["Indicadores produccion leche"]["Produccion(Miles de litros)"]["No Estatal"]

            #DataFrame Leche de Vaca Total
            produccionDF = pd.DataFrame({  
                "Estatal": produccion_leche_estatal,
                "No Estatal": produccion_leche_NOestatal
            })
            produccionDF = produccionDF.apply(pd.to_numeric)
            produccionDF.index.name = "Año"

            #Datos Leche de Vaca Total
            cabra_leche_total = data["ovino_caprino"]["Produccion de leche"]["Produccion de leche(litros)"]["Total"]
            cabra_estatal = data["ovino_caprino"]["Produccion de leche"]["Produccion de leche(litros)"]["Estatal"]
            cabra_NOestatal = {}
            for year in cabra_leche_total:
                if cabra_leche_total[year] and cabra_estatal[year]:
                    cabra_NOestatal[year] = round(float(cabra_leche_total[year]) - float(cabra_estatal[year]), 1)
            #DataFrame Leche de Vaca Total
            cabraE_NE = pd.DataFrame({
                "Estatal": cabra_estatal,
                "No Estatal": cabra_NOestatal
            })
            cabraE_NE = cabraE_NE.apply(pd.to_numeric)
            cabraE_NE.index.name = "Año"
            colors = ["rgb(0,87,214)","rgb(0,33,66)"]
            #Grafico de Area con Selectbox para especificar el Tipo de Leche
            st.markdown("### 🥛 Producción de leche en Cuba (1989-2022)")
            opcion = st.selectbox("Seleccione el Tipo de Leche", ["Leche de Vaca", "Leche de Cabra"])
            fig1 = px.area(produccionDF,markers=True,color_discrete_sequence=colors,hover_name='value', hover_data={'variable': None, 'value':None})
            fig1.update_layout(width=800, height=600,
                            yaxis_title = "Cantidad", xaxis_title = "Años", 
                            title = "🐄 Producción de leche de vaca (Miles de litros)",
                            legend=dict(title=dict(text="Producción")))
            
            fig2 = px.area(cabraE_NE,markers=True,color_discrete_sequence=colors,hover_name='value', hover_data={'variable': None, 'value':None})
            fig2.update_layout(width=800, height=600, 
                            yaxis_title = "Cantidad", xaxis_title = "Años", 
                            title = "🐐 Producción de leche de cabra (Litros)",
                            legend=dict(title=dict(text="Producción")))
            
            def mostrar(graf):
                st.plotly_chart(graf)
            if opcion == "Leche de Vaca":
                mostrar(fig1)
            if opcion == "Leche de Cabra":
                mostrar(fig2)
        with col2:        
            #Vacas de ordeño    
            vacas_ordenno_E = data["vacuno"]["Indicadores produccion leche"]["Existencia promedio de vacas de ordeño(Mcabz)"]["Estatal"]
            vacas_ordenno_NE = data["vacuno"]["Indicadores produccion leche"]["Existencia promedio de vacas de ordeño(Mcabz)"]["No Estatal"]
            vacas_ordenno_T = data["vacuno"]["Indicadores produccion leche"]["Existencia promedio de vacas de ordeño(Mcabz)"]["Total"]
            vacas_ordennoDF = pd.DataFrame({    
                "No Estatal": vacas_ordenno_NE,
                "Estatal": vacas_ordenno_E,    
            })
            #Cabras de ordenno
            cabra_ordennoT = data["ovino_caprino"]["Produccion de leche"]["Cabras de ordeño(Cabezas)"]["Total"]
            cabra_ordennoE = data["ovino_caprino"]["Produccion de leche"]["Cabras de ordeño(Cabezas)"]["Estatal"]
            cabra_ordennoNE = {}

            for year in cabra_ordennoT:
                if cabra_ordennoT[year] != cabra_ordennoE[year]:
                    cabra_ordennoNE[year] = round(float(cabra_ordennoT[year]) - float(cabra_ordennoE[year]), 1)

            cabra_ordennoDF = pd.DataFrame({
                "No Estatal": cabra_ordennoNE,
                "Estatal": cabra_ordennoE
            })

            cabra_ordennoDF = cabra_ordennoDF.apply(pd.to_numeric)
            vacas_ordennoDF = vacas_ordennoDF.apply(pd.to_numeric)
                
            #Datos Rendimiento Anual Vacas de Ordeño
            rendE = data["vacuno"]["Indicadores produccion leche"]["Rendimiento anual por vaca en ordeño(kg)"]["Estatal"]
            rendNE = data["vacuno"]["Indicadores produccion leche"]["Rendimiento anual por vaca en ordeño(kg)"]["No Estatal"]
            df = pd.DataFrame({
                "Estatal": rendE,
                "No Estatal": rendNE
            })
            df.apply(pd.to_numeric)
            df.index.name = "Año"
            #Grafico de Area para el Rendimiento Anual de Vacas de Ordeño
            st.markdown("### 🐄 Rendimiento anual de vacas de ordeño")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            fig = px.area(df,markers=True,color_discrete_sequence=colors,hover_name='value', hover_data={'variable': None, 'value':None})
            fig.update_layout(width=800, height=600,
                            yaxis_title = "Cantidad", xaxis_title = "Años",
                            title= "🥛 Kilogramos (Kg)", 
                            legend=dict(title=dict(text="Producción")))
            st.plotly_chart(fig)

        with st.expander("Observaciones"):
            st.markdown("- Si bien es cierto que los gráficos de área no están hechos para mostrar muchas áreas superpuestas, al representar los valores estatales y no estatales de esta forma se alcanza a visualizar un área total como suma de ambos.")
            st.markdown("- Y para un análisis individual más exacto se recomienda desactivar uno de los grupos en la leyenda.")
            st.markdown("- Producción de leche: Se considera toda la leche obtenida del ordeño, se excluye la mamada directamente de los terneros(as). En los casos que no se contó con toda la cobertura informativa se realizaron cálculos indirectos.")
            st.markdown("- Vacas de ordeño: Es el promedio de las vacas que se ordeñan y se obtiene sumando el número de vacas ordeñadas diariamente y dividiendo entre el número de días del período informado.")
            st.markdown("- Rendimiento anual de vacas de ordeño: Se determina dividiendo la producción anual de leche entre el número promedio de vacas de ordeño.")
            csv1_1 = convert_df(produccionDF)
            csv1_2 = convert_df(cabraE_NE)
            csv1_21 = convert_df(df)
            with st.popover("Descargar CSV"):
                st.download_button( 
                                label="Leche de Vaca",
                                data=csv1_1,
                                file_name="lechevaca.csv",
                                mime="text/csv")
                st.download_button( 
                                label="Leche de Cabra",
                                data=csv1_2,
                                file_name="lechecabra.csv",
                                mime="text/csv") 
                st.download_button( 
                                label="Rendimiento Vacas",
                                data=csv1_21,
                                file_name="vacas_rendimiento.csv",
                                mime="text/csv") 
               
        st.divider()

        st.markdown("### 🐄🐐  Existencia por tipos de ganado de ordeño")
        opciones = st.selectbox("Seleccione un grupo", ["Vacas de ordeño", "Cabras de ordeño"])

        def crear_grafica1(year):
            colors = ['#c560a0', '#4f2d57']
            fig = go.Figure(data = go.Pie(labels=["No Estatal", "Estatal"], values = vacas_ordennoDF.loc[str(year)],pull= 0.1, textposition="outside", hoverinfo='value',textinfo='label+percent', 
                                marker=dict(colors=colors, line=dict(color='black', width=3))))
            fig.update_layout(
            width=1300,  
            height=500,  
            margin=dict(l=100, r=100, t=100, b=100))
            return fig  
        
        def crear_grafica2(year):
            colors = ['#f5c47f', '#d1953e']
            fig = go.Figure(data = go.Pie(labels=["No Estatal", "Estatal"], values = cabra_ordennoDF.loc[str(year)],pull= 0.1, textposition="outside", hoverinfo='value',textinfo='label+percent', 
                                marker=dict(colors=colors, line=dict(color='black', width=3))))
            fig.update_layout(
            width=1300,  
            height=500,  
            margin=dict(l=100, r=100, t=100, b=100))
            return fig  
        
        if opciones == "Vacas de ordeño":
            opciones1 = st.select_slider("Año",[x for x in range (1989,2023)])
            st.markdown("###### 🐮 Existencia promedio de vacas de ordeño (Miles de cabezas)")
            st.plotly_chart(crear_grafica1(opciones1))

        if opciones == "Cabras de ordeño":
            opciones1 = st.select_slider("Año",[x for x in range (1993,2012)])
            st.markdown("###### 🐐 Existencia de cabras de ordeño (Cabezas)")
            st.plotly_chart(crear_grafica2(opciones1))

        with st.expander("Observaciones"):
            st.markdown("- En los primeros 8 años desde 1985 los datos que se tienen muestran que sólo existían valores estatales como total.")
            csv1_3 = convert_df(vacas_ordennoDF)
            csv1_4 = convert_df(cabra_ordennoDF)
            with st.popover("Descargar CSV"):
                st.download_button( 
                                label="Vacas de Ordeño",
                                data=csv1_3,
                                file_name="vacasordenno.csv",
                                mime="text/csv") 
                st.download_button( 
                                label="Cabras de Ordeño",
                                data=csv1_4,
                                file_name="df_cabras_ordenno.csv",
                                mime="text/csv")              
    with st.container(border=True):
        #Datos Importaciones Carne
        lechecondV = data["Importaciones"]["Leche condensada Valor (MP)"]
        lechecondC = data["Importaciones"]["Leche condensada Cantidad (t)"]
        lecheenpolvoV = data["Importaciones"]["Leche en polvo Valor (MP)"]
        lecheenpolvoC = data["Importaciones"]["Leche en polvo Cantidad (t)"]
        mantequillaV = data["Importaciones"]["Mantequilla Valor (MP)"]
        mantequillaC = data["Importaciones"]["Mantequilla Cantidad (t)"]
        quesoV = data["Importaciones"]["Queso y cuajada Valor (MP)"]
        quesoC = data["Importaciones"]["Queso y cuajada Cantidad (t)"]

        #DataFrames
        dfV = pd.DataFrame({
                "Leche condensada": lechecondV,
                "Leche en polvo" : lecheenpolvoV,
                "Mantqeuilla" : mantequillaV,
                "Queso" : quesoV
            })
        dfV.index.name = "Año"
        dfC = pd.DataFrame({
                "Leche condensada": lechecondC,
                "Leche en polvo" : lecheenpolvoC,
                "Mantqeuilla" : mantequillaC,
                "Queso" : quesoC
            })
        dfC.index.name = "Año"
        custom_colors = ["rgb(0,33,66)","rgb(0,87,214)","#8a8a8a","rgb(216,0,0)","#ad5514", "#c5d15d"] #Secuencia de colores
        #Grafico de Linea con selectbox
        st.markdown("#### 🥛 Valores de Importaciones de Lacteos Seleccionados por Tipos")
        opcion = st.selectbox("Seleccione un grupo", ["Valor", "Cantidad"])
        def graficar(opc):
            fig = px.line(opc,markers=True,color_discrete_sequence=custom_colors, hover_name='value', hover_data={'value':None})
            fig.update_layout(width=1200, height=600, 
                                yaxis_title = "Cantidad", xaxis_title = "Años",
                                legend=dict(title=dict(text="Tipo de Lacteo")))
            return fig
        if opcion == "Valor":
            st.markdown("###### Miles de Pesos (MP)")
            st.plotly_chart(graficar(dfV))
        if opcion == "Cantidad":
            st.markdown("###### Toneladas (T)")
            st.plotly_chart(graficar(dfC))
        with st.expander("Observaciones"):
            st.markdown("- Se incluyen estos valores por ser una de las fuentes más significativas de obtención de lácteos para la distribución en nuestro pais.")
            st.markdown("- En la leyenda se pueden elegir los valores que se muestren o no en la gráfica pulsando en la línea de color al lado del nombre del tipo de importación (si se pulsa dos veces se descartan el resto de valores y solo se muestra el pulsado de forma individual).")
            st.markdown("- En el cuerpo de la gráfica se muestra en los marcadores de cada pico para que se muestren los valores exactos en un cartel (tooltip).")    
            st.markdown("- De los datos sobre los pocos productos seleccionados para exportaciones sólo se tenía el valor por lo que se decidió no incluirlo en el dataproduct.")    
            csv2_1 = convert_df(dfV)
            csv2_2 = convert_df(dfC)
            with st.popover("Descargar CSV"):
                st.download_button( 
                                label="Valor",
                                data=csv2_1,
                                file_name="Valor.csv",
                                mime="text/csv")
                st.download_button( 
                                label="Cantidad",
                                data=csv2_2,
                                file_name="Cantidad.csv",
                                mime="text/csv") 

    
with tab2:
    with st.container(border=True):
        #Produccion huevos
        produccion_huevos_total = data["aves"]["Produccion de huevos(MMU)"]["Total"]
        produccion_huevos_estatal = data["aves"]["Produccion de huevos(MMU)"]["Empresas avicolas "]
        produccion_huevos_NOestatal = {}

        produccion_huevos_ponedoras = data["aves"]["Indicadores seleccionados de gallinas ponedoras"]["Produccion de huevos(MMU)"]
        produccion_huevos_otros = {}
        col1, col2 = st.columns(2)
        with col1:
                #Huevos x gallina
                st.markdown("#### 🥚🥩 Rendimiento de Producción de Huevos y Carne de Ave")
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
                choice = st.selectbox("Selecciona un grupo", ["Huevos por Gallina", "Producción Total de Carne"])
                if choice == "Huevos por Gallina":
                    df = egg
                    st.markdown("###### Miles de Millones de Unidades (MMU)")
                    color = ["#ec7416"]
                else:
                    df = carneDF
                    st.markdown("###### Miles de Toneladas (Mt)")
                    color = ["#e21616"]
                df.index.name = "Año"
                fig = px.line(df,markers=True,color_discrete_sequence=color, hover_name='value', hover_data={'variable': None, 'value':None})
                fig.update_layout(width=800, height=600, 
                                    yaxis_title = "Cantidad", xaxis_title = "Años",showlegend = False)
                st.plotly_chart(fig)
        with col2:
            for year in produccion_huevos_total:
                if produccion_huevos_total[year] != produccion_huevos_estatal[year]:
                    produccion_huevos_NOestatal[year] = round(float(produccion_huevos_total[year]) - float(produccion_huevos_estatal[year]), 1)
            for year in produccion_huevos_total:
                if produccion_huevos_total[year] and produccion_huevos_ponedoras[year]:
                    produccion_huevos_otros[year] = round(float(produccion_huevos_total[year]) - float(produccion_huevos_ponedoras[year]), 1)
            huevos = pd.DataFrame({
                "Empresas Avicolas": produccion_huevos_estatal,
                "Otros": produccion_huevos_NOestatal,
            })
            huevos = huevos.apply(pd.to_numeric)

            ponedoras = pd.DataFrame({
                "Aves Ponedoras": produccion_huevos_ponedoras,
                "Otros": produccion_huevos_otros
            })
            st.markdown("#### 🥚 Producción de Huevos")
            
            choice = st.selectbox("Seleccione un grupo", ["Total", "Empresas Avícolas"])
            year = st.select_slider("Año ", [x for x in range(1989, 2023)])
            st.markdown("###### Miles de Millones de Unidades (MMU)")
            if choice == "Total":
                def crear_grafica(year):
                    colors = ["#e4e42d","#deaa49"]
                    fig = go.Figure(data=go.Pie(labels=["Empresas Avicolas", "Otros"], values= huevos.loc[str(year)], pull = 0.1, textposition="outside", hoverinfo="value", textinfo='label+percent',
                                                marker=dict(colors=colors, line = dict(color='black', width=3))))
                    fig.update_layout(width=1300,  height=500,  margin=dict(l=100, r=100, t=100, b=100))
                    return fig 
            else:
                def crear_grafica(year):
                    colors = ["#e4e42d","#deaa49"]
                    fig = go.Figure(data=go.Pie(labels=["Aves Ponedoras", "Otros"], values= ponedoras.loc[str(year)], pull = 0.1, textposition="outside", hoverinfo="value", textinfo='label+percent',
                                                marker=dict(colors=colors, line = dict(color='black', width=3))))
                    fig.update_layout(width=1300,  height=500,  margin=dict(l=100, r=100, t=100, b=100))
                    return fig 
            st.plotly_chart(crear_grafica(year))
        with st.expander("Observaciones"):
            st.markdown("- Producción de huevos: Se considera como tal todos los que se obtengan de las aves independientemente de su destino, calidad, tamaño o estado (sano, cascado o roto).")
            st.markdown("- Huevos por gallina: Es el resultado de dividir la producción de gallinas ponedoras entre la existencia promedio de ponedoras.")
            csv3_1 = convert_df(carneDF)
            csv3_2 = convert_df(egg)
        
            with st.popover("Descargar CSV"):
                st.download_button( 
                                    label="Carne",
                                    data=csv3_1,
                                    file_name="carne.csv",
                                    mime="text/csv")
                st.download_button( 
                                    label="Huevos",
                                    data=csv3_2,
                                    file_name="huevos.csv",
                                    mime="text/csv")             

with tab3:
    with st.container(border=True):
        pienso_por_ave = data["aves"]["Indicadores seleccionados de gallinas ponedoras"]["Pienso consumido por ave(kg)"]
        pienso_to_huevo = data["aves"]["Indicadores seleccionados de gallinas ponedoras"]["Conversion de pienso en huevo(g)"]
        exist_prom= data["aves"]["Indicadores seleccionados de gallinas ponedoras"]["Existencia promedio(Mcabz)"]
        prod_huevo= data["aves"]["Indicadores seleccionados de gallinas ponedoras"]["Produccion de huevos(MMU)"]
        df1 = pd.DataFrame({"Pienso consumido por Ave (Kg)":pienso_por_ave,
                            "Existencia Promedio (MCabz)": exist_prom})
        df2 = pd.DataFrame({"Pienso en Huevo (g)":pienso_to_huevo,
                            "Producción de huevos(MMU)": prod_huevo})
        df1.index.name = "Año"
        df2.index.name = "Año"
        st.markdown("#### 🐓🥚 Relaciones de consumo de pienso en aves")
        with st.popover("Filtrado de datos"):
            val = st.selectbox("Seleccione", ["Pienso por Ave", "Pienso en Huevo"])
        if val == "Pienso por Ave":
            toggle = st.toggle("Intercambiar valores")
            if toggle:
                st.markdown("###### Tamaño : Existencia Promedio (MCabz)")
                fig = px.scatter(df1, size="Existencia Promedio (MCabz)", color_discrete_sequence=["#d3b003"],hover_name='value', hover_data={'variable':None,'value':None})
                fig.update_layout(width=1200, height=600,xaxis_title="Años",
                                    yaxis_title = "Cantidad (Kg)",
                                    legend=dict(title=dict(text="Eje Y")))
            else:
                st.markdown("###### Tamaño : Pienso consumido por Ave (Kg)")
                fig = px.scatter(df1, size="Pienso consumido por Ave (Kg)", color_discrete_sequence=["#c81919"],hover_name='value', hover_data={'variable':None,'value':None})
                fig.update_layout(width=1200, height=600,
                                    yaxis_title = "Cantidad (MCabz)",xaxis_title="Años",
                                    legend=dict(title=dict(text="Eje Y")))
            st.plotly_chart(fig)
        else:
            toggle = st.toggle("Intercambiar valores")
            if toggle:
                st.markdown("###### Tamaño : Producción de huevos(MMU)")
                fig = px.scatter(df2, size="Producción de huevos(MMU)", color_discrete_sequence=["#ffe165"],hover_name='value', hover_data={'variable':None,'value':None})
                fig.update_layout(width=1200, height=600,
                                    yaxis_title = "Cantidad (g)",
                                    legend=dict(title=dict(text="Eje Y")))
            else:
                st.markdown("###### Tamaño : Pienso en Huevo (g)")
                fig = px.scatter(df2, size="Pienso en Huevo (g)", color_discrete_sequence=["#ff6565"],hover_name='value', hover_data={'variable':None,'value':None})
                fig.update_layout(width=1200, height=600,
                                    yaxis_title = "Cantidad (MMU)",
                                    legend=dict(title=dict(text="Eje Y")))
            st.plotly_chart(fig)
        with st.expander("Observaciones"):
            st.markdown("- Conversión de pienso en huevo: Es el resultado de dividir el consumo de pienso de ponedoras entre la producción de huevos de ponedoras.")
            st.markdown("- Pienso consumido por ave: Es el resultado de dividir el consumo de pienso de las aves entre la existencia promedio.")
            st.markdown("- Al activar el interruptor el parámetro correspondiente al tamaño de las burbujas del gráfico de dispresión y los valores asignados al eje Y se intercambian.")
            csv4_1 = convert_df(df1)
            csv4_2 = convert_df(df2)
        
            with st.popover("Descargar CSV"):
                st.download_button( 
                                    label="Pienso por Ave",
                                    data=csv4_1,
                                    file_name="Pienso_por_ave.csv",
                                    mime="text/csv")
                st.download_button( 
                                    label="Pienso en Huevo",
                                    data=csv4_2,
                                    file_name="Pienso_en_huevo.csv",
                                    mime="text/csv")              
        
    with st.container(border=True):
            #Datos Importaciones Carne
            piensoV = data["Importaciones"]["Pienso para animales (excepto cereales sin moler) Valor (MP)"]
            tortasC = data["Importaciones"]["Tortas de soja Cantidad (t)"]
            tortasV = data["Importaciones"]["Tortas de soja Valor (MP)"]
            harina_piensoC = data["Importaciones"]["Harina animal para pienso Cantidad (t)"]
            harina_piensoV = data["Importaciones"]["Harina animal para pienso Valor (MP)"]
            preparadosC = data["Importaciones"]["Preparados del tipo utilizado para la alimentacion de animales Cantidad (t)"]
            preparadosV = data["Importaciones"]["Preparados del tipo utilizado para la alimentacion de animales Valor (MP)"]
            diversosV = data["Importaciones"]["Productos y preparados comestibles diversos Valor (MP)"]
            otrosC = data["Importaciones"]["Otros preparados alimenticios Cantidad (t)"]
            otrosV = data["Importaciones"]["Otros preparados alimenticios Valor (MP)"]

            #DataFrames
            dfV = pd.DataFrame({
                "Pienso para animales (excepto cereales sin moler)": piensoV,
                "Tortas de soja": tortasV,
                "Harina animal para pienso": harina_piensoV,
                "Preparados del tipo utilizado para la alimentación de animales": preparadosV,
                "Productos y preparados comestibles diversos": diversosV,
                "Otros preparados alimenticios": otrosV
            })
            dfV.index.name = "Año"

            dfC = pd.DataFrame({
                "Tortas de soja": tortasC,
                "Harina animal para pienso": harina_piensoC,
                "Preparados del tipo utilizado para la alimentación de animales": preparadosC,
                "Otros preparados alimenticios": otrosC
            })
            dfC.index.name = "Año"

            dfV = dfV.apply(pd.to_numeric)
            dfC = dfC.apply(pd.to_numeric)
            #Grafico de Linea con selectbox
            st.markdown("#### 🧑🏻‍🌾 Valores de importaciones con destino a la alimentación del ganado")
            opcion = st.selectbox("Seleccione una opción", ["Valor", "Cantidad"])
            
            val = px.line(dfV,markers=True,color_discrete_sequence=custom_colors, hover_name='value', hover_data={'value':None})
            val.update_layout(width=1200, height=600, 
                            yaxis_title = "Cantidad", xaxis_title = "Años",
                            legend=dict(title=dict(text="Tipo")))
                
            cant = px.line(dfC,markers=True,color_discrete_sequence=custom_colors, hover_name='value', hover_data={'value':None})
            cant.update_layout(width=1200, height=600, 
                            yaxis_title = "Cantidad", xaxis_title = "Años",
                            legend=dict(title=dict(text="Tipo")))
            if opcion == "Valor":
                st.markdown("###### Miles de Pesos (MP)")
                st.plotly_chart(val)
            if opcion == "Cantidad":
                st.markdown("###### Toneladas (T)")
                st.plotly_chart(cant)
            
            with st.expander("Obervaciones"):
                st.markdown("- Se incluyen estos valores, dado que las importaciones en este contexto son la mayor fuente de obtención de productos destinados a la alimentación del ganado para la distribución en nuestro pais.")
                st.markdown("- En la leyenda se pueden elegir los valores que se muestren o no en la gráfica pulsando en la línea de color al lado del nombre del tipo de importación (si se pulsa dos veces se descartan el resto de valores y solo se muestra el pulsado de forma individual).")
                st.markdown("- En el cuerpo de la gráfica se muestra en los marcadores de cada pico para que se muestren los valores exactos en un cartel (tooltip).")
                st.markdown("- De los datos sobre los pocos productos seleccionados para exportaciones sólo se tenía el valor por lo que se decidió no incluirlo en el dataproduct.")
                csv5_1 = convert_df(dfC)
                csv5_2 = convert_df(dfV)
            
                with st.popover("Descargar CSV"):
                    st.download_button( 
                                        label="Cantidad",
                                        data=csv5_1,
                                        file_name="cant.csv",
                                        mime="text/csv")
                    st.download_button( 
                                        label="Valor",
                                        data=csv5_2,
                                        file_name="values.csv",
                                        mime="text/csv")       