from folium import Map, GeoJson, GeoJsonPopup, GeoJsonTooltip, Choropleth, LayerControl
import pandas as pd
from geopandas import read_file, GeoDataFrame
from streamlit_folium import st_folium
import streamlit as st


#Datos
province_geo = "data/geojsons/cuba.geojson"
province_data = pd.read_csv("data/csv/US_Unemployment_Oct2012.csv")

#Instanciando Mapa
m = Map(location=[21.5, -79.6], tiles="CartoDB positron", zoom_start=7, no_touch=True, prefer_canvas=True)

#Densidades
Choropleth(
    geo_data=province_geo,
    name="Desempleo",
    data=province_data,
    columns = ['State', 'Unemployment'],
    key_on='feature.properties.province_id',
    fill_color='OrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Tasa de desempleo (%)',
    reset=True,
    control=False
).add_to(m)

#Tooltip
geo_data = read_file("data/geojsons/cuba.geojson")
geodf = GeoDataFrame.from_features(geo_data)
geodf.crs = "EPSG:4326" 
popup = GeoJsonPopup(fields=["province", "province_id"], aliases=["<strong>Provincia:</strong>", "<strong>ID:</strong>"])
tooltip = GeoJsonTooltip(fields=["province", "province_id"], aliases=["<strong>Provincia:</strong>", "<strong>ID:</strong>"],sticky=False)
GeoJson(
    geodf,
    name="A",
    style_function=lambda feature: {"color":"#767676"},
    highlight_function=lambda feature: {"fillColor": "#ffff00"},
    tooltip=tooltip,
    control=False
).add_to(m)

#Display Layer
LayerControl().add_to(m)

map_data = st_folium(m, use_container_width=True, height=550)
    
