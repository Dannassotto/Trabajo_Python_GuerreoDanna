import json
import os

MY_VENTAS = "data_ventas.json"

def NewFile(data):
    with open(MY_VENTAS, "w") as wf:
        json.dump(data, wf, indent=4)

def updateFile(data):
    with open(MY_VENTAS, 'w') as fw:
        json.dump(data, fw, indent=4)

def AddData(category, key, data):
    if os.path.isfile(MY_VENTAS):
        with open(MY_VENTAS, "r+") as file:
            file_data = json.load(file)
            if category in file_data:
                file_data[category][key] = data
            else:
                file_data[category] = {key: data}
            file.seek(0)
            json.dump(file_data, file, indent=4)
    else:
        file_data = {category: {key: data}}
        NewFile(file_data)

def ReadFile():
    if os.path.isfile(MY_VENTAS):
        with open(MY_VENTAS, "r") as file:
            return json.load(file)
    else:
        return {}
