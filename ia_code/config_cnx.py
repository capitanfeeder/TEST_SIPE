import mysql.connector
import os
from mysql.connector import MySQLConnection
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'crede.env')
load_dotenv(dotenv_path=dotenv_path)

# Establecer la conexión con la base de datos
def get_connection() -> MySQLConnection:
    """
    Establece y devuelve una conexión a la base de datos MySQL.

    Returns:
        MySQLConnection: Conexión a la base de datos MySQL.
    """
    conexion = mysql.connector.connect(
        host=os.getenv("HOST"),
        port=19318,
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE")
)
    return conexion
