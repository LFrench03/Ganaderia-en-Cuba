import streamlit as st


col1, col2, col3 = st.columns(3)

with col2:
    st.image("brand/PNG/Identificador_principal.png", width=350)

with st.expander("¿Cuál es nuestro objetivo principal?"):
    st.write("Utilizando los datos de la Oficina Nacional de Estadística e Información (ONEI) como base, nuestro objetivo principal es dar a conocer cómo ha evolucionado la ganadería en Cuba en el período comprendido entre los años 1985 y 2022. A través de un análisis de datos históricos y actuales buscamos comprender y visibilizar los desafíos que enfrenta actualmente el sector ganadero cubano como las limitaciones tecnológicas o la alimentación del propio ganado. De forma general, identificaremos las tendencias más relevantes y evaluaremos el impacto de diferentes variables sobre la producción ganadera. Mediante nuestro estudio queremos responder algunas interrogantes como ¿Qué ganado predomina en nuestro país?, ¿Qué tan bueno es el rendimiento de nuestro ganado? o ¿Cémo es la alimentación ganadera?, que su respuesta se evidenciará a través de graficos de líneas, histogramas u otros para mostrar la evolución de las principales variables a lo largo del tiempo.")



st.markdown('<p style="font-family: sans-serif;color:rgb(0,87,214);font-size: 35px;font-weight: bold;"><i>¿Qué podemos encontrar en nuestro DataProduct?</i></p>', unsafe_allow_html=True)
st.markdown('<p style=font-size: 18px;font-weight: bold;"><i>Al desplegar la barra lateral observamos que el contenido de la página se encuentra dividido en las secciones Ganado, Entidades y Acerca de, cada una contiene las siguientes subsecciones:</i></p>', unsafe_allow_html=True)

st.write('<p style="font-size: 20px;font-weight: bold;">🐾<i> Existencia: Esta sección está dividida en tres pestañas, Existencia del ganado, Entregas a sacrificio y Natalidad y Mortalidad. En la primera pestaña se analiza la distribución de las razas ganaderas, y su evolución a lo largo del tiempo. La pestaña no. 2 abarca todo lo relacionado con las entregas a sacrificio de los distintos sectores ganaderos y se realizan comparaciones entre los mismos. Por último, en la pestaña no. 3 analizamos el comportamiento de los nacimientos y muertes del ganado, así como la tasa de mortalidad. </i></p>', unsafe_allow_html=True)
st.write('<p style="font-size: 20px;font-weight: bold;">🛄<i> Producción: De igual forma que la sección anterior contiene tres pestañas, Producción de leche, Producción avícola, Alimentación del ganado. El contenido en Producción de leche, se basa en un estudio sobre la leche producida en Cuba según el tipo de ganado y el rendimiento del ganado de ordeño a lo largo de los años. En la segunda pestaña nos centramos específicamente en la producción avícola, ya sea carne o huevos y su rendimiento. Y en la pestaña no. 3 analizamos la alimentación del ganado en nuestro país y los valores de importación destinados al alimento.</i></p>', unsafe_allow_html=True)
st.write('<p style="font-size: 20px;font-weight: bold;">📍<i> Entidades: Mostramos, en esta sección un mapa de Cuba con las principales entidades del sector agropecuario. </i></p>', unsafe_allow_html=True)
st.write('<p style="font-size: 20px;font-weight: bold;">💲<i> Cuentas Nacionales: luiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiis </i></p>', unsafe_allow_html=True)