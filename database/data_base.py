import mysql.connector

# Conexión a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sergio1997",
    database="limasoftbd"
)

cursor = conexion.cursor()

# Crear la tabla
crear_tabla_query = """
CREATE TABLE IF NOT EXISTS empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    ciudad VARCHAR(100),
    salario DECIMAL(10, 2)
)
"""
cursor.execute(crear_tabla_query)
conexion.commit()

print("Tabla creada exitosamente.")
