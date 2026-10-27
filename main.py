# datos de la tienda
codigos = []
nombres = []
precios = []
cantidades = []

# datos de acceso
USUARIO = "yo"
CLAVE = "101"

intentos = 0
acceso = False
while intentos < 3 and not acceso:
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")
    if usuario == USUARIO and clave == CLAVE:
        acceso = True
        print("Bienvenido a la tienda.")
    else:
        intentos = intentos + 1
        print("Datos incorrectos. Intentos restantes:", 3 - intentos)

# Menú
if acceso:
    opcion = ""
    while opcion != "6":
        print()
        print("TIENDA")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Ver cálculos")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        # Opción 1: Agregar producto
        if opcion == "1":
            print("Agregar productos")
            codigo = input("Código: ").strip().upper()
            if codigo == "":
                print("El código no puede estar vacío.")
            elif codigo in codigos:
                print("Ya existe un producto con este código.")
            else:
                nombre = input("Nombre: ").strip()
                precio_texto = input("Precio (Q): ").strip()
                cantidad_texto = input("Cantidad: ").strip()

                if nombre == "":
                    print("El nombre no puede estar vacío.")
                elif not precio_texto.replace(".", "", 1).isdigit():
                    print("El precio debe ser un número, por ejemplo 25.50.")
                elif not cantidad_texto.isdigit():
                    print("La cantidad debe ser un número entero.")
                else:
                    codigos.append(codigo)
                    nombres.append(nombre)
                    precios.append(float(precio_texto))
                    cantidades.append(int(cantidad_texto))
                    print("Producto agregado correctamente")
        # Opción 2: Listar productos 
        elif opcion == "2":
            print("\n" + "=" * 65)
            print("                 LISTA DE PRODUCTOS")
            print("=" * 65)

            if len(codigos) == 0:
                print("No hay productos registrados.")
            else:
                print(
                    f"{'CODIGO':<10}"
                    f"{'NOMBRE':<20}"
                    f"{'PRECIO':>15}"
                    f"{'CANTIDAD':>15}"
                )

                print("-" * 65)

                for i in range(len(codigos)):
                    print(
                        f"{codigos[i]:<10}"
                        f"{nombres[i]:<20}"
                        f"{('Q ' + format(precios[i], ',.2f')):>15}"
                        f"{cantidades[i]:>15}"
                    )

                print("-" * 65)
                print(f"Total de productos: {len(codigos)}")

            print("=" * 65)
        #  Opción 3: Buscar producto
        elif opcion == "3":
            print("Buscar producto")
            buscado = input("Código o nombre del producto: ").strip()
            if buscado == "":
                print("Debes escribir algo para buscar.")
            else:
                encontrado = False
                for i in range(len(codigos)):
                    if codigos[i] == buscado.upper() or buscado.lower() in nombres[i].lower():
                        print(codigos[i], "|", nombres[i], "| Q", precios[i], "| Cant:", cantidades[i])
                        encontrado = True
                if not encontrado:
                    print("No se encontró ningún producto con ese dato.")
        # Opción 4: Eliminar producto
        elif opcion == "4":
            print("Eliminar producto")
            codigo = input("Código del producto que quieres eliminar: ").strip().upper()
            if codigo in codigos:
                posicion = codigos.index(codigo)
                print("Se eliminará:", nombres[posicion])
                confirmar = input("¿Seguro? (s/n): ").strip().lower()
                if confirmar == "s":
                    codigos.pop(posicion)
                    nombres.pop(posicion)
                    precios.pop(posicion)
                    cantidades.pop(posicion)
                    print("Producto eliminado.")
                else:
                    print("Eliminación cancelada.")
            else:
                print("No existe un producto con ese código.")
        # Opción 5: Cálculos del inventario
        elif opcion == "5":
            print("\n" + "=" * 40)
            print("       CALCULOS DEL INVENTARIO")
            print("=" * 40)

            if len(codigos) == 0:
                print("\nNo hay productos registrados.")

            else:
                total_inventario = 0
                total_unidades = 0
                suma_precios = 0
                pos_caro = 0
                pos_barato = 0

                for i in range(len(codigos)):
                    total_inventario += precios[i] * cantidades[i]
                    total_unidades += cantidades[i]
                    suma_precios += precios[i]

                    if precios[i] > precios[pos_caro]:
                        pos_caro = i

                    if precios[i] < precios[pos_barato]:
                        pos_barato = i

                promedio = suma_precios / len(codigos)

                print("\n--- 1. RESUMEN GENERAL ---")
                print(f"Cantidad de productos: {len(codigos)}")
                print(f"Total de unidades: {total_unidades}")

                print("\n--- 2. VALORES DEL INVENTARIO ---")
                print(f"Valor total: Q {total_inventario:,.2f}")
                print(f"Precio promedio: Q {promedio:,.2f}")

                print("\n--- 3. COMPARACION DE PRECIOS ---")
                print(
                    f"Producto mas caro: {nombres[pos_caro]}"
                    f" - Q {precios[pos_caro]:,.2f}"
                )
                print(
                    f"Producto mas barato: {nombres[pos_barato]}"
                    f" - Q {precios[pos_barato]:,.2f}"
                )

            print("\n" + "=" * 40)
        # Opción 6: Salir
        elif opcion == "6":
            print("Hasta luego")
        else:
            print("Opción no válida. Escribe un número del 1 al 6.")
else:
    print("Demasiados intentos fallidos. El programa se cerrará.")
    print("vuelve a internar")
