import streamlit as st

st.write("Metodologia")
st.markdown('''\n
### *Formato de modificacion de dataframe por seleccion*\n
# Seccion de existencia(Pagina con tabulaciones)\n
Tab1-Existencia\n
\tQue tipo de ganado ha predominado y que tipo ha sido la minoria? 
    Comparacion entre la existencia de todos los tipos de ganado con un grafico de linea como serie de tiempo
    (Contenedor 1.1)
            -Desplegable para seleccionar el tipo de analisis: Total, Estatal, No Estatal o All in(Parte superior)
            -Se utiliza la existencia promedio del ganado vacuno para los valores Estatales y No Estatales
        Nota: Para el analisis se tendrian las evaluaciones en una misma escala para evaluar las comparaciones
    Ademas(formato columnas(3)):
    (Contenedor 1.2) 
    Formato de slide para pasar los años y, en ese formato
        -para los diferentes tipos de ganado vacuno una comparacion con bar chart con dos barras(Machos y Hembras)
        -para el ganado ovino caprino un grafico de pastel para comparar la existencia ovina con la caprina
        -para las aves un grafico de area comparando la existencia de aves en empresas estatales
    (Expansor 1) 
    Observaciones, datos y metodologia del analisis de la pagina
Tab2-Entregas a Sacrificios\n
\tQue tipo de ganado tiene mas densidad de entregas a sacrificios? 
    (Contenedor 2.1)
        Mismo formato del contenedor 1.1 con los sacrificios(exceptuando las aves)
    (Contenedor 2.2)
        Scatter plot para peso en pie y peso promedio de los 3 tipos de ganado productores con un slide en la parte su para pasar los años(se incluyen los pollos de ceba)
    (Contenedor 2.3)     
        Comparacion con grafico de pastel de las entregas estatales de sacrificio estatales de ganado porcino(De ceba y la diferencia de esta con el total)
    Y para finalizar(formato columnas(2)):
    (Contenedor 2.4)
        Seccion para los pollos de ceba con:
            -un grafico de area para ver el total de sacrificios de pollos de ceba como linea de tiempo
            -grafico de linea como serie de tiempo para el pienso consumido por ave y para la conversion de pienso en carne
    (Expansor 2) 
    Observaciones, datos y metodologia del analisis de la pagina
Tab3-Natalidad y Mortalidad(Vacuno & Porcino)\n
    (Contenedor 3.1)
    Calcular tasa de existencia y se representa en un grafico de area para compararlo como serie de tiempo         
    (Contenedor 3.2)
    Grafico de linea para nacimientos y muertes como serie de tiempo
\n
# Seccion de rendimiento(Pagina con tabulaciones)\n
    (Contenedor 1.1)Columnas(2)
        -Se especifica que la leche de ovino carprino es litros, la de vaca miles de litros y los huevos en miles de millones de unidades 
        y se compara con un histograma y el slide debajo para pasar los años
        -Lo mismo con la existencia
    (Contenedor 1.2)
        Lo mismo con el rendimiento en kg de leche para cada vaca y huevos por gallina ponedora en unidades
    (Contenedor 1.3)
        Grafico de pastel para comparar de las entregas de sacrifico del ganado porcino cuales son de ceba y cuales no. Con un slide para los años y un desplegable
        para seleccionar si se evaluara en el Total, Estatal o no Estatal
\n
Notas de Analisis Exploratorio:\n
        Arreglar en el Json los valores totales que estan vacios y que tienen en los mismos años valores en estatal. Si esta en estatal tiene que estar en total tambien.
        Poner en el Json las unidades de medida que no esten puestas
''')