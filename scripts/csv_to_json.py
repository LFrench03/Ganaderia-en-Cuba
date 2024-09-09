import pandas as pd
import json
'''
Script que se utilizo para convertir los csv en una plantilla estructurada de diccionario (luego de limpiarlos) para luego desde esa estructura inicial ir reestructurando el 'inventraio_ganado.json'
'''
orient = ['dict','list','series','split','records','index']# Distintos tipos de orient para la generacion del diccionario 
def csv_to_json(ruta_csv, ruta_json):
    try:
        df = pd.read_csv(ruta_csv)

        titanic_json = df.to_dict(orient=orient[0])

        with open(ruta_json, 'w') as archivo_json:
            json.dump(titanic_json, archivo_json, indent=4)
        
        print("Archivo JSON creado exitosamente.")
    except Exception as e:
        print(f"Error al procesar el archivo CSV: {e}")

ruta_csv = "data/csv/5.4-pib-aprecios-constantes.csv"
ruta_json = 'scripts/result.json'
csv_to_json(ruta_csv,ruta_json)

