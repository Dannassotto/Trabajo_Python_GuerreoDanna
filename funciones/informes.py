import json

VENTAS_FILE = "data_ventas.json"
COMPRAS_FILE = "data_compras.json"

def cargar_datos(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def informe_ventas():
    ventas = cargar_datos(VENTAS_FILE)
    
    if not ventas:
        print("No hay datos de ventas disponibles.")
        return
    
    print("********** INFORME DE VENTAS **********")
    total_ingresos = 0
    for cliente, detalles in ventas.get("data_ventas", {}).items():
        print(f"Cliente: {detalles['nombreC']}")
        print(f"Dirección: {detalles['direccioC']}")
        print(f"Empleado: {detalles['nombreE']} - {detalles['cargoE']}")
        print("Productos vendidos:")
        for producto in detalles["productos"]:
            print(f"- {producto['nombre']}: {producto['cantidad']} unidades a ${producto['precio']} c/u")
            total_ingresos += producto['cantidad'] * producto['precio']
        print("-" * 40)
    print(f"Total de ingresos: ${total_ingresos}")
    print("****************************************")

def informe_stock():
    compras = cargar_datos(COMPRAS_FILE)
    
    if not compras:
        print("No hay datos de stock disponibles.")
        return
    
    print("********** INFORME DE STOCK **********")
    for producto, detalles in compras.get("data_compras", {}).items():
        print(f"Producto: {producto}")
        print(f"Cantidad en stock: {detalles['cantidaP']}")
        print(f"Precio de compra: ${detalles['precioC']}")
        print("-" * 40)
    print("****************************************")

if __name__ == "__main__":
    while True:
        print("\n1. Informe de Ventas")
        print("\n2. Informe de Stock")
        print("\n3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            informe_ventas()
        elif opcion == '2':
            informe_stock()
        elif opcion == '3':
            break
        else:
            print("Opción no válida.")
