import modules.ventass as mv
import funciones.globales as fg

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
        
        mv.AddData('data_ventas', nombreC, ventass)
        
        if 'data_ventas' not in fg.ventan:
            fg.ventan['data_ventas'] = {}
        fg.ventan['data_ventas'][nombreC] = ventass
        
        if input("¿Desea registrar otra venta? S(si) o Enter(no): ").strip().lower() == 's':
            ventas()
    
    except ValueError as e:
        print(f'Opción no válida: {e}')
        ventas(op)

if __name__ == "__main__":
    ventas()
