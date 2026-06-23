from os import system

while True:
    try:
        system("pause")
        system("cls")

        print(""" 
 ========== CONTROL DE INVENTARIO AUTOMOTRIZ ==========
1. Ingresar Nuevo Vehículo
2. Verificar Existencia de Patente
3. Actualizar Datos de un Vehículo (Precio y Año)
4. Aplicar Descuento Masivo por Año
5. Exportar Inventario Filtrado por Tipo
6. Listar Catálogo Completo con IVA Incluido
7. Finalizar programa
========================================================""")
        opcion = int(input("Seleccione : "))
        match opcion:
            case 1: 
                patente = int(input("Selecione : ")).upper().strip()
                tipo = input("Ingrese tipo : ").capitalize()
                anio = int(input("INGRESE AÑO (2015 - 2026) : "))
                precio = int(input("Ingrese precio $: "))

            case 2: pass
            case 3: pass
            case 4: pass
            case 5: pass
            case 6: pass
            case 7: pass
            case _: print("No validó")
    except Exception as e:
        print(f"Error {e}")