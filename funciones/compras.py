
def compras(op=0):
    title = """
    *************
    * COMPRAS   *
    *************
    """
    print(title)
    
    try:
        fcompra = input('Fecha de la compra (dd-mm-yyyy): ')
        nombreP = input('Nombre del proveedor: ')
        nombreCo = input('Ingrese el contacto: ')
        nombrePR = input('Ingrese el nombre del producto: ')
        cantidaP = input('Ingrese la cantidad del producto: ')
        precioC = input('Ingrese el precio del producto: ')

        comprass = {
            'fcompra': fcompra,
            'nombreP': nombreP,
            'nombreCo': nombreCo,
            'nombrePR': nombrePR,
            'cantidaP': cantidaP,
            'precioC': precioC
        }
    except ValueError as e:
        print(f'Opción no válida: {e}')
        compras(op)