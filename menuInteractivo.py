import sqlite3

def crear_base_datos():
    conexion = sqlite3.connect('inventario.db')  # Crea o conecta a la base de datos
    cursor = conexion.cursor()

    # Crear la tabla productos si no existe
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT
    )
    ''')

    conexion.commit()
    conexion.close()
    print("Base de datos y tabla creadas con éxito.")

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar un producto")
    print("2. Mostrar todos los productos")
    print("3. Actualizar un producto")
    print("4. Eliminar un producto")
    print("5. Buscar un producto")
    print("6. Generar reporte de bajo stock")
    print("7. Salir")

def registrar_producto():
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    categoria = input("Categoría: ")

    cursor.execute('''
    INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
    VALUES (?, ?, ?, ?, ?)
    ''', (nombre, descripcion, cantidad, precio, categoria))

    conexion.commit()
    conexion.close()
    print("Producto registrado con éxito.")

def mostrar_productos():
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if productos:
        print("\n--- Lista de productos ---")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}")
    else:
        print("\nNo hay productos registrados en el inventario.")

    conexion.close()

def main():
    crear_base_datos()  # Asegura que la base de datos esté lista antes de iniciar el menú
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            mostrar_productos()
        elif opcion == '3':
            print("Funcionalidad de actualizar producto aquí.")
        elif opcion == '4':
            print("Funcionalidad de eliminar producto aquí.")
        elif opcion == '5':
            print("Funcionalidad de buscar producto aquí.")
        elif opcion == '6':
            print("Funcionalidad de generar reporte aquí.")
        elif opcion == '7':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
