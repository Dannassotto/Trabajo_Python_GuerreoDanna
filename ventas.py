def ventas(op):
    title="""
    *****************
    *     VENTAS    *
    *****************
    """
    print(title)
try:
    fventa=(input('ingrese fecha de la venta:'))
    nombreC=(input('ingrese el nombre del cliente:'))
    direccioC=(input('ingrese la dirección del cliente:'))
    nombreE= (('nombre del empleado:'))
    cargoE=(input('cargo del empleado:'))
    
    ventass={
        'fventa': fventa,
        'nombreC' : nombreC,
        'direccioC': direccioC,
        'nombreE':nombreE,
        'cargoE' : cargoE
    }
except ValueError:
    print("opcion invalida")
    ventas(0)