import pandas as pd
import json
orient = ['dict','list','series','split','records','index']# Distintos tipos de orient para la generacion del diccionario 
def csv_to_json(ruta_csv, ruta_json):
    try:
        df = pd.read_csv(ruta_csv)

        titanic_json = df.to_dict(orient=orient[4])

        with open(ruta_json, 'w') as archivo_json:
            json.dump(titanic_json, archivo_json, indent=4)
        
        print("Archivo JSON creado exitosamente.")
    except Exception as e:
        print(f"Error al procesar el archivo CSV: {e}")

ruta_csv = ""
ruta_json = 'result.json'
csv_to_json(ruta_csv,ruta_json)

