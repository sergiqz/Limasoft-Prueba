# Limasoft-Prueba
Este proyecto es una aplicación web desarrollada con Flask que permite mostrar gráficos y una tabla de datos sobre empleados extraídos de una base de datos MySQL. Los gráficos visualizan la relación entre la edad y el salario de los empleados, así como la distribución de empleados por ciudad.

<div style="display: flex; justify-content: space-around; align-items: flex-start;">
    <img src="images/edad_vs_salario.png" alt="Gráfico de Empleados" width="500" height="300" />
    <img src="images/personas_por_ciudad.png" alt="Personas por ciudad" width="500" height="300" />
</div>

# Requisitos Previos
Antes de comenzar, asegúrate de tener instalado lo siguiente:
- Python 3.x
- pip (gestor de paquetes de Python)
- MySQL (para la base de datos)
- Flask
- SQLAlchemy
- MySQL Connector para SQLAlchemy
- Pandas
- Matplotlib

# Instalación
## Clonar el repositorio:
https://github.com/sergiqz/Limasoft-Prueba.git

## Instalar las dependencias:
pip install -r requirements.txt

## Configurar la base de datos MySQL:
ejecutar el archivo
- flask\database\data_base.py
- flask\database\insert.py

## Modificar las credenciales de la base de datos en el archivo de configuración (utils.py):
- engine = create_engine('mysql+mysqlconnector://usuario:password@localhost/limasoftbd')

## Correr la aplicación:
Después de configurar todo, puedes correr la aplicación con el siguiente comando:
- python app.py

## Acceder a la aplicación:
Abre tu navegador y ve a la dirección 
http://127.0.0.1:5000/.
