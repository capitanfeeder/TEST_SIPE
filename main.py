from fastapi import FastAPI
from openai import OpenAI
import mysql.connector
from ia_sipe import generate_query, execute_query, transform_response
from config_cnx import get_connection
from db_schema import sql10708993
from registro_query import guardar_consulta_correcta, guardar_consulta_error

app = FastAPI()

# Ruta raíz
@app.get("/")
async def root():
    return {"message": "Implementacion de IA en SIPE"}

@app.post("/sipe")
async def sql_query(question: str):
    """
    Este endpoint recibe una pregunta o un pedido, lo convierte a consulta SQL y 
    devuelve el resultado de la misma.

    Parámetros de entrada:
    - question: str - Una pregunta con temática de RR.HH.

    Respuesta:
    - Un diccionario con el resultado de la consulta SQL.
    """
    print("Bienvenido al endpoint /sipe")
    
    sql_query = generate_query(question, sql10708993)
    execute = execute_query(sql_query)

    if "error" in execute:
        guardar_consulta_error(question, sql_query, execute)
        return {"result": execute}
    else:
        guardar_consulta_correcta(question, sql_query, execute)
        result = transform_response(question, execute)
        return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)