import json
def generate_json(path):
    try:
        with open (path, encoding="utf8") as json_data:
            data = json.load(json_data)
        year = 1985
        data["events"] = []
        for _ in range(38):
            data["events"].append({"text":{"headline": f"Anno {year}.", "text":f"<p>Esto ocurrio en el anno {year}.</p"},"start_date": {"year": year}})
            year +=1
        with open(path, 'w') as archivo_json:
            json.dump(data, archivo_json, indent=4)
            print("a")

    except Exception as e:
        print(f"Error al procesar el archivo Json: {e}")
path = "historia.json"
generate_json(path)