productos_disponibles = {1: {"nombre": "producto1", "categoria": "ropa", "precio": 3000}, 2: {"nombre": "producto2", "categoria": "tecnologia", "precio": 10000}, 3: {"nombre": "producto3", "categoria": "ropa", "precio": 5000}, 4: {"nombre": "producto4", "categoria": "hogar", "precio": 8000}, 5: {"nombre": "producto5", "categoria": "tecnologia", "precio": 22000}}

while True:
    print("""Bienvenido/a a tu Ecommerce
            1) Ver catálogo de productos
            2) Buscar producto por nombre o categoría
            3) Agregar producto al carrito
            4) Ver carrito y total
            5) Vaciar carrito
            0) Salir""")

    opcion = int(input("Seleccione una opción: "))

    if opcion > 0 and opcion < 6:
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
    elif opcion == 0:
        print("Gracias por visitar nuestro Ecommerce. ¡Hasta luego!")
        break
