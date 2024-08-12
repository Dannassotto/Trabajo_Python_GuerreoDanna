import funciones.ventas as fv
import funciones.compras as fc
import funciones.informes as fi
import funciones.globales as fg

def menu_principal():
    while True:
        fg.borrar_pantalla()
        print("*****************")
        print("*   MENÚ PRINCIPAL   *")
        print("*****************")
        print("1. Registrar Ventas")
        print("2. Registrar Compras")
        print("3. Generar Informe de Ventas")
        print("4. Generar Informe de Stock")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            fv.ventas()
        elif opcion == "2":
            fc.compras()
        elif opcion == "3":
            fi.informe_ventas()
            fg.pausar_pantalla()
        elif opcion == "4":
            fi.informe_stock()
            fg.pausar_pantalla()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            fg.pausar_pantalla()

if __name__ == "__main__":
    menu_principal()
