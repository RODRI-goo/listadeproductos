import os

# Lista global para almacenar los productos
productos = []

#  para cargar los datos desde el archivo con el nombre productos.txt
def cargar_datos():
    if os.path.exists('productos.txt'):
        with open('productos.txt', 'r') as file:
            for linea in file:
                nombre, precio, cantidad = linea.strip().split(',')
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })
    else:
        print("No se encontró el archivo de datos, iniciando con un inventario vacío.")

# para guardar los datos en el archivo
def guardar_datos():
    with open('productos.txt', 'w') as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados con éxito.")

# para añadir un producto
def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un valor numérico válido para el precio.")
    
    while True:
        try:
            cantidad = int(input("Introduce la cantidad del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un valor numérico válido para la cantidad.")

    productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
    print(f"Producto '{nombre}' añadido con éxito.")

# Función para ver todos los productos
def ver_productos():
    if productos:
        print("\nLista de productos:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos en el inventario.")

# Función para actualizar un prodycto existente
def actualizar_producto():
    nombre = input("Introduce el nombre del producto que quieres actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            print(f"Producto encontrado: {producto}")
            nuevo_nombre = input("Introduce el nuevo nombre (deja en blanco para no cambiar): ")
            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre
            
            while True:
                nuevo_precio = input("Introduce el nuevo precio (deja en blanco para no cambiar): ")
                if not nuevo_precio:
                    break
                try:
                    producto['precio'] = float(nuevo_precio)
                    break
                except ValueError:
                    print("Por favor, introduce un valor numérico válido para el precio.")

            while True:
                nueva_cantidad = input("Introduce la nueva cantidad (deja en blanco para no cambiar): ")
                if not nueva_cantidad:
                    break
                try:
                    producto['cantidad'] = int(nueva_cantidad)
                    break
                except ValueError:
                    print("Por favor, introduce un valor numérico válido para la cantidad.")

            print(f"Producto '{nombre}' actualizado con éxito.")
            return
    print(f"Producto '{nombre}' no encontrado.")

#  para eliminar un producto existente
def eliminar_producto():
    nombre = input("Introduce el nombre del producto que quieres eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado con éxito.")
            return
    print(f"Producto '{nombre}' no encontrado.")

# Función para mostrar el meno prinipal
def menu():
    cargar_datos()
    
    while True:
        print("\nGestión de Inventario")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            print("Saliendo del sistema.")
            break
        else:
            print("Por favor, selecciona una opción válida.")


menu()
