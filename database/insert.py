import mysql.connector

# Conexión a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sergio1997",
    database="limasoftbd"
)

cursor = conexion.cursor()

# Insertar registros en la tabla
insertar_datos_query = """
INSERT INTO empleados (nombre, edad, ciudad, salario)
VALUES (%s, %s, %s, %s)
"""

empleados = [
    ("Juan Perez", 35, "Lima", 2500.50),
    ("Maria Lopez", 28, "Arequipa", 3000.00),
    ("Carlos Sanchez", 40, "Trujillo", 3500.75),
    ("Ana Martinez", 30, "Chiclayo", 2800.00),
    ("Luis Fernandez", 50, "Cusco", 4500.25)
]

cursor.executemany(insertar_datos_query, empleados)
conexion.commit()

print(f"Se insertaron {cursor.rowcount} registros.")
