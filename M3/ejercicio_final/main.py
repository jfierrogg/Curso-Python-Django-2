productos_disponibles = {1: {"nombre": "producto1", "categoria": "ropa", "precio": 3000}, 2: {"nombre": "producto2", "categoria": "tecnologia", "precio": 10000}, 3: {"nombre": "producto3", "categoria": "ropa", "precio": 5000}, 4: {"nombre": "producto4", "categoria": "hogar", "precio": 8000}, 5: {"nombre": "producto5", "categoria": "tecnologia", "precio": 22000}}

def ver_productos():
    for id, producto in productos_disponibles.items():
        print(f"ID: {id} Nombre: {producto["nombre"]}, Precio: {producto["precio"]}")

def buscar():
    opcion = int(input("Desea buscar por Nombre ingrese 1 o si desea bucarpor categoria ingrese 2: "))
    if opcion == 1:
        buscando = input("Ingrese el Nombre: ")
        for id, producto in productos_disponibles.items():
            if buscando != producto["nombre"]:
                continue
            elif buscando == producto["nombre"]:
                print(f"ID: {id} Nombre: {producto["nombre"]}, Precio: {producto["precio"]}")
                break
            else:
                print("Opcion incorrecta")
    elif opcion == 2:
        buscando = input("Ingrese el Categoria: ")
        for id, producto in productos_disponibles.items():
            if buscando != producto["categoria"]:
                continue
            elif buscando == producto["categoria"]:
                print(f"ID: {id} categoria: {producto["categoria"]}, Precio: {producto["precio"]}")
            else:
                print("Opcion incorrecta")
    else:
        print("Opcion incorrecta")

carrito = []
productos = []
precios = []

def agregar(producto):
    productos.append(producto["nombre"])
    precios.append(producto["precio"])
    #carrito.extend(productos, precios)

def ver_carrito_total():
    print(productos)
    """
    for producto, precio in zip(productos, precios):
        total = precio + precio
        print(carrito)
        print(f"{producto}: {precio} unidades, total = {total}")
    """

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
            ver_productos()
        elif opcion == 2:
            buscar()
        elif opcion == 3:
            ver_productos()
            producto_seleccionado = int(input("Ingresa el ID del producto seleccionado: "))
            agregar(productos_disponibles[producto_seleccionado])
        elif opcion == 4:
            ver_carrito_total()
        elif opcion == 5:
            pass
    elif opcion == 0:
        print("Gracias por visitar nuestro Ecommerce. ¡Hasta luego!")
        break
