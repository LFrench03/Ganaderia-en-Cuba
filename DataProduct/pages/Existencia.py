import streamlit as st
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go

with open('inventario_ganado.json',encoding = "utf8") as json_data: #Cargar Json 
    data = json.load(json_data)  
            
#Datos totales
vacuno = data["vacuno"]["Total"]  
porcino = data["porcino"]["Existencia(Mcabz)"]["Total"]
ovino_caprino = data["ovino_caprino"]["Existencia(Mcabz)"]["Total"]["Total"]
aves = data["aves"]["Existencia(Mcabz)"]["Existencia total de aves"]
equido = data["equido"]["Existencia(Mcabz)"]["Total"] 

#Datos Porcino Estatal
porcinoE = data["porcino"]["Existencia(Mcabz)"]["Estatal"]
porcinoNE = {}
            
#Datos Porcino No Estatal
for year in porcino:
    porcinoNE[year] = round(float(porcino[year]) - float(porcinoE[year]), 1) 
            
#Datos Ovino Caprino Estatal
ovino_caprinoE = data["ovino_caprino"]["Existencia(Mcabz)"]["Estatal"]["Total"]
ovino_caprinoNE = {}
            
#Datos Ovino Caprino No Estatal
for year in ovino_caprino:
    if ovino_caprino[year] != ovino_caprinoE[year]:
        ovino_caprinoNE[year] = round(float(ovino_caprino[year]) - float(ovino_caprinoE[year]), 1) 
            
#Datos Aves Estatal
avesE = data["aves"]["Existencia(Mcabz)"]["Empresas avicolas estatales"]["Existencia total de aves"]
avesNE = {}
                
#Datos Aves No Estatal
for year in aves:
    if aves[year] != avesE[year]:
        avesNE[year] = round(float(aves[year]) - float(avesE[year]),1)     
            
#Datos Equido Estatal y No Estatal
equidoE = data["equido"]["Existencia(Mcabz)"]["Estatal"]["Total"]
equidoNE = data["equido"]["Existencia(Mcabz)"]["No estatal"]["Total"]

#Dataframes Existencia
ganado_TOTAL = pd.DataFrame({
                "Vacuno": vacuno,
                "Porcino": porcino,
                "Ovino Caprino": ovino_caprino,
                "Aves": aves,
                "Equido": equido
                
            })   
ganado_TOTAL.index.name = "Año" #Cambiar nombre de los indices de cada dataframe para que se muestre en el tooltip
ganado_ESTATAL = pd.DataFrame({
                "Porcino": porcinoE,
                "Ovino Caprino": ovino_caprinoE,
                "Aves": avesE,
                "Equido": equidoE
            })
ganado_ESTATAL.index.name = "Año"
ganado_NO_ESTATAL = pd.DataFrame({
                "Porcino": porcinoNE,
                "Ovino Caprino": ovino_caprinoNE,
                "Aves": avesNE,
            })
ganado_NO_ESTATAL.index.name = "Año"
ganado_TOTAL = ganado_TOTAL.apply(pd.to_numeric)
ganado_ESTATAL = ganado_ESTATAL.apply(pd.to_numeric)
ganado_NO_ESTATAL = ganado_NO_ESTATAL.apply(pd.to_numeric)
            
custom_colors = ["#6382f3","#f3639c","#8a8a8a","#e8e85b","#ad5514"] #Secuencia de colores

#Tabulaciones
tab1, tab2, tab3 = st.tabs(["Existencia del ganado", "Entregas a sacrificio", "Natalidad y Mortalidad"])

