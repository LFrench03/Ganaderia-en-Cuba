from streamlit_folium import st_folium
import streamlit as st
from folium import Map, GeoJson, GeoJsonPopup, GeoJsonTooltip, Choropleth, LayerControl
import pandas as pd
from geopandas import read_file, GeoDataFrame
import plotly.graph_objects as go
from numpy import nan
import json 

#Datos
with open("inventario_ganado.json") as json_file:
    data = json.load(json_file)

province_geo = "data/geojsons/cuba.geojson"
ids = ["art","cam","cav","cfg", "gra", "gtm", "hol" , "ijv" ,"lha","ltu" ,"mat"
       ,"may","pri","ssp","stg","vcl"]
lista_prov = ["Artemisa", "Camaguey","Ciego de Avila","Cienfuegos","Granma","La Habana","Matanzas","Sancti Spiritus","Las Tunas","Holguin","Santiago de Cuba","Isla de la Juventud"
              ,"Villa Clara","Guantanamo","Pinar del Rio","Mayabeque"]
lista_prov = sorted(lista_prov)
dt2012 = {}
dt2013 = {}
dt2014 = {}
dt2015 = {}
dt2016 = {}
dt2017 = {}
l1 = [dt2012,dt2013,dt2014,dt2015,dt2016,dt2017]
for df, year in list(zip(l1,[str(x) for x in range(2012, 2018)])):
    for id,prov in list(zip(ids, lista_prov)):
        if data["Instituciones"]["Tenientes de tierras"][year][prov] != "Cuba":
            df[id] = data["Instituciones"]["Tenientes de tierras"][year][prov]["Total"]
dp2012 = {}
dp2013 = {}
dp2014 = {}
dp2015 = {}
dp2016 = {}
dp2017 = {}
l1 = [dp2012,dp2013,dp2014,dp2015,dp2016,dp2017]
for df, year in list(zip(l1,[str(x) for x in range(2012, 2018)])):
    for id,prov in list(zip(ids, lista_prov)):
        if data["Instituciones"]["Por Provincias"][year][prov] != "Cuba":
            df[id] = data["Instituciones"]["Por Provincias"][year][prov]["Total"]
dt2012 = pd.DataFrame({"Val":dt2012})
dt2012["ID"] = dt2012.index
dt2012["index"] = [x for x in range(16)]
dt2012.set_index("index", inplace=True)
dt2012.index.name=None
dt2013 = pd.DataFrame({"Val":dt2013})
dt2013["ID"] = dt2013.index
dt2013["index"] = [x for x in range(16)]
dt2013.set_index("index", inplace=True)
dt2013.index.name=None
dt2014 = pd.DataFrame({"Val":dt2014})
dt2014["ID"] = dt2014.index
dt2014["index"] = [x for x in range(16)]
dt2014.set_index("index", inplace=True)
dt2014.index.name=None
dt2015 = pd.DataFrame({"Val":dt2015})
dt2015["ID"] = dt2015.index
dt2015["index"] = [x for x in range(16)]
dt2015.set_index("index", inplace=True)
dt2015.index.name=None
dt2016 = pd.DataFrame({"Val":dt2016})
dt2016["ID"] = dt2016.index
dt2016["index"] = [x for x in range(16)]
dt2016.set_index("index", inplace=True)
dt2016.index.name=None
dt2017 = pd.DataFrame({"Val":dt2017})
dt2017["ID"] = dt2017.index
dt2017["index"] = [x for x in range(16)]
dt2017.set_index("index", inplace=True)
dt2017.index.name=None
dp2012 = pd.DataFrame({"Val":dp2012})
dp2012["ID"] = dp2012.index
dp2012["index"] = [x for x in range(16)]
dp2012.set_index("index", inplace=True)
dp2012.index.name=None
dp2013 = pd.DataFrame({"Val":dp2013})
dp2013["ID"] = dp2013.index
dp2013["index"] = [x for x in range(16)]
dp2013.set_index("index", inplace=True)
dp2013.index.name=None
dp2014 = pd.DataFrame({"Val":dp2014})
dp2014["ID"] = dp2014.index
dp2014["index"] = [x for x in range(16)]
dp2014.set_index("index", inplace=True)
dp2014.index.name=None
dp2015 = pd.DataFrame({"Val":dp2015})
dp2015["ID"] = dp2015.index
dp2015["index"] = [x for x in range(16)]
dp2015.set_index("index", inplace=True)
dp2015.index.name=None
dp2016 = pd.DataFrame({"Val":dp2016})
dp2016["ID"] = dp2016.index
dp2016["index"] = [x for x in range(16)]
dp2016.set_index("index", inplace=True)
dp2016.index.name=None
dp2017 = pd.DataFrame({"Val":dp2017})
dp2017["ID"] = dp2017.index
dp2017["index"] = [x for x in range(16)]
dp2017.set_index("index", inplace=True)
dp2017.index.name=None
popover = st.popover("Filtrado de datos")
choice = popover.selectbox("Seleccione",["Entidades por provincia", "Tenientes de tierras por provincia"])

