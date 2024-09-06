import streamlit as st

def descargar_json(ruta_archivo):
    with open(ruta_archivo, 'rb') as f:
        st.download_button(
            label="Descargar Json",
            data=f,
            file_name='inventario_ganado.json',
            mime='application/json'
        )
def descargar_geojson(ruta_archivo):
    with open(ruta_archivo, 'rb') as f:
        st.download_button(
            label="Descargar GeoJson",
            data=f,
            file_name='cuba.geojson',
            mime='application/geojson'
        )

st.markdown('<p style=font-size:22px;font-weight:bold;color:rgb(0,87,214);"><i>Referencias:</i></p>', unsafe_allow_html=True)
st.markdown('* *Repositorio del proyecto [Entrar aquí](https://github.com/LFrench03/Ganaderia-en-Cuba)*')
st.markdown('* *Sitio web de la Oficina Nacional de Estadísticas e Información [Entrar aquí](https://www.onei.gob.cu/)*')
st.markdown('* *Repositorio de Yudivian Almeida con los datos geolocalizables en formato geojson de las provincias y municipios de Cuba [Entrar aquí](https://github.com/yudivian/cuba-geojsons/tree/master)*')
st.markdown('* *Documentación de Plotly [Entra aquí](https://plotly.com/python/)*')
st.markdown('* *Documentación de Streamlit [Entra aquí](https://docs.streamlit.io/develop/api-reference)*')
st.markdown('<p style=font-size:22px;font-weight:bold;color:rgb(0,87,214);"><i>Notas:</i></p>', unsafe_allow_html=True)
st.markdown('* <p style=font-size:17px;font-weight:bold;color:gray;"><i>La mayor parte de los datos utilizados provienen de la ONEI y están disponibles en formato CSV en las observaciones de cada representación con los DataFrames correspondientes de las secciones del análisis. Durante el proceso de desarrollo de este proyecto se tuvieron que procesar cada uno de los datos y someterlos a un robusto Análisis Exploratorio, en cuyo proceso se determinó almacenar todo en un archivo Json como base de datos con todos los datos ya procesados. Para esta tarea se desarrollaron scripts en el lenguaje de programación Python para automatizar lo máximo posible cada uno de los procesos.</i></p>', unsafe_allow_html=True)
st.markdown('* <p style=font-size:17px;font-weight:bold;color:gray;"><i>Además, se hizo uso de una base de datos de coordenadas geolocalizables para instanciar el mapa con sus divisiones por provincias correctamente asignadas. Para ello se contó con la fortuna de poder aprovechar el repositorio de geojson de nuestro profesor y jefe de carrera Yudivian Almeida.</i></p>', unsafe_allow_html=True)
st.markdown('* <p style=font-size:17px;font-weight:bold;color:gray;"><i>Cabe mencionar que además de los datos de las series estadisticas publicadas por la ONEI también se incluyeron en las observaciones aclaraciones y especificaciones de conceptos obtenidas de los anuarios estadísticos que nos ofrece la misma.</i></p>', unsafe_allow_html=True)
st.markdown('<p style=font-size:22px;font-weight:bold;color:rgb(0,87,214);"><i>Contenido descargable:</i></p>', unsafe_allow_html=True)
rutaJSON = "inventario_ganado.json"
rutaGeoJson = "data/geojsons/cuba.geojson"
with st.popover("Descargar"):
    c1,c2 = st.columns(2)
    with c1:
        descargar_json(rutaJSON)
    with c1:
        descargar_geojson(rutaGeoJson)
