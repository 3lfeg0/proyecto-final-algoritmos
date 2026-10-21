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
        print("===== TIENDA =====")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Ver cálculos")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("--- Agregar producto ---")
            codigo = input("Código: ").strip()
            if codigo == "":
                print("El código no puede estar vacío.")
            elif codigo in codigos:
                print("Ya existe un producto con ese código.")
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
            print("Listar productos (pendiente)")
        elif opcion == "3":
            print("Buscar producto (pendiente)")
        elif opcion == "4":
            print("Eliminar producto (pendiente)")
        elif opcion == "5":
            print("Ver cálculos (pendiente)")
        elif opcion == "6":
            print("Hasta luego.")
        else:
            print("Opción no válida. Escribe un número del 1 al 6.")
else:
    print("Demasiados intentos fallidos. El programa se cerrará.")