if choice == "Entidades por provincia":
    l1 = [dp2012,dp2013,dp2014,dp2015,dp2016,dp2017]
    st.markdown("#### 🗺 Entidades por provincia")
    years = [x for x in range(2012, 2017)] #Se selecciona hasta el 2016 por un aparente error con el toggle que lo recibe siempre con la capital excluida por alguna razon
    year = st.select_slider("Año", years)
    toggle = st.toggle("Excluir la capital")
    if toggle:
        def mapa(year):
            #Instanciando Mapa
            m = Map(location=[21.3, -79.6], tiles="CartoDB positron", zoom_start=7, control_scale=True, no_touch=True)
            province_data = l1[years.index(year)]
            exc = pd.concat([province_data.iloc[:8,:], province_data.iloc[9:,:]], ignore_index=True, sort=False)
            #Densidades
            Choropleth(
                geo_data="data/geojsons/cuba_without_havana.geojson",
                name="Entidades",
                data=exc,
                columns = ['ID', 'Val'],
                key_on='feature.properties.province_id',
                fill_color='OrRd',
                fill_opacity=0.7,
                line_opacity=0.2,
                legend_name='Entidades (Unidad)',
                reset=True,
                control=False
            ).add_to(m)
            #Popup & Tooltip
            geo_data = read_file("data/geojsons/cuba.geojson")
            geodf = GeoDataFrame.from_features(geo_data)
            geodf.crs = "EPSG:4326"
            if year==2012:
                popup = GeoJsonPopup(fields=["province","Entidades"+str(year)+"Total","Entidades"+str(year)+"Empresas","Entidades"+str(year)+"Presupuestadas","Entidades"+str(year)+"Cooperativas"], 
                                    aliases=["<strong>Provincia:</strong>", "<strong>Total:</strong>", "<strong>Empresas:</strong>", "<strong>Presupuestadas:</strong>", "<strong>Cooperativas:</strong>"])
                tooltip = GeoJsonTooltip(fields=["province","Entidades"+str(year)+"Total","Entidades"+str(year)+"Empresas","Entidades"+str(year)+"Presupuestadas","Entidades"+str(year)+"Cooperativas"], 
                                    aliases=["<strong>Provincia:</strong>", "<strong>Total:</strong>", "<strong>Empresas:</strong>", "<strong>Presupuestadas:</strong>", "<strong>Cooperativas:</strong>"],
                                        sticky=False)
            if year == 2013: 
                popup = GeoJsonPopup(fields=["province","Entidades"+str(year)+"Total","Entidades"+str(year)+"Empresas","Entidades"+str(year)+"Sociedades Mercantiles","Entidades"+str(year)+"CTotal","Entidades"+str(year)+"UBPC","Entidades"+str(year)+"CPA","Entidades"+str(year)+"CCS","Entidades"+str(year)+"Presupuestadas"], 
                                    aliases=["<strong>Provincia:</strong>", "<strong>Total:</strong>", "<strong>Empresas:</strong>", "<strong>Sociedades Mercantiles:</strong>", "<strong>Cooperativas:</strong>", "<strong>UBPC:</strong>", "<strong>CPA:</strong>", "<strong>CCS:</strong>","<strong>Presupuestadas:</strong>"])
                tooltip = GeoJsonTooltip(fields=["province","Entidades"+str(year)+"Total","Entidades"+str(year)+"Empresas","Entidades"+str(year)+"Sociedades Mercantiles","Entidades"+str(year)+"CTotal","Entidades"+str(year)+"UBPC","Entidades"+str(year)+"CPA","Entidades"+str(year)+"CCS","Entidades"+str(year)+"Presupuestadas"], 
                                        aliases=["<strong>Provincia:</strong>", "<strong>Total:</strong>", "<strong>Empresas:</strong>", "<strong>Sociedades Mercantiles:</strong>", "<strong>Cooperativas:</strong>", "<strong>UBPC:</strong>", "<strong>CPA:</strong>", "<strong>CCS:</strong>", "<strong>Presupuestadas:</strong>"],
                                        sticky=False)
            if year > 2013:
                popup = GeoJsonPopup(fields=["province","Entidades"+str(year)+"Total","Entidades"+str(year)+"Empresas","Entidades"+str(year)+"Sociedades Mercantiles","Entidades"+str(year)+"CTotal","Entidades"+str(year)+"CNoA","Entidades"+str(year)+"UBPC","Entidades"+str(year)+"CPA","Entidades"+str(year)+"CCS","Entidades"+str(year)+"Presupuestadas"], 
                                    aliases=["<strong>Provincia:</strong>", "<strong>Total:</strong>", "<strong>Empresas:</strong>", "<strong>Sociedades Mercantiles:</strong>", "<strong>Cooperativas:</strong>", "<strong>CNoA:</strong>", "<strong>UBPC:</strong>", "<strong>CPA:</strong>", "<strong>CCS:</strong>","<strong>Presupuestadas:</strong>"])
                tooltip = GeoJsonTooltip(fields=["province","Entidades"+str(year)+"Total","Entidades"+str(year)+"Empresas","Entidades"+str(year)+"Sociedades Mercantiles","Entidades"+str(year)+"CTotal","Entidades"+str(year)+"CNoA","Entidades"+str(year)+"UBPC","Entidades"+str(year)+"CPA","Entidades"+str(year)+"CCS","Entidades"+str(year)+"Presupuestadas"], 
                                    aliases=["<strong>Provincia:</strong>", "<strong>Total:</strong>", "<strong>Empresas:</strong>", "<strong>Sociedades Mercantiles:</strong>", "<strong>Cooperativas:</strong>", "<strong>CNoA:</strong>", "<strong>UBPC:</strong>", "<strong>CPA:</strong>", "<strong>CCS:</strong>","<strong>Presupuestadas:</strong>"],
                                        sticky=False)
            GeoJson(
                geodf,
                name="Datos",
                style_function=lambda feature: {"color":"#767676"},
                highlight_function=lambda feature: {"fillColor": "#ffff00"},
                popup=popup,
                tooltip=tooltip,
                control=False
            ).add_to(m)

            return st_folium(m, use_container_width=True, height=550)
        map_data = mapa(year)

    else:
        def mapa(year):
            #Instanciando Mapa
            m = Map(location=[21.3, -79.6], tiles="CartoDB positron", zoom_start=7, control_scale=True, no_touch=True)
            province_data = l1[years.index(year)]
            #Densidades
            Choropleth(
                geo_data=province_geo,
                name="Entidades",
                data=province_data,
                columns = ['ID', 'Val'],
                key_on='feature.properties.province_id',
                fill_color='OrRd',
                fill_opacity=0.7,
                line_opacity=0.2,
                legend_name='Entidades',
                reset=True,
                control=False
            ).add_to(m)
            #Tooltip
            geo_data = read_file("data/geojsons/cuba.geojson")
            geodf = GeoDataFrame.from_features(geo_data)
            geodf.crs = "EPSG:4326"
            if year==2012:
                popup = GeoJsonPopup(fields=["province","Entidades"+str(year)+"Total","Entidades"+str(year)+"Empresas","Entidades"+str(year)+"Presupuestadas","Entidades"+str(year)+"Cooperativas"], 
                                    aliases=["<strong>Provincia:</strong>", "<strong>Total:</strong>", "<strong>Empresas:</strong>", "<strong>Presupuestadas:</strong>", "<strong>Cooperativas:</strong>"])
                tooltip = GeoJsonTooltip(fields=["province","Entidades"+str(year)+"Total","Entidades"+str(year)+"Empresas","Entidades"+str(year)+"Presupuestadas","Entidades"+str(year)+"Cooperativas"], 
                                    aliases=["<strong>Provincia:</strong>", "<strong>Total:</strong>", "<strong>Empresas:</strong>", "<strong>Presupuestadas:</strong>", "<strong>Cooperativas:</strong>"],
                                        sticky=False)
            if year == 2013: 
                popup = GeoJsonPopup(fields=["province","Entidades"+str(year)+"Total","Entidades"+str(year)+"Empresas","Entidades"+str(year)+"Sociedades Mercantiles","Entidades"+str(year)+"CTotal","Entidades"+str(year)+"UBPC","Entidades"+str(year)+"CPA","Entidades"+str(year)+"CCS","Entidades"+str(year)+"Presupuestadas"], 
                                    aliases=["<strong>Provincia:</strong>", "<strong>Total:</strong>", "<strong>Empresas:</strong>", "<strong>Sociedades Mercantiles:</strong>", "<strong>Cooperativas:</strong>", "<strong>UBPC:</strong>", "<strong>CPA:</strong>", "<strong>CCS:</strong>","<strong>Presupuestadas:</strong>"])
                tooltip = GeoJsonTooltip(fields=["province","Entidades"+str(year)+"Total","Entidades"+str(year)+"Empresas","Entidades"+str(year)+"Sociedades Mercantiles","Entidades"+str(year)+"CTotal","Entidades"+str(year)+"UBPC","Entidades"+str(year)+"CPA","Entidades"+str(year)+"CCS","Entidades"+str(year)+"Presupuestadas"], 
                                        aliases=["<strong>Provincia:</strong>", "<strong>Total:</strong>", "<strong>Empresas:</strong>", "<strong>Sociedades Mercantiles:</strong>", "<strong>Cooperativas:</strong>", "<strong>UBPC:</strong>", "<strong>CPA:</strong>", "<strong>CCS:</strong>", "<strong>Presupuestadas:</strong>"],
                                        sticky=False)
            if year > 2013:
                popup = GeoJsonPopup(fields=["province","Entidades"+str(year)+"Total","Entidades"+str(year)+"Empresas","Entidades"+str(year)+"Sociedades Mercantiles","Entidades"+str(year)+"CTotal","Entidades"+str(year)+"CNoA","Entidades"+str(year)+"UBPC","Entidades"+str(year)+"CPA","Entidades"+str(year)+"CCS","Entidades"+str(year)+"Presupuestadas"], 
                                    aliases=["<strong>Provincia:</strong>", "<strong>Total:</strong>", "<strong>Empresas:</strong>", "<strong>Sociedades Mercantiles:</strong>", "<strong>Cooperativas:</strong>", "<strong>CNoA:</strong>", "<strong>UBPC:</strong>", "<strong>CPA:</strong>", "<strong>CCS:</strong>","<strong>Presupuestadas:</strong>"])
                tooltip = GeoJsonTooltip(fields=["province","Entidades"+str(year)+"Total","Entidades"+str(year)+"Empresas","Entidades"+str(year)+"Sociedades Mercantiles","Entidades"+str(year)+"CTotal","Entidades"+str(year)+"CNoA","Entidades"+str(year)+"UBPC","Entidades"+str(year)+"CPA","Entidades"+str(year)+"CCS","Entidades"+str(year)+"Presupuestadas"], 
                                        aliases=["<strong>Provincia:</strong>", "<strong>Total:</strong>", "<strong>Empresas:</strong>", "<strong>Sociedades Mercantiles:</strong>", "<strong>Cooperativas:</strong>", "<strong>CNoA:</strong>", "<strong>UBPC:</strong>", "<strong>CPA:</strong>", "<strong>CCS:</strong>","<strong>Presupuestadas:</strong>"],
                                        sticky=False)
            GeoJson(
                geodf,
                name="Datos",
                style_function=lambda feature: {"color":"#767676"},
                highlight_function=lambda feature: {"fillColor": "#ffff00"},
                popup=popup,
                tooltip=tooltip,
                control=False
            ).add_to(m)

            return st_folium(m, use_container_width=True, height=550)
        map_data = mapa(year)

