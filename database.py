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

