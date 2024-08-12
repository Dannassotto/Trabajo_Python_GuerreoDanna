import json
import os

MY_VENTAS= "data_ventas"

def AddData(*param):
    data= list(param)
    with open(MY_VENTAS, "r+") as omu:
        file_data=json.load(omu)
        if(len(param)>1):
            file_data[data[0]].update({data[1]:data[2]})
        else:
            file_data.update({param[0]})
            omu.seek(0)
            json.dump(file_data,omu,indent=4)

