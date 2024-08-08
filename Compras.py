def compras(op):
    title="""
    *************
    * COMPRAS   *
    *************
    """
    print(title)
try:
    fcompra= (input('fecha de la compra'))
    nombreP=(input('nombre proveedor'))
    nombreCo=(input('ingrese el contacto'))
    nombrePR=(input('ingrese el nombre del producto'))
    cantidaP=(input('ingrese la cantidad del producto'))
    precioC=(input('ingrese el precio del producto'))

    comprass={
    'fcompra':fcompra,
    'nombreP':nombreP,
    'nombreCo': nombreCo,
    'nombrePR' : nombrePR,
    'cantidaP' : cantidaP,
    'precioC' : precioC

    }
    
except ValueError:
    print('opción no valida')


