import json 
'''
Script para agregar los valores que se mostrarian en el tooltip del mapa al 'data/geojsons/cuba.geojson'
'''
with open("data/geojsons/cuba.geojson") as json_file:
    data = json.load(json_file)
with open("inventario_ganado.json") as json_file2:
    data2 = json.load(json_file2)

lista_prov = ["La Habana","Matanzas","Cienfuegos","Sancti Spiritus","Las Tunas","Holguin","Granma","Santiago de Cuba","Isla de la Juventud"
              ,"Camaguey","Ciego de Avila","Villa Clara","Guantanamo","Pinar del Rio","Artemisa","Mayabeque"] #Provincias en el orden que aparece en la estructura del GeoJson


tierras=data2["Instituciones"]["Tenientes de tierras"]  #Luego "Por Provincias"
index = 0
for i, j  in list(zip([x for x in range(16)], lista_prov)):
    for year in tierras:
        values = data2["Instituciones"]["Tenientes de tierras"][year][j]  #Luego "Por Provincias"
        for key in values:
            if key == "Cooperativas" and (isinstance(values[key], dict)):
                for k in values[key]:
                    data["features"][i]["properties"]["Tierras"+year+k] = values[key][k]   #Luego "Entidades"
            else:
                data["features"][i]["properties"]["Tierras"+year+key] = values[key]   #Luego "Entidades"


try:
    with open("data/geojsons/cuba.geojson", 'w') as archivo_json:
        json.dump(data, archivo_json, indent=4)
        print("GeoJson Actualizado de forma exitosa")
except Exception as e:
    print(f"Error al procesar el GeoJson: {e}")