if choice == "Tenientes de tierras por provincia":
    st.markdown("#### 🗺 Tenientes de tierra por provincia")
    l1 = [dt2012,dt2013,dt2014,dt2015,dt2016,dt2017]
    years = [x for x in range(2012, 2018)]
    year = st.select_slider("Año", years)
    def mapa(year):
        #Instanciando Mapa
        m = Map(location=[21.3, -79.6], tiles="CartoDB positron", zoom_start=7, control_scale=True, no_touch=True)
        province_data = l1[years.index(year)]
        #Densidades
        Choropleth(
            geo_data=province_geo,
            name="Tenientes de Tierras",
            data=province_data,
            columns = ['ID', 'Val'],
            key_on='feature.properties.province_id',
            fill_color='OrRd',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Tenientes de Tierras (Unidad)',
            reset=True,
            control=False
        ).add_to(m)
        #Tooltip
        geo_data = read_file("data/geojsons/cuba.geojson")
        geodf = GeoDataFrame.from_features(geo_data)
        geodf.crs = "EPSG:4326"
        if year == 2012:
            popup = GeoJsonPopup(fields=["province","Tierras"+str(year)+"Total","Tierras"+str(year)+"Granjas","Tierras"+str(year)+"UBPC","Tierras"+str(year)+"CPA","Tierras"+str(year)+"Otros"], 
                                aliases=["<strong>Provincia:</strong>", "<strong>Total:</strong>", "<strong>Granjas:</strong>", "<strong>UBPC:</strong>", "<strong>CPA:</strong>", "<strong>Otros:</strong>"])
            tooltip = GeoJsonTooltip(fields=["province","Tierras"+str(year)+"Total","Tierras"+str(year)+"Granjas","Tierras"+str(year)+"UBPC","Tierras"+str(year)+"CPA","Tierras"+str(year)+"Otros"], 
                                    aliases=["<strong>Provincia:</strong>", "<strong>Total:</strong>", "<strong>Granjas:</strong>", "<strong>UBPC:</strong>", "<strong>CPA:</strong>", "<strong>Otros:</strong>"],
                                    sticky=False)
        if year > 2012: 
            popup = GeoJsonPopup(fields=["province","Tierras"+str(year)+"Total","Tierras"+str(year)+"Granjas","Tierras"+str(year)+"UBPC","Tierras"+str(year)+"CPA","Tierras"+str(year)+"CCS"], 
                                aliases=["<strong>Provincia:</strong>", "<strong>Total:</strong>", "<strong>Granjas:</strong>", "<strong>UBPC:</strong>", "<strong>CPA:</strong>", "<strong>CCS:</strong>"])
            tooltip = GeoJsonTooltip(fields=["province","Tierras"+str(year)+"Total","Tierras"+str(year)+"Granjas","Tierras"+str(year)+"UBPC","Tierras"+str(year)+"CPA","Tierras"+str(year)+"CCS"], 
                                    aliases=["<strong>Provincia:</strong>", "<strong>Total:</strong>", "<strong>Granjas:</strong>", "<strong>UBPC:</strong>", "<strong>CPA:</strong>", "<strong>CCS:</strong>"],
                                    sticky=False)
        GeoJson(
            geodf,
            name="Datos",
            style_function=lambda feature: {"color":"#767676"},
            highlight_function=lambda feature: {"fillColor": "#ffff00"},
            popup=popup,
            tooltip=tooltip,
            control=False
        ).add_to(m)

        return st_folium(m, use_container_width=True, height=550)
    map_data = mapa(year)

