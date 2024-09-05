import streamlit as st


col1, col2, col3 = st.columns(3)

with col2:
    st.image("brand/PNG/Identificador_principal.png", use_column_width=True)

with st.expander("¿Quiénes somos?"):
    st.write("Un equipo de estudiantes de la carrera de Ciencia de Datos que ha emprendido una investigación sobre uno de los temas más controvertidos en Cuba: la ganadería. Como parte de este proyecto académico, han creado un identificador único llamado DataPecuario. Este identificador funciona como una marca para representar el conjunto resultante de la fusión de todas las partes independientes en las que se divide esta investigación exhaustiva sobre el sector pecuario cubano.")
    st.write("DataPecuario opera como un elemento centralizador, integrando y facilitando el acceso a los datos recopilados a lo largo del estudio. Este enfoque permite una visualización más clara y comprensible de la información relacionada con la ganadería en Cuba.")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown('<p style="font-family: sans-serif;font-size: 20px;font-weight: bold;"><i style="color:rgb(0,87,214);">DataPecuario:</i> <l style= "color:rgb(0,33,66);">La ganadería cubana en datos</l></p>', unsafe_allow_html=True)
    

with st.expander("¿Cuál es nuestro objetivo principal?"):
    st.write("Basándonos en los datos proporcionados por la Oficina Nacional de Estadísticas e Información (ONEI), nuestro principal objetivo es presentar una visión detallada de cómo ha evolucionado la ganadería en Cuba durante el período que abarca desde 1985 hasta 2022. A través del análisis exhaustivo, buscamos comprender y exponer los desafíos que enfrenta actualmente el sector ganadero cubano, como las limitaciones económicas y la alimentación del propio ganado.")
    st.write("De esta forma, nuestro estudio se centra en identificar las tendencias más significativas y evaluar el impacto de diferentes variables sobre la producción ganadera.")



st.markdown('<p style="font-family: sans-serif;color:rgb(0,87,214);font-size: 35px;font-weight: bold;"><i>¿Qué se puede encontrar en nuestro DataProduct?</i></p>', unsafe_allow_html=True)
st.markdown('<p style=font-size:17px;font-weight:bold;color:gray;"><i>Por medio de la barra lateral plegable de la izquierda observamos que el contenido de la página se encuentra dividido en las secciones: "Ganado", "Entidades" y "Acerca de", donde se distribuyeron las diferentes páginas con los siguientes análisis:</i></p>', unsafe_allow_html=True)

st.markdown('<p style=font-size:24px;font-weight:bold;color:rgb(0,33,66);"><i>- Ganado:</i></p>', unsafe_allow_html=True)
st.markdown("Existencia: Sección dividida en tres pestañas, 'Existencia del ganado', 'Entregas a sacrificio' y 'Natalidad y Mortalidad'. En la primera pestaña se analiza la distribución de los diferentes tipos de ganado, así como su evolución a lo largo del tiempo. La siguiente tabulación abarca lo relacionado con las entregas a sacrificio de los distintos sectores ganaderos con comparaciones gráficas interactivas. Y culmina la sección con su última parte, donde se analiza el comportamiento de los nacimientos y muertes del ganado y tasas.")
st.markdown("Producción: De igual forma que la sección anterior contiene tres tabulaciones, que en este caso son: 'Producción de leche', 'Producción avícola' y 'Alimentación del ganado'. El contenido en Producción de leche, se enfoca en un estudio sobre la leche producida en Cuba según el tipo de ganado y el rendimiento del ganado de ordeño. Luego, la segunda pestaña se centra específicamente en el rendimieno de la producción avícola (carne y huevos). Para terminar en la tercera pestaña se estudia la alimentación del ganado considerando los diferentes valores de importaciones con este destino, además de abordar las relaciones de consumo de pienso en aves y considerar el factor económico del PIB para este sector.")
st.markdown('<p style=font-size:24px;font-weight:bold;color:rgb(0,33,66);"><i>- Entidades:</i></p>', unsafe_allow_html=True)
st.markdown("Instituciones: En esta página individual sin pestañas se contiene la distribucion geográfica interactiva por provincias de las diferentes instituciones y tierras de la isla en un período de tiempo desde el 2012 hasta el 2016. En la parte inferior se considera el número de entidades (de forma general y por tipo de cooperativas) en un período de tiempo más prolongado.")
st.markdown('<p style=font-size:24px;font-weight:bold;color:rgb(0,33,66);"><i>- Acerca de:</i></p>', unsafe_allow_html=True)
st.markdown("Metodología: Referencias, contenido descargable de los datos utilizados (procesados y sin procesar), entre otros.")

st.markdown('<p style=font-size:15px;font-weight:bold;color:rgb(0,87,214);"><i>Posdata: Notar que para cada gráfica se incluyen desplegables con información adicional e indicaciones sobre la interactividad de las mismas.</i></p>', unsafe_allow_html=True)