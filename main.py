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
        print("Bienvenido al sistema.")
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
        elif opcion == "2":
            print("Lista de productos")
            if len(codigos) == 0:
                print("No hay productos registrados.")
            else:
                for i in range(len(codigos)):
                    print(codigos[i], "|", nombres[i], "| Q", precios[i], "| Cant:", cantidades[i])
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
        elif opcion == "5":
            print("Ver cálculos (pendiente)")
        elif opcion == "6":
            print("Hasta luego.")
        else:
            print("Opción no válida. Escribe un número del 1 al 6.")
else:
    print("Demasiados intentos fallidos. El programa se cerrará.")