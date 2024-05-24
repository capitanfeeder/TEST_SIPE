import mysql.connector
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv("cred.env")

# Establecer la conexión con la base de datos
def get_connection():
    conexion = mysql.connector.connect(
        host=os.getenv("HOST"),
        port=3306,
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE")
)
    return conexion