#Datos Entidades
general = {}    #generales
for year in data["Entidades"]:
    general[year] = {}
    for key in data["Entidades"][year]:
        if key == "Cooperativas":
            general[year]["Cooperativas"] = int(data["Entidades"][year][key]["Total"])
        else:
            general[year][key] = int(data["Entidades"][year][key])
dfg = pd.DataFrame(general)
dfg = dfg.transpose()
dfg = dfg.iloc[:,1:]

cooperativas = {}   #solo cooperativas
for year in data["Entidades"]:
    cooperativas[year] = {}
    for key in data["Entidades"][year]["Cooperativas"]:
        if data["Entidades"][year]["Cooperativas"][key] == "":
            cooperativas[year][key] = nan
        else:
            cooperativas[year][key] = data["Entidades"][year]["Cooperativas"][key]
dfc = pd.DataFrame(cooperativas)
dfc = dfc.transpose()
dfc = dfc.iloc[9:,:]
dfc = dfc.iloc[:,1:]
opciones = st.selectbox("Selecciones", ["General", "Cooperativas"])
col1, col2 = st.columns(2)
with col1:
    def crear_grafica(year):
        colors = ['#ff0000', '#950e0e', '#ff8686']
        fig = go.Figure(data = go.Pie(labels=["Empresas", "Cooperativas", "Presupuestadas"], values = dfg.loc[str(year)],pull= 0.1, textposition="outside", hoverinfo='value',textinfo='label+percent', 
                marker=dict(colors=colors, line=dict(color='black', width=3))))
        fig.update_layout(
                width=1300,  
                height=500,  
                margin=dict(l=100, r=100, t=100, b=100))
        return fig 
    def crear_grafica2(year):
        colors = ['#ff0000', '#510808', '#950e0e', '#ff8686']
        fig = go.Figure(data = go.Pie(labels=["CNoA" ,"UBPC", "CPA", "CCS"],values = dfc.loc[str(year)],pull= 0.1, textposition="outside", hoverinfo='value',textinfo='label+percent', 
                marker=dict(colors=colors, line=dict(color='black', width=3))))
        fig.update_layout(
                width=1300,  
                height=500,  
                margin=dict(l=100, r=100, t=100, b=100))
        return fig
    if opciones == "General" :
        st.markdown("#### Número de Entidades")
        date = st.select_slider("Año", [x for x in range(1999, 2022)])
        st.plotly_chart(crear_grafica(date))
    if opciones == "Cooperativas" :
        st.markdown("#### Número de Cooperativas")
        date = st.select_slider("Año", [x for x in range(2008, 2022)])
        st.plotly_chart(crear_grafica2(date))
with col2:
    with st.expander("Observaciones"):
        st.write("A")
