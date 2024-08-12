from os import system
import sys

def borrar_pantalla():
    if sys.platform in ["linux", "darwin"]:
        system("clear")
        
    else:
        system("cls")

def pausar_pantalla():
    if sys.platform in ["linux", "darwin"]:
        input("Presione enter para continuar ")
    else:
        system("pause")

compran = {
    "data_compras": {}
}