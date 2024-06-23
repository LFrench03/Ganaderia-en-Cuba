import pandas as pd
import json
orient = ['dict','list','series','split','records','index']#Distintos tipos de orient para la generacion del diccionario 
def csv_to_json(ruta_csv, ruta_json):
    try:
        # Leer el archivo CSV en un DataFrame
        df = pd.read_csv(ruta_csv)

        # Generando el diccionario a partir del DataFrame completo
        titanic_json = df.to_dict(orient=orient[4])

        # Guardando en archivo Json
        with open(ruta_json, 'w') as archivo_json:
            json.dump(titanic_json, archivo_json, indent=4)
        
        print("Archivo JSON creado exitosamente.")
    except Exception as e:
        print(f"Error al procesar el archivo CSV: {e}")
#Prueba:
ruta_csv = "data/csv/ovino_caprino/produccion-de-leche-y-entrega-a-sacrificio-de-ganado-ovino-caprino.csv"
ruta_json = 'result.json'
csv_to_json(ruta_csv,ruta_json)