with tab1: #Tab de Existencia
    # Sistema de Metricas de diferencia entre dos años
    with st.container(border=True):
        st.markdown("#### 📉📈 Desarrollo de diferencias de la existencia total del ganado cubano desde 1990 hasta 2022")
        ganado_TOTAL = ganado_TOTAL.iloc[5:,:]
        ganado = st.selectbox("Seleccione un tipo de ganado", list(ganado_TOTAL.columns))
        col1, col2, col3 = st.columns(3)
        with col1.popover("Seleccione el Año X"):
            year1 = st.select_slider("Año X",list(ganado_TOTAL.index))
        with col3.popover("Seleccione el Año Y"):
            year2 = st.select_slider("Año Y",list(ganado_TOTAL.index))
        with col2:
            result = round(float(ganado_TOTAL.loc[str(year2), ganado])-ganado_TOTAL.loc[str(year1), ganado],2)
            botton = st.toggle("Intercambiar métrica")
            if botton:
                st.metric(label=ganado, value=f"{ganado_TOTAL.loc[str(year2), ganado]} MCabz", delta=f"{result} MCabz")
            else:
                st.metric(label=ganado, value=f"{ganado_TOTAL.loc[str(year1), ganado]} MCabz", delta=f"{result} MCabz")
            st.markdown("##### Años ")
            col2_1, col2_2 = st.columns(2)
            col2_1.markdown(f"X = {year1}")
            col2_2.markdown(f"Y = {year2}")
        with st.expander("Explicación"):
            st.markdown('''- El valor que se muestra en la métrica por defecto es el valor de existencia en el Año X como minuendo de la resta (al activar el toggle mostraria el Año Y en su lugar),
                        y el subíndice (delta) muestra la diferencia (positiva o negativa) del resultado de la diferencia entre el valor de existencia
                        en el Año X menos el del Año Y *(todos los valores obviamente correspondientes al tipo de ganado seleccionado)*''')
            st.markdown('''- Los valores de existencia están dados en Miles de Cabezas (MCabz)''')

    st.markdown("### 〽️ ¿Qué tipos de ganado han predominado en Cuba en el período de 1985-2022?")
    
    with st.container(border=True):       
            opciones = st.selectbox( "Seleccione una grupo", ["Total", "Estatal", "No Estatal"]) #Selectbox de Existencia

            #Graficos de Linea de la Existencia
            st.markdown("###### Miles de Cabezas (MCabz)")
            total = px.line(ganado_TOTAL,markers=True,color_discrete_sequence=custom_colors, hover_name='value', hover_data={'value':None})
            total.update_layout(width=800, height=600, 
                            yaxis_title = "Cantidad", xaxis_title = "Años",
                            legend=dict(title=dict(text="Tipo de ganado")))
            
            estatal = px.line(ganado_ESTATAL,markers=True,color_discrete_sequence=custom_colors[1:], hover_name='value', hover_data={'value':None})
            estatal.update_layout(width=800, height=600, 
                            yaxis_title = "Cantidad", xaxis_title = "Años", 
                            legend=dict(title=dict(text="Tipo de ganado")))    
            
            NOestatal = px.line(ganado_NO_ESTATAL,markers=True,color_discrete_sequence=custom_colors[1:-1], hover_name='value', hover_data={'value':None})
            NOestatal.update_layout(width=800, height=600, 
                            yaxis_title = "Cantidad", xaxis_title = "Años", 
                            legend=dict(title=dict(text="Tipo de ganado")))       
            
            #Funcion auxiliar y condicionales para el Selectbox de Existencia
            def mostrar(graf):
                st.plotly_chart(graf)
            if opciones == "Total":
                mostrar(total)
            if opciones == "Estatal":
                mostrar(estatal)
            if opciones == "No Estatal":
                mostrar(NOestatal)
            with st.expander("Observaiones"):
                st.write("- La cantidad de todos los tipos de ganado está expresada en miles de cabezas")
                st.write("- Los valores de los años que son 0, se deben a que no se encuentran los datos en la ONEI")
    with st.container(border=True):

        col1, col2 = st.columns(2)

        with col1:
            #Datos diferentes Tipos de Aves
            ponedoras = data["aves"]["Existencia(Mcabz)"]["Empresas avicolas estatales"]["Gallinas ponedoras"]
            pollos_ceba = data["aves"]["Existencia(Mcabz)"]["Empresas avicolas estatales"]["Pollos de ceba(Miles de cabezas"]
            reproductoras = data["aves"]["Existencia(Mcabz)"]["Empresas avicolas estatales"]["Reproductoras "]
            carne = data["aves"]["Existencia(Mcabz)"]["Empresas avicolas estatales"]["De carne"]
            ponedoras = data["aves"]["Existencia(Mcabz)"]["Empresas avicolas estatales"]["De ponedoras"]
            otras = data["aves"]["Existencia(Mcabz)"]["Empresas avicolas estatales"]["Otras"]     
            
            #DataFrame diferentes Tipos de Aves
            aves_estatales_tipos = pd.DataFrame({
                "Pollos de ceba": pollos_ceba,
                "Reproductoras": reproductoras,
                "De carne": carne,
                "De ponedoras": ponedoras,
                "Otras": otras       
            })
            aves_estatales_tipos = aves_estatales_tipos.apply(pd.to_numeric)
            
            #Grafico de Barras de Frecuencia de Existencia de los diferentes Tipos de Aves
            opciones3 = st.select_slider("Seleccione un año",[x for x in range (1995,2023)])
            st.markdown("#### 🐓 Frecuencia de la existencia de los diferentes Tipos de Aves")
            def crear_grafica(year):
                df = aves_estatales_tipos.loc[str(year)]
                df.index.name = "Tipo"
                fig = px.bar(df,hover_name='value', hover_data={'variable': None, 'value':None})
                fig.update_layout( yaxis_title = "Cantidad", xaxis_title = "Tipo de ganado")
                fig.update_traces(width=0.5,
                                marker_line_color="black",
                                marker_line_width=1.5, opacity=0.6,
                                showlegend=False)
                fig.data[0].marker.color = ["#eef124", "#d95330", "#8a8a8a", "#ff9e29", "#3a3d85"]
                    
                return fig  
            st.markdown("###### Miles de Cabezas (MCabz)")
            st.plotly_chart(crear_grafica(opciones3))
        #Expansor con observaciones
        with col2:        
            with st.expander("Observaciones"):
                st.write("- La cantidad de todos los tipos de ganado está expresada en miles de cabezas")
                st.write("- Los valores de los años que son 0, se deben a que no se encuentran los datos en la ONEI")
                
        col1, col2 = st.columns(2)

        with col1:
            #Datos Existencia Ovino y Caprino por separado
            exist_ovino = data["ovino_caprino"]["Existencia(Mcabz)"]["Total"]["Ovino"]
            exist_caprino = data["ovino_caprino"]["Existencia(Mcabz)"]["Total"]["Caprino"]
            
            #DataFrame Existencia Ovino y Caprino por separado
            exist_OC = pd.DataFrame({    
                "Ovino": exist_ovino,
                "Caprino": exist_caprino,    
            })
                
            exist_OC = exist_OC.apply(pd.to_numeric)

            #Grafico de pastel con slider para los años
            st.markdown("#### 🐏🐐 Comparación de la existencia del ganado Ovino-Caprino")
            opciones1 = st.select_slider("Seleccione un año",[x for x in range (1990,2023)])
            st.markdown("###### Cabezas (Cabz)") 
            colors = ['#51829B', '#9BB0C1'] #Colores
            def crear_grafica(year):
                fig = go.Figure(data = go.Pie(labels=["Ovino", "Caprino"], values = exist_OC.loc[str(year)], pull= 0.1, textposition="outside", hoverinfo='value',textinfo='label+percent', 
                    marker=dict(colors=colors, line=dict(color='black', width=3))))
                fig.update_layout(
                width=1300,  
                height=500,  
                margin=dict(l=100, r=100, t=100, b=100)
            )
                
                return fig  

            st.plotly_chart(crear_grafica(opciones1))

        #Expansor con observaciones
        with col2:        
            with st.expander("Observaciones"):
                st.write("- La cantidad de todos los tipos de ganado está expresada en miles de cabezas")
                st.write("- Los valores de los años que son 0, se deben a que no se encuentran los datos en la ONEI")
        
        #Datos tipos de Ganado Vacuno
        ternerasH = data["vacuno"]["Hembras"]["Terneras"]
        annojasH = data["vacuno"]["Hembras"]["Añojas"]
        novillasH = data["vacuno"]["Hembras"]["Novillas"]
        vacasH = data["vacuno"]["Hembras"]["Vacas"]
        ternerosM = data["vacuno"]["Machos"]["Terneros"]
        annojaosM = data["vacuno"]["Machos"]["Añojos"]
        toretesM = data["vacuno"]["Machos"]["Toretes"]
        toros_cebaM = data["vacuno"]["Machos"]["Toros de ceba"]
        bueyesM = data["vacuno"]["Machos"]["Bueyes"]
        sementalesM = data["vacuno"]["Machos"]["Sementales"]
        receladoresM = data["vacuno"]["Machos"]["Receladores"]

        #DataFrame Tipos de Ganado Vacuno
        vacasDF = pd.DataFrame({
            "Terneras": ternerasH,
            "Añojas": annojasH,
            "Novillas": novillasH,
            "Vacas": vacasH,        
            "Terneros": ternerosM,
            "Añojos": annojaosM,
            "Toretes": toretesM,
            "Toros de ceba": toros_cebaM,
            "Bueyes": bueyesM,
            "Sementales": sementalesM,
            "Receladores": receladoresM     
        })      
        vacasDF = vacasDF.apply(pd.to_numeric)

        #Grafico de Barra con Slider para los Tipos de Ganado Vacuno
        st.markdown("### 🐄🐂 Distribución de los diferentes tipos de Ganado Vacuno")
        
        opciones = st.select_slider("Seleccione un año",[x for x in range (1985,2023)])
        def crear_grafica(year):
            df = vacasDF.loc[str(year)]
            df.index.name = "Tipo"
            fig = px.bar(df, hover_name='value', hover_data={'variable': None, 'value':None})
            fig.update_layout(
            yaxis_title = "Cantidad", xaxis_title = "Ganado vacuno")       
            fig.update_traces(width=0.7,
                    marker_line_color="black",
                    marker_line_width=1.5, opacity=0.6,
                    showlegend = False) 
            fig.data[0].marker.color = ["#FA7070", "#FA7070","#FA7070", "#FA7070","#4793AF", "#4793AF","#4793AF", "#4793AF","#4793AF", "#4793AF","#4793AF"] #Colores Rojo para Hembras y Azul para Macho
            return fig  
        st.markdown("###### Miles de Cabezas (MCabz)")
        st.plotly_chart(crear_grafica(opciones))   

        #Expansor con observaciones
        with st.expander("Observaciones"):
            st.write("- La cantidad de todos los tipos de ganado está expresada en miles de cabezas")
            st.write("- Los valores de los años que son 0, se deben a que no se encuentran los datos en la ONEI")
        col1, col2 = st.columns(2)
        with col1:
            #Datos equido
            equinoT = data["equido"]["Existencia(Mcabz)"]["Equino"]["Total"]
            equinoM = data["equido"]["Existencia(Mcabz)"]["Equino"]["machos"]
            equinoH = {}
            for i in equinoT:
                equinoH[i] = round(float(equinoT[i]) - float(equinoM[i]), 1)
            asnalT = data["equido"]["Existencia(Mcabz)"]["Asnal"]["Total"]
            asnalM = data["equido"]["Existencia(Mcabz)"]["Asnal"]["machos"]
            asnalH = {}
            for i in asnalT:
                asnalH[i] = round(float(asnalT[i]) - float(asnalM[i]), 1)
            mular = data["equido"]["Existencia(Mcabz)"]["Mular"]
            
            equinoTE = data["equido"]["Existencia(Mcabz)"]["Estatal"]["Equino"]["Total"]
            equinoME = data["equido"]["Existencia(Mcabz)"]["Estatal"]["Equino"]["machos"]
            equinoHE = {}
            for i in equinoT:
                equinoHE[i] = round(float(equinoTE[i]) - float(equinoME[i]), 1)
            asnalTE = data["equido"]["Existencia(Mcabz)"]["Estatal"]["Asnal"]["Total"]
            asnalME = data["equido"]["Existencia(Mcabz)"]["Estatal"]["Asnal"]["machos"]
            asnalHE = {}
            for i in asnalTE:
                asnalHE[i] = round(float(asnalTE[i]) - float(asnalME[i]), 1)
            mularE = data["equido"]["Existencia(Mcabz)"]["Estatal"]["Mular"]
            equinoTNE = data["equido"]["Existencia(Mcabz)"]["No estatal"]["Equino"]["Total"]
            equinoMNE = data["equido"]["Existencia(Mcabz)"]["No estatal"]["Equino"]["machos"]
            equinoHNE = {}
            for i in equinoT:
                equinoHNE[i] = round(float(equinoTNE[i]) - float(equinoMNE[i]), 1)
            asnalTNE = data["equido"]["Existencia(Mcabz)"]["No estatal"]["Asnal"]["Total"]
            asnalMNE = data["equido"]["Existencia(Mcabz)"]["No estatal"]["Asnal"]["machos"]
            asnalHNE = {}
            for i in asnalTE:
                asnalHNE[i] = round(float(asnalTNE[i]) - float(asnalMNE[i]), 1)
            mularNE = data["equido"]["Existencia(Mcabz)"]["No estatal"]["Mular"]            

            #Dataframes equido  
            dfT = pd.DataFrame({
                    "Equino": equinoT,
                    "Asnal": asnalT,
                    "Mular": mular
            })
            dfE = pd.DataFrame({
                    "Equino": equinoTE,
                    "Asnal": asnalTE,
                    "Mular": mularE
            })
            dfNE = pd.DataFrame({
                    "Equino": equinoTNE,
                    "Asnal": asnalTNE,
                    "Mular": mularNE
            })
            dfequino = pd.DataFrame({
                    "Macho":equinoM,
                    "Hembra":equinoH
            })

            dfasnal = pd.DataFrame({
                    "Macho":asnalM,
                    "Hembra":asnalH
            })

            #Grafico de pastel equido
            st.markdown("### 🐴 Existencia de Ganado Equido por Tipos")
            opcion = st.selectbox("Seleccione un grupo", ["Total", "Equino", "Asnal", "Estatal", "No Estatal"])
            def crear_graficaT(year, df):
                colors = ['#e59c57', '#ddb38c', "#856b53"]
                fig = go.Figure(data = go.Pie(labels=["Equino", "Asnal", "Mular"], values = df.loc[str(year)],pull= 0.1, textposition="outside", hoverinfo='value',textinfo='label+percent', 
                                marker=dict(colors=colors, line=dict(color='black', width=3))))
                fig.update_layout(width=1300,  height=500,  margin=dict(l=100, r=100, t=100, b=100))
                return fig 
            if opcion == "Total":
                st.markdown("###### Total (Miles de Cabezas)")
                opciones1 = st.select_slider("Año",[x for x in range (1985,2023)])
                st.plotly_chart(crear_graficaT(opciones1, dfT))   
            if opcion == "Estatal":
                st.markdown("###### Estatal (Miles de Cabezas)")
                opciones1 = st.select_slider("Año",[x for x in range (1985,2023)])
                st.plotly_chart(crear_graficaT(opciones1, dfE)) 
            if opcion == "No Estatal":
                st.markdown("###### No Estatal (Miles de Cabezas)")
                opciones1 = st.select_slider("Año",[x for x in range (1985,2023)])
                st.plotly_chart(crear_graficaT(opciones1, dfNE))    
                
            def crear_graficaE(year, df):
                colors = ["#4793AF","#FA7070"]
                fig = go.Figure(data = go.Pie(labels=["Macho", "Hembra"], values = df.loc[str(year)],pull= 0.1, textposition="outside", hoverinfo='value',textinfo='label+percent', 
                                marker=dict(colors=colors, line=dict(color='black', width=3))))
                fig.update_layout(width=1300,  height=500,  margin=dict(l=100, r=100, t=100, b=100))
                return fig 
            if opcion == "Equino":
                st.markdown("###### Equino (Miles de cabezas)")
                opciones1 = st.select_slider("Año",[x for x in range (1985,2023)])
                st.plotly_chart(crear_graficaE(opciones1, dfequino))  
            if opcion == "Asnal":
                st.markdown("###### Asnal (Miles de cabezas)")
                opciones1 = st.select_slider("Año",[x for x in range (1985,2023)])
                st.plotly_chart(crear_graficaE(opciones1, dfasnal))
        with col2:
            with st.expander("Observaciones"):
                st.markdown("# A")
