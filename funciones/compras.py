import modules.comprass as mv
import funciones.globalesC as fC

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
        
        mv.AddData('data_compras', nombrePR, comprass)
        
        if 'data_compras' not in fC.compran:
            fC.compran['data_compras'] = {}
        fC.compran['data_compras'][nombrePR] = comprass
        
        if input("¿Desea registrar otra compra? S(si) o Enter(no): ").strip().lower() == 's':
            compras()
    
    except ValueError as e:
        print(f'Opción no válida: {e}')
        compras(op)

if __name__ == "__main__":
    compras()
