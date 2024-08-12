def ventas(op=0):
    title = """
    *****************
    *     VENTAS    *
    *****************
    """
    print(title)
    
    try:
        fventa = input('Ingrese fecha de la venta (dd-mm-yyyy): ')
        nombreC = input('Ingrese el nombre del cliente: ')
        direccioC = input('Ingrese la dirección del cliente: ')
        nombreE = input('Ingrese el nombre del empleado: ')
        cargoE = input('Ingrese el cargo del empleado: ')
        
        ventass = {
            'fventa': fventa,
            'nombreC': nombreC,
            'direccioC': direccioC,
            'nombreE': nombreE,
            'cargoE': cargoE
        }
    except ValueError as e:
        print(f'Opción no válida: {e}')
        ventas(op)