with tab2:
        st.markdown("### 🪓 ¿Qué tipo de ganado tiene mayor frecuencia de entregas a sacrificios?")
    
        with st.container(border=True): 
                opc = st.selectbox("Seleccione un grupo", ["Total", "Estatal"]) #Selectbox con opciones 

                #Datos Sacrificios Total
                sacrif_vacunoT = data["vacuno"]["Sacrificios"]["Cabezas(M)"]["Total"]
                sacrif_porcinoT = data["porcino"]["Entregas a sacrificio"]["Total"]["Cabezas(Mcabz)"]
                sacrif_ovT = data["ovino_caprino"]["Entregas a sacrificio"]["Cantidad(Mcabz)"]["Total"]
                sacrif_aves = data["aves"]["Entregas a sacrificio"]["Pollos de ceba entrega a sacrificio"]["Cantidad(Mcabz)"]

                #Datos Sacrificios Ganado Vacuno Estatales
                sacrif_vacunoE = data["vacuno"]["Sacrificios"]["Cabezas(M)"]["Estatal"]
                #Datos Sacrificios Ganado Vacuno No estatales
                sacrif_vacunoNE = {}        
                for year in sacrif_vacunoT:
                    if sacrif_vacunoT[year] != sacrif_vacunoE[year]:
                        sacrif_vacunoNE[year] = round(float(sacrif_vacunoT[year]) - float(sacrif_vacunoE[year]), 1) 

                #Datos Sacrificios Ganado Porcino Estatales
                sacrif_porcinoE = data["porcino"]["Entregas a sacrificio"]["Estatal"]["Cabezas(Mcabz)"]["Total"]
                sacrif_porcinoNE = {}
                #Datos Sacrificios Ganado Porcino No Estatales
                for year in sacrif_porcinoT:
                    if sacrif_porcinoT[year] != sacrif_porcinoE[year]:
                        sacrif_porcinoNE[year] = round(float(sacrif_porcinoT[year]) - float(sacrif_porcinoE[year]),1)

                #Datos Sacrificios Ganado Ovino-Caprino Estatales
                sacrif_ovE = data["ovino_caprino"]["Entregas a sacrificio"]["Cantidad(Mcabz)"]["Estatal"]
                sacrif_ovNE = {}
                for year in sacrif_ovT:
                    if sacrif_ovT[year] != sacrif_ovE[year]:
                        sacrif_ovNE[year] = round(float(sacrif_ovT[year]) - float(sacrif_ovE[year]), 1) 
                
                #DataFrames Sacrificios
                sacrif_TOTAL = pd.DataFrame({
                    "Vacuno": sacrif_vacunoT,
                    "Porcino": sacrif_porcinoT,
                    "Ovino Caprino": sacrif_ovT,
                    "Pollos de Ceba": sacrif_aves
                })   
                
                sacrif_ESTATAL = pd.DataFrame({
                    "Vacuno": sacrif_vacunoE,
                    "Porcino": sacrif_porcinoE,
                    "Ovino Caprino": sacrif_ovE,
                    "Pollos de Ceba": sacrif_aves
                })

                sacrif_TOTAL = sacrif_TOTAL.apply(pd.to_numeric)
                sacrif_TOTAL.index.name = "Año"
                sacrif_ESTATAL = sacrif_ESTATAL.apply(pd.to_numeric)
                sacrif_ESTATAL.index.name = "Año"

                
                #Grafico de Linea
                sacrifT = px.line(sacrif_TOTAL,markers=True,color_discrete_sequence=custom_colors[:-1],hover_name='value', hover_data={'value':None})
                sacrifT.update_layout(width=800, height=600, 
                                yaxis_title = "Cantidad", xaxis_title = "Años", legend=dict(title=dict(text="Tipo de ganado")))
                
                sacrifE = px.line(sacrif_ESTATAL,markers=True,color_discrete_sequence=custom_colors[:-1],hover_name='value', hover_data={'value':None})
                sacrifE.update_layout(width=800, height=600, 
                                yaxis_title = "Cantidad", xaxis_title = "Años", legend=dict(title=dict(text="Tipo de ganado")))
                

                
             
                if opc == "Total":
                    st.markdown("###### Miles de Cabezas (MCabz)")
                    st.plotly_chart(sacrifT)
                if opc == "Estatal":
                    st.markdown("###### Miles de Cabezas (MCabz)")
                    st.plotly_chart(sacrifE)

            
                with st.expander("Observaciones"):
                    st.markdown("A")

        with st.container(border=True):
            st.subheader("⚖️ Peso en pie y peso promedio del ganado de tipo productor")

        
            pesoenpie_vacuno = data["vacuno"]["Sacrificios"]["Peso en pie(Mt)"]["Total"]
            pesoenpie_porcino = data["porcino"]["Entregas a sacrificio"]["Total"]["Peso en pie(Mt)"]
            pesoenpie_aves = data["aves"]["Entregas a sacrificio"]["Pollos de ceba entrega a sacrificio"]["Peso en pie(Mt)"]
            pesoenpie_ovino_carpino = data["ovino_caprino"]["Entregas a sacrificio"]["Peso en pie(Mt)"]["Total"]
            pesoprom_vacuno = data["vacuno"]["Sacrificios"]["Peso Promedio(Kg)"]["Total"]
            pesoprom_porcino = data["porcino"]["Entregas a sacrificio"]["Total"]["Peso promedio(kg)"]
            pesoprom_aves = data["aves"]["Entregas a sacrificio"]["Pollos de ceba entrega a sacrificio"]["Peso promedio(kg)"]
            pesoenprom_ovino_carpino = data["ovino_caprino"]["Entregas a sacrificio"]["Peso promedio(kg)"]["Total"]



            pie = pd.DataFrame({
            "Vacuno": pesoenpie_vacuno,
            "Porcino": pesoenpie_porcino,
            "Aves": pesoenpie_aves,
            "Ovino Caprino": pesoenpie_ovino_carpino
        })
            promedio = pd.DataFrame({
            "Vacuno": pesoprom_vacuno,
            "Porcino": pesoprom_porcino,
            "Ovino Caprino":pesoenprom_ovino_carpino
        })
            pie = pie.apply(pd.to_numeric)
            promedio = promedio.apply(pd.to_numeric)

            choice = st.selectbox("Seleccione una opcion", ["Peso en Pie", "Peso Promedio"])
            opciones2 = st.select_slider("Año",[x for x in range (1991,2023)])
            def crear_grafica(year, choice):
                if choice == "Peso en Pie":
                    df = pie.loc[str(year)]                
                    df.index.name = "Tipo"             
                    fig = px.bar(df, hover_name='value', hover_data={'variable': None, 'value':None}, orientation="h")
                    fig.update_layout(
                    yaxis_title = "Tipo de Ganado", xaxis_title = "Peso en Pie(Mt)")
                    fig.data[0].marker.color = ["#6382f3","#f3639c","#e8e85b","#8a8a8a"] #Secuencia de colores
                else:
                    df = promedio.loc[str(year)] 
                    df.index.name = "Tipo"                            
                    fig = px.bar(df, hover_name='value', hover_data={'variable': None, 'value':None}, orientation="h")
                    fig.update_layout(
                    yaxis_title = "Tipo de Ganado", xaxis_title = "Peso Promedio(Kg)")
                    fig.data[0].marker.color = ["#6382f3","#f3639c","#8a8a8a"] #Secuencia de colores
                
                fig.update_traces(width=0.7,
                        marker_line_color="black",
                        marker_line_width=1.5, opacity=0.6,
                        showlegend = False) 
                return fig  

            st.plotly_chart(crear_grafica(opciones2, choice))     

            with st.expander("Observaciones"):
                st.write("A")
        
        with st.container(border=True):
            #Datos Porcino Estatal Entregas de Sacrificio Estatal
            porcino_estatalT= data['porcino']['Entregas a sacrificio']['Estatal']['Cabezas(Mcabz)']['Total']
            porcino_estatalCeba = data['porcino']['Entregas a sacrificio']['Estatal']['Cabezas(Mcabz)']['Ceba']
            porcino_estatalResto = {}
            for year in porcino_estatalT:
                if porcino_estatalT[year] and porcino_estatalCeba[year]:
                    porcino_estatalResto[year] = round(float(porcino_estatalT[year]) - float(porcino_estatalCeba[year]),1)
            
            #DatFrame Porcino Sacrificios Estatal
            df = pd.DataFrame({
                "De Ceba": porcino_estatalCeba,
                "Resto": porcino_estatalResto
            })
            st.markdown("#### 🐷 Comparación de entregas a sacrificio del Ganado Porcino de Ceba con los valores restantes")
            year = st.select_slider("Año", [x for x in range(1989, 2013)])
            st.markdown("###### Miles de Cabezas (MCabz)")
            def graficar(year):
                fig = go.Figure(data = go.Pie(labels = ["De Ceba", "Resto"], values = df.loc[str(year)], pull = 0.1, textposition="outside", hoverinfo="value", textinfo="label+percent",
                                            marker=dict(colors=["#fc5b98", "#761e3f"], line=dict(color="black", width=3))))
                fig.update_layout(width=1300, height=500, margin=dict(l=100, r=100, t=100, b=100))
                return fig
            st.plotly_chart(graficar(year))

            with st.expander("Observaciones"):
                st.markdown("A")

        with st.container(border=True):
            #Datos Importaciones Carne
            carneV = data["Importaciones"]["Carne y preparados de carne Valor(MP)"]
            carnebovinaV = data["Importaciones"]["Carne de ganado bovino congelada deshuesada Valor(MP)"]
            carnebovinaC = data["Importaciones"]["Carne de ganado bovino congelada deshuesada Cantidad(t)"]
            carneporcinaV = data["Importaciones"]["Carne de ganado porcino congelada Valor (MP)"]
            carneporcinaC = data["Importaciones"]["Carne de ganado porcino congelada Cantidad (t)"]
            carneavesV = data["Importaciones"]["Carne y despojos comestibles de las aves Valor (MP)"]
            carneavesC = data["Importaciones"]["Carne y despojos comestibles de las aves Cantidad (t)"]
            carnerestoV = data["Importaciones"]["Carne y despojos de carne preparados o en conserva Valor (MP)"]
            carnerestoC = data["Importaciones"]["Carne y despojos de carne preparados o en conserva Cantidad (t)"]

            #DataFrames
            dfV = pd.DataFrame({
                "Carne de ganado bovino congelada deshuesada": carnebovinaV,
                "Carne de ganado porcino congelada deshuesada": carneporcinaV,
                "Carne y despojos comestibles de las aves": carneavesV,
                "Carne y despojos y despojos de carne preparados o en conserva": carnerestoV
            })
            dfV.index.name = "Año"
            dfC = pd.DataFrame({
                "Carne de ganado bovino congelada deshuesada": carnebovinaC,
                "Carne de ganado porcino congelada deshuesada": carneporcinaC,
                "Carne y despojos comestibles de las aves": carneavesC,
                "Carne y despojos y despojos de carne preparados o en conserva": carnerestoC
            })
            dfC.index.name = "Año"

            #Grafico de Linea con selectbox
            st.markdown("#### 🥩 Valores de Importaciones de Carne Seleccionados por Tipos")
            opcion = st.selectbox("Seleccione un grupo", ["Valor", "Cantidad"])
            def graficar(opc):
                fig = px.line(opc,markers=True,color_discrete_sequence=custom_colors, hover_name='value', hover_data={'variable': None, 'value':None})
                fig.update_layout(width=1200, height=600, 
                                yaxis_title = "Cantidad", xaxis_title = "Años",
                                legend=dict(title=dict(text="Tipo de Carne")))
                return fig
            if opcion == "Valor":
                st.markdown("###### Miles de Pesos (MP)")
                st.plotly_chart(graficar(dfV))
            if opcion == "Cantidad":
                st.markdown("###### Toneladas (T)")
                st.plotly_chart(graficar(dfC))
            
            with st.expander("Obervaciones"):
                st.write("Natalidad y Mortalidad")


