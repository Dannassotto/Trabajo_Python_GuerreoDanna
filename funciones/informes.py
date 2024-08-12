import json
import os

MY_VENTAS = "data_ventas.json"
MY_COMPRAS = "data_compras.json"

def informe_ventas():
    if not os.path.isfile(MY_VENTAS):
        print("No hay datos de ventas disponibles.")
        return

    with open(MY_VENTAS, "r") as file:
        ventas = json.load(file)
    
    print("Informe de Ventas:")
    for cliente, detalles in ventas.get('data_ventas', {}).items():
        print(f"\nCliente: {cliente}")
        print(f"Fecha: {detalles['fventa']}")
        print(f"Dirección: {detalles['direccioC']}")
        print(f"Empleado: {detalles['nombreE']} ({detalles['cargoE']})")

def informe_stock():
    if not os.path.isfile(MY_COMPRAS):
        print("No hay datos de compras disponibles.")
        return

    with open(MY_COMPRAS, "r") as file:
        compras = json.load(file)
    
    print("Informe de Stock:")
    for producto, detalles in compras.get('data_compras', {}).items():
        print(f"\nProducto: {producto}")
        print(f"Fecha: {detalles['fcompra']}")
        print(f"Proveedor: {detalles['nombreP']}")
        print(f"Contacto: {detalles['nombreCo']}")
        print(f"Cantidad: {detalles['cantidaP']}")
        print(f"Precio: {detalles['precioC']}")
