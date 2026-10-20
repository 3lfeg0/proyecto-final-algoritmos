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
# Menuu
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
            print("Agregar producto (pendiente)")
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