with tab3:
    #Datos de los nacimientos y muertes
    nacimientos_vacunos = data["vacuno"]["Nacimientos_muertes(Mcabz)"]["Nacimientos"]["Totales"]
    muertes_vacuno = data["vacuno"]["Nacimientos_muertes(Mcabz)"]["Muertes"]["Totales"]
    nacimientos_porcinos = data["porcino"]["Nacimientos (vivos)(Mcabz)"]["Total"]
    muertes_porcinos = data["porcino"]["Muertes de crías (a)(Mcabz)"]["Total"]
    
    with st.container(border=True):
        nac_vDF = pd.DataFrame({
            "Nacimientos vacunos": nacimientos_vacunos
        })
        muer_vDF = pd.DataFrame({
            "Muertes vacunas": muertes_vacuno
        })
        nac_pDF = pd.DataFrame({
            "Nacimientos porcinos": nacimientos_porcinos
        })
        muer_pDF = pd.DataFrame({
            "Muertes porcinas": muertes_porcinos
        })
        nac_vDF = nac_vDF.apply(pd.to_numeric)
        muer_vDF = muer_vDF.apply(pd.to_numeric)
        nac_pDF = nac_pDF.apply(pd.to_numeric)
        muer_pDF = muer_pDF.apply(pd.to_numeric)

        nac_vDF.columns = ["Muertes vacunas"]
        nac_pDF.columns = ["Muertes porcinas"]

        calcular_tasa_vacuno = round(((nac_vDF/muer_vDF)-1),2)
        calcular_tasa_porcino = round(((nac_pDF/muer_pDF)-1),2)
        tasa_existDF = pd.DataFrame({
            "Ganado vacuno": calcular_tasa_vacuno.squeeze(),
            "Ganado porcino": calcular_tasa_porcino.squeeze()
        })
        tasa_existDF = tasa_existDF.apply(pd.to_numeric)
        st.markdown("### 💀 Tasa de Mortalidad")
        opciones11 = st.select_slider("Año",[x for x in range (1993,2023)])
        def crear_grafica(year):
            df = tasa_existDF.loc[str(year)]
            df.index.name = "Tipo"
            fig = px.bar(df, hover_name='value', hover_data={'variable': None, 'value':None}, orientation='h')
            fig.update_layout(
            xaxis_title = "Tasa")       
            fig.update_traces(width=0.5,
                    marker_line_color="black",
                    marker_line_width=1.5, opacity=0.6, 
                    showlegend = False) 
            fig.data[0].marker.color = ["#5B99C2","#e0327c"] 
            return fig  

        st.plotly_chart(crear_grafica(opciones11)) 
        with st.expander("Observaciones") :
            st.markdown("")

    with st.container(border=True):
        st.markdown("### 🧬 Nacimientos y Muertes")
        answer = st.selectbox("Tipo de Ganado", ["Vacuno🐮", "Porcino🐷"])
        nac_muert_vacunosDF = pd.DataFrame({
            "Nacimientos": nacimientos_vacunos,
            "Muertes": muertes_vacuno
        })
        nac_muert_vacunosDF.index.name = "Año"
        nac_muert_porcinosDF = pd.DataFrame({
            "Nacimientos": nacimientos_porcinos,
            "Muertes": muertes_porcinos
        })
        nac_muert_porcinosDF.index.name = "Año"
        nac_muert_vacunosDF = nac_muert_vacunosDF.apply(pd.to_numeric)
        nac_muert_porcinosDF = nac_muert_porcinosDF.apply(pd.to_numeric)

        #Grafico de Linea con selectbox
        v = px.line(nac_muert_vacunosDF, hover_name='value', hover_data={'variable': None, 'value':None}, markers=True,color_discrete_sequence=custom_colors)
        v.update_layout(width=800, height=600, 
                    yaxis_title = "Cantidad", xaxis_title = "Años", 
                    legend=dict(
                                title=dict(text="")))
        p = px.line(nac_muert_porcinosDF, hover_name='value', hover_data={'variable': None, 'value':None}, markers=True,color_discrete_sequence=custom_colors)
        p.update_layout(width=800, height=600, 
                    yaxis_title = "Cantidad", xaxis_title = "Años", 
                    legend=dict(
                                title=dict(text="")
                            )
                    )
        st.markdown("###### Miles de Cabezas (MCabz)")
        if answer == "Vacuno🐮":
            st.plotly_chart(v)
        if answer == "Porcino🐷":
            st.plotly_chart(p)
        with st.expander("Observaciones") :
            st.markdown("")

    with st.container(border=True):
        st.markdown("### 🐔 Mortalidad de gallinas ponedoras")
        #Datos gallinas ponedoras
        gp_muertes = data["aves"]["Indicadores seleccionados de gallinas ponedoras"]["Muertes(Mcabz)"]
        gp_existencia = data["aves"]["Indicadores seleccionados de gallinas ponedoras"]["Existencia promedio(Mcabz)"]
        gp_tasa_mortalidad = data["aves"]["Indicadores seleccionados de gallinas ponedoras"]["Tasa de mortalidad(%)"]
        gp_muertesDF = pd.DataFrame({
            "Existencia promedio": gp_existencia,
            "Muertes de gallinas ponedoras": gp_muertes
    })
            
        gp_tasa_mortalidadDF = pd.DataFrame({
        "Tasa de mortalidad de gallinas ponedoras": gp_tasa_mortalidad
    })
            
        #Selectbox para grafico de area y de linea
        choices5 = st.selectbox( "Selecciona", ["Existencia promedio y mortalidad", "Tasa de mortalidad (%)"])
        gp_muertesDF.index.name = "Año"
        mgp = px.line(gp_muertesDF, hover_name='value', hover_data={'variable': None, 'value':None}, markers=True,color_discrete_sequence=custom_colors)
        mgp.update_layout(width=800, height=600, 
                    yaxis_title = "Cantidad", xaxis_title = "Años", 
                    legend=dict(
                                title=dict(text="")
                            )
                    )
        
        gp_tasa_mortalidadDF.index.name = "Año"
        tm = px.line(gp_tasa_mortalidadDF, hover_name='value', hover_data={'variable': None, 'value':None} ,markers=True,color_discrete_sequence=["#bb0A00"])
        tm.update_layout(width=800, height=600, 
                    yaxis_title = "Cantidad", xaxis_title = "Años", 
                    showlegend = False)

        if choices5 == "Existencia promedio y mortalidad":
            st.markdown("###### Existencia promedio (Miles de Cabezas)")
            st.plotly_chart(mgp)
        if choices5 == "Tasa de mortalidad (%)":
            st.markdown("###### Tasa de Mortalidad (%)")
            st.plotly_chart(tm)
        with st.expander("Observaciones") :
            st.markdown("")
