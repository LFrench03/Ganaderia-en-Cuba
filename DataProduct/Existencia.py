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
    
    with st.container(border=True):       
        def mostrar(graf):
            st.plotly_chart(graf)
            
        st.subheader("〽️ Distribución del ganado en Cuba")
        opciones = st.selectbox( "Seleccione una opción", ["Total", "Estatal", "No Estatal"],)
        
        # data totales
        vacuno = data["vacuno"]["Total"]  
        porcino = data["porcino"]["Existencia(Mcabz)"]["Total"]
        ovino_caprino = data["ovino_caprino"]["Existencia(Mcabz)"]["Total"]["Total"]
        aves = data["aves"]["Existencia(Mcabz)"]["Existencia total de aves"]
        equido = data["equido"]["Existencia(Mcabz)"]["Total"]
        
        
        #data E y NE
        porcinoE = data["porcino"]["Existencia(Mcabz)"]["Estatal"]
        porcinoNE = {}
        
        for year in porcino:
            if porcino[year] and porcinoE[year]:
                porcinoNE[year] = round(float(porcino[year]) - float(porcinoE[year]), 1) 
        
        ovino_caprinoE = data["ovino_caprino"]["Existencia(Mcabz)"]["Estatal"]["Total"]
        ovino_caprinoNE = {}
        
        for year in ovino_caprino:
            if ovino_caprino[year] and ovino_caprinoE[year]:
                ovino_caprinoNE[year] = round(float(ovino_caprino[year]) - float(ovino_caprinoE[year]), 1) 
        
        avesE = data["aves"]["Existencia(Mcabz)"]["Empresas avicolas estatales"]["Existencia total de aves"]
        aves_1992 = data["aves"]["Existencia(Mcabz)"]["Existencia aves 1992"]
        avesE_1992 = data["aves"]["Existencia(Mcabz)"]["Empresas avicolas estatales"]["Existencia de aves estatal (1992)"]
        avesNE = {}
            
        for year in aves_1992:
            if aves_1992[year] and avesE_1992[year]:
                avesNE[year] = round(float(aves_1992[year]) - float(avesE_1992[year]), 1)        

                
        equidoE = data["equido"]["Existencia(Mcabz)"]["Estatal"]["Total"]
        equidoNE = {}
        
        for year in equido:
            if equido[year] and equidoE[year]:
                equidoNE[year] = round(float(equido[year]) - float(equidoE[year]), 1)    
                    
        
        ganado_TOTAL = pd.DataFrame({
            "Vacuno": vacuno,
            "Porcino": porcino,
            "Ovino Caprino": ovino_caprino,
            "Aves": aves,
            "Equido": equido
            
        })   
        
        ganado_ESTATAL = pd.DataFrame({
            "Porcino": porcinoE,
            "Ovino Caprino": ovino_caprinoE,
            "Aves": avesE,
            "Equido": equidoE
        })
        
        ganado_NO_ESTATAL = pd.DataFrame({
            "Porcino": porcinoNE,
            "Ovino Caprino": ovino_caprinoNE,
            "Aves": avesNE,
            "Equido": equidoNE
        })
        
        
        ganado_TOTAL = ganado_TOTAL.apply(pd.to_numeric)
        ganado_ESTATAL = ganado_ESTATAL.apply(pd.to_numeric)
        ganado_NO_ESTATAL = ganado_NO_ESTATAL.apply(pd.to_numeric)
        
        total = px.line(ganado_TOTAL,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
        total.update_layout(width=800, height=600, 
                        yaxis_title = "Cantidad", xaxis_title = "Años", 
                        legend=dict(
                            title=dict(text="Tipo de ganado")
                        )
                            
                        )
        
        estatal = px.line(ganado_ESTATAL,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
        estatal.update_layout(width=800, height=600, 
                        yaxis_title = "Cantidad", xaxis_title = "Años", 

                        legend=dict(
                            title=dict(text="Tipo de ganado")
                        )
                            
                        )    
        
        NOestatal = px.line(ganado_NO_ESTATAL,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
        NOestatal.update_layout(width=800, height=600, 
                        yaxis_title = "Cantidad", xaxis_title = "Años", 
 
                        legend=dict(
                            title=dict(text="Tipo de ganado")
                        )
                            
                        )       
        

        if opciones == "Total":
            mostrar(total)
        if opciones == "Estatal":
            mostrar(estatal)
        if opciones == "No Estatal":
            mostrar(NOestatal)

        
    with st.container(border=True):
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
        
        st.subheader("📊 Distribución de los distintos tipos de ganado vacuno en Cuba")
        opciones = st.select_slider("Seleccione un año",[x for x in range (1985,2023)])
        def crear_grafica(year):
            fig = px.bar(vacasDF.loc[str(year)])
            fig.update_layout(
            yaxis_title = "Cantidad", xaxis_title = "Ganado vacuno", 
            showlegend = False)
            
            fig.update_traces(width=0.7,
                    marker_line_color="black",
                    marker_line_width=1.5, opacity=0.6)
            fig.data[0].marker.color = ["#FA7070", "#FA7070","#FA7070", "#FA7070","#4793AF", "#4793AF","#4793AF", "#4793AF","#4793AF", "#4793AF","#4793AF"]
            return fig  

        st.plotly_chart(crear_grafica(opciones))

                
          
        exist_ovino = data["ovino_caprino"]["Existencia(Mcabz)"]["Total"]["Ovino"]
        exist_caprino = data["ovino_caprino"]["Existencia(Mcabz)"]["Total"]["Caprino"]
        

        exist_OC = pd.DataFrame({    
            "Ovino": exist_ovino,
            "Caprino": exist_caprino,    

        })

            
        exist_OC = exist_OC.apply(pd.to_numeric)

        st.subheader("Comparación de la existencia del ganado Ovino-Caprino")
        opciones1 = st.select_slider("Seleccione un año",[x for x in range (1990,2023)])
        colors = ['#51829B', '#9BB0C1']
        
        def crear_grafica(year):
            fig = go.Figure(data = go.Pie(labels=["Ovino", "Caprino"], values = exist_OC.loc[str(year)]))
            fig.update_traces(hoverinfo='label+percent', textinfo='label+percent', textfont_size=15,
                        marker=dict(colors=colors, line=dict(color='black', width=3)))
            fig.update_layout(

            width=1300,  
            height=500,  
            margin=dict(l=100, r=100, t=100, b=100)
        )
            
            return fig  

        st.plotly_chart(crear_grafica(opciones1))
        
        
        
        ponedoras = data["aves"]["Existencia(Mcabz)"]["Empresas avicolas estatales"]["Gallinas ponedoras"]
        pollos_ceba = data["aves"]["Existencia(Mcabz)"]["Empresas avicolas estatales"]["Pollos de ceba(Miles de cabezas"]
        reproductoras = data["aves"]["Existencia(Mcabz)"]["Empresas avicolas estatales"]["Reproductoras "]
        carne = data["aves"]["Existencia(Mcabz)"]["Empresas avicolas estatales"]["De carne"]
        ponedoras = data["aves"]["Existencia(Mcabz)"]["Empresas avicolas estatales"]["De ponedoras"]
        otras = data["aves"]["Existencia(Mcabz)"]["Empresas avicolas estatales"]["Otras"]
        

        aves_estatales_tipos = pd.DataFrame({
            "Gallinas ponedoras": ponedoras,
            "Pollos de ceba": pollos_ceba,
            "Reproductoras": reproductoras,
            "De carne": carne,
            "De ponedoras": ponedoras,
            "Otras": otras
                 
        })

        aves_estatales_tipos = aves_estatales_tipos.apply(pd.to_numeric)


        
        opciones3 = st.select_slider("Seleccione un año",[x for x in range (1995,2023)])

        
        def crear_grafica(year):
                
            fig = px.bar(aves_estatales_tipos.loc[str(year)])
            fig.update_layout( 
                        yaxis_title = "Cantidad", xaxis_title = "Tipo de ganado",             
                        legend=dict(
                            title=dict(text="Año")
                        )   ,
                        showlegend=False
                        )
            fig.update_traces(width=0.5,
                            marker_line_color="black",
                            marker_line_width=1.5, opacity=0.6)
            fig.data[0].marker.color = ["#B5C0D0", "#CCD3CA", "#F5E8DD", "#F6B17A", "#B5C99A", "#213555"]
                
            return fig  


        st.plotly_chart(crear_grafica(opciones3))

    with st.expander("Observaciones"):
        st.write("- La cantidad de todos los tipos de ganado está expresada en miles de cabezas")
        st.write("- Los valores de los años que son 0, se deben a que no se encuentran los datos en la ONEI")

        





    with tab2:
        st.header("¿Qué tipo de ganado tiene más densidad de entregas a sacrificios?")
    
        with st.container(border=True):       
            st.subheader("🪓 Comparación de la cantidad de entregas a sacrificios según el tipo de ganado")
            def mostrar(graf):
                st.plotly_chart(graf)
            
            opciones1 = st.selectbox( "", ["Total", "Estatal", "No Estatal"],)


            sacrif_vacunoT = data["vacuno"]["Sacrificios"]["Cabezas(M)"]["Total"]
            sacrif_porcinoT = data["porcino"]["Entregas a sacrificio"]["Total"]["Cabezas(Mcabz)"]
            sacrif_ovT = data["ovino_caprino"]["Entregas a sacrificio"]["Cantidad(Mcabz)"]["Total"]


            sacrif_vacunoE = data["vacuno"]["Sacrificios"]["Cabezas(M)"]["Estatal"]

            sacrif_vacunoNE = {}
                    
            for year in sacrif_vacunoT:
                if sacrif_vacunoT[year] and sacrif_vacunoE[year]:
                    sacrif_vacunoNE[year] = round(float(sacrif_vacunoT[year]) - float(sacrif_vacunoE[year]), 1) 


            sacrif_porcinoE = data["porcino"]["Entregas a sacrificio"]["Estatal"]["Cabezas(Mcabz)"]["Total"]
            sacrif_porcinoNE = {}
                    
            for year in sacrif_porcinoT:
                if sacrif_porcinoT[year] and sacrif_porcinoE[year]:
                    sacrif_porcinoNE[year] = round(float(sacrif_porcinoT[year]) - float(sacrif_porcinoE[year]), 1) 

            sacrif_ovE = data["ovino_caprino"]["Entregas a sacrificio"]["Cantidad(Mcabz)"]["Estatal"]
            sacrif_ovNE = {}

            for year in sacrif_ovT:
                if sacrif_ovT[year] and sacrif_ovE[year]:
                    sacrif_ovNE[year] = round(float(sacrif_ovT[year]) - float(sacrif_ovE[year]), 1) 


            sacrif_TOTAL = pd.DataFrame({
                "Vacuno": sacrif_vacunoT,
                "Porcino": sacrif_porcinoT,
                "Ovino Caprino": sacrif_ovT  
            })   
            
            sacrif_ESTATAL = pd.DataFrame({
                "Vacuno": sacrif_vacunoE,
                "Porcino": sacrif_porcinoE,
                "Ovino Caprino": sacrif_ovE,
            })
            
            sacrif_NO_ESTATAL = pd.DataFrame({
                "Vacuno": sacrif_vacunoNE,
                "Porcino": sacrif_porcinoNE,
                "Ovino Caprino": sacrif_ovNE,
            })


            sacrif_TOTAL = sacrif_TOTAL.apply(pd.to_numeric)
            sacrif_ESTATAL = sacrif_ESTATAL.apply(pd.to_numeric)
            sacrif_NO_ESTATAL = sacrif_NO_ESTATAL.apply(pd.to_numeric)
            
            sacrifT = px.line(sacrif_TOTAL,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
            sacrifT.update_layout(width=800, height=600, 
                            yaxis_title = "Cantidad", xaxis_title = "Años", 
                            
                            legend=dict(
                                title=dict(text="Tipo de ganado")
                            )
                                
                            )
            
            sacrifE = px.line(sacrif_ESTATAL,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
            sacrifE.update_layout(width=800, height=600, 
                            yaxis_title = "Cantidad", xaxis_title = "Años", 
                            
                            legend=dict(
                                title=dict(text="Tipo de ganado")
                            )
                                
                            )    
            
            sacrifNE = px.line(sacrif_NO_ESTATAL,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
            sacrifNE.update_layout(width=800, height=600, 
                            yaxis_title = "Cantidad", xaxis_title = "Años", 
                            
                            legend=dict(
                                title=dict(text="Tipo de ganado")
                            )
                                
                            )       
            

            if opciones1 == "Total":
                mostrar(sacrifT)
            if opciones1 == "Estatal":
                mostrar(sacrifE)
            if opciones1 == "No Estatal":
                mostrar(sacrifNE)



        with st.container(border=True):
            st.subheader("⚖️ Peso en pie y peso promedio del ganado de tipo productor")

            
            
            opciones7 = st.selectbox( "Seleccione una opción", ["Peso en pie", "Peso promedio"],)

            
            
            
            pesoenpie_vacuno = data["vacuno"]["Sacrificios"]["Peso en pie(Mt)"]["Total"]
            pesoenpie_porcino = data["porcino"]["Entregas a sacrificio"]["Total"]["Peso en pie(Mt)"]
            pesoenpie_aves = data["aves"]["Entregas a sacrificio"]["Peso en pie(Mt)"]



            pesoenpieDF = pd.DataFrame({
            "Vacuno": pesoenpie_vacuno,
            "Porcino": pesoenpie_porcino,
            "Aves": pesoenpie_aves,


        })
        
            pesoenpieDF = pesoenpieDF.apply(pd.to_numeric)
            
                
            opciones4 = st.select_slider("  ",[x for x in range (1989,2023)])
            colors = ['#9BABB8','#EEE3CB','#D7C0AE']
                
            def crear_grafica(year):
                pe = go.Figure(data = go.Pie(labels=["Vacuno", "Porcino", "Aves"], values = pesoenpieDF.loc[str(year)]))
                pe.update_traces(hoverinfo='label+percent', textinfo='label+percent', textfont_size=15,
                            marker=dict(colors=colors, line=dict(color='black', width=1.5)))
                pe.update_layout(
                title_text="Peso en pie del ganado de tipo productor (Mt)",
                showlegend = False,
                width=2000,  
                height=500,  
            
            )
                return pe  

            pe = crear_grafica(opciones4)





            pesopromedio_vacuno = data["vacuno"]["Sacrificios"]["Peso Promedio(Kg)"]["Total"]
            pesopromedio_porcino = data["porcino"]["Entregas a sacrificio"]["Total"]["Peso promedio(kg)"]
           
    
            pesopromedioDF = pd.DataFrame({
            "Vacuno": pesopromedio_vacuno,
            "Porcino": pesopromedio_porcino,
        })

            pesopromedioDF = pesopromedioDF.apply(pd.to_numeric)
            
                
            
            colors = ['#9BABB8', '#EEE3CB']
                
            def crear_grafica(year):
                pp = go.Figure(data = go.Pie(labels=["Vacuno", "Porcino"], values = pesopromedioDF.loc[str(year)]))
                pp.update_traces(hoverinfo='label+percent', textinfo='label+percent', textfont_size=15,
                            marker=dict(colors=colors, line=dict(color='black', width=1.5)))
                pp.update_layout(
                title_text="Peso promedio del ganado de tipo productor (Kg)",
                showlegend = False,
                width=2000,  
                height=500,  
            
            )
                return pp  

            pp = crear_grafica(opciones4)


            def mostrar_slide(graf):
                st.plotly_chart(graf)
            

            if opciones7 == "Peso en pie":
                mostrar(pe)
            if opciones7 == "Peso promedio":
                mostrar(pp)




        with st.container(border=True):
            st.subheader("🪓 Comparación de la cantidad de entregas a sacrificios del ganado porcino de ceba respecto al total")

            slider = st.select_slider(" ",[x for x in range (1989,2013)])

            porcino_total_estatal = data["porcino"]["Entregas a sacrificio"]["Estatal"]["Cabezas(Mcabz)"]["Total"]
            porcino_ceba = data["porcino"]["Entregas a sacrificio"]["Estatal"]["Cabezas(Mcabz)"]["Ceba"]


            porcino_ceba_totaalDF = pd.DataFrame({
              "Ganado porcino de ceba": porcino_ceba,
              "Ganado porcino estatal": porcino_total_estatal

            })
            

            porcino_ceba_totaalDF = porcino_ceba_totaalDF.apply(pd.to_numeric)

            colors = ['#BC9F8B', '#EEE3CB']
            def crear_grafica(year):
                fig = go.Figure(data = go.Pie(labels=["Ganado porcino de ceba", "Ganado porcino estatal"], values = porcino_ceba_totaalDF.loc[str(year)]))
                fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=15,
                            marker=dict(colors=colors, line=dict(color='black', width=1.5)))
                fig.update_layout(
                    legend=dict(
                                title=dict(text="Sacrificios")
                            ),
                width=2000,  
                height=500,  
            
            )
                return fig  

            st.plotly_chart(crear_grafica(slider))


        with st.container(border=True):
            st.subheader("🐓 Entregas a sacrificio de pollos de ceba")

            pollosceba_sacrifT = data["aves"]["Entregas a sacrificio"]["Pollos de ceba entrega a sacrificio"]["Cantidad(Mcabz)"]

            pollosceba_sacrif_dataframe = pd.DataFrame({
              "Pollos de ceba entregados a sacrificio": pollosceba_sacrifT,

            })
            

            pollosceba_sacrif_dataframe = pollosceba_sacrif_dataframe.apply(pd.to_numeric)


            fig = px.area(pollosceba_sacrif_dataframe,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
            fig.update_layout(width=800, height=600, 
                    yaxis_title = "Cantidad", xaxis_title = "Años", 
                    title = "Cantidad total de entregas a sacrificio de pollos de ceba",
                    showlegend = False)


            st.plotly_chart(fig)




            def mostrar(graf):
                st.plotly_chart(graf)


            choices3 = st.selectbox( "Seleccione una opción", ["Pienso consumido por ave", "Conversión de pienso en carne"],)

            pienso_consumido_ave = data["aves"]["Entregas a sacrificio"]["Pollos de ceba entrega a sacrificio"]["Pienso consumido por ave(kg)"]
            convers_pienso_carne = data["aves"]["Entregas a sacrificio"]["Pollos de ceba entrega a sacrificio"]["Conversion de pienso en carne(kg)"]

            pcDF = pd.DataFrame({
              "Pienso consumido por ave": pienso_consumido_ave,
            })

            cpDF = pd.DataFrame({
              "Conversión de pienso en carne": convers_pienso_carne,
            })

            pcDF = pcDF.apply(pd.to_numeric)

            cpDF = cpDF.apply(pd.to_numeric)


            pc = px.line(pcDF,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
            pc.update_layout(width=800, height=600, 
                    yaxis_title = "Cantidad", xaxis_title = "Años", 
                    title = "Pienso consumido por ave (kg)",
                    showlegend = False)
            
            cp = px.line(cpDF,markers=True,color_discrete_sequence=px.colors.qualitative.Pastel1)
            cp.update_layout(width=800, height=600, 
                    yaxis_title = "Cantidad", xaxis_title = "Años", 
                    title = "Conversión de pienso en carne (kg)",
                    showlegend = False)



            if choices3 == "Pienso consumido por ave":
                mostrar(pc)
            if choices3 == "Conversión de pienso en carne":
                mostrar(cp)


        with st.expander("Observaciones"):
                st.write("- La cantidad de todos los tipos de ganado está expresada en miles de cabezas")
                st.write("- Los valores de los años que son 0, se deben a que no se encuentran los datos en la ONEI")
                st.write("- Mt: toneladas métricas")





