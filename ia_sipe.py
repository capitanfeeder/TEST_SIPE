from openai import OpenAI
import mysql.connector
import pandas as pd
import json
import os
import re
from dotenv import load_dotenv
from db_schema import sql10708993
from config_cnx import get_connection

load_dotenv("cred.env")

# Conexion a openai
client = OpenAI(api_key=os.environ.get("api_key"))

# Función para obtener consultas predefinidas desde el archivo Excel
def get_predefined_queries_from_excel():
    archivo = "registro/consultas_correctas.xlsx"
    if not os.path.isfile(archivo):
        return {}

    df = pd.read_excel(archivo)
    predefined_queries = {}
    for index, row in df.iterrows():
        predefined_queries[row['Pregunta'].lower()] = row['Consulta']

    return predefined_queries

# Funcion para generar la consulta SQL
def generate_query(question, sql10708993):
    # Obtener las consultas predefinidas desde el archivo Excel
    predefined_queries = get_predefined_queries_from_excel()

    # Verificar si la pregunta coincide con alguna de las consultas predefinidas
    for predefined_question, predefined_query in predefined_queries.items():
        if predefined_question in question.lower():
            return predefined_query.strip()

    # Si no hay coincidencias, generar la consulta con OpenAI
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"""
                    Use the following database schema to generate an SQL query that answers the question:
                    {json.dumps(sql10708993)}.
                    The question is: {question}. You must return ONLY the SQL query without any other text.
                    Otherwise, I will not be able to interpret the response. Additionally, if you receive ambiguous requests
                    such as: 'Show me the seniority' or 'Show me the juniors', you should understand that the request is for
                    an SQL query that returns the relevant records. When seniority or hierarchy is mentioned, it refers to
                    Trainee, Junior, Semisenior, and Senior levels. If I ask for a list of employees, the query must include
                    last_name and name, as well as any other information I request about them. Answer only those questions
                    related to the SIPE database. Keep in mind that the database structure in dictionary format with key-value
                    pairs is in sql10708993. You have the tables with their respective columns.
                """
            }
        ],
        model="gpt-4",
    )

    return chat_completion.choices[0].message.content.strip()

# Funcion para ejecutar la consulta SQL
def execute_query(sql_query):
    forbidden_words = ["DELETE", "DROP", "ALTER", "TRUNCATE", "INSERT", "UPDATE", "CREATE", "RENAME", "REVOKE", "GRANT"]
    for word in forbidden_words:
        if re.search(word, sql_query, re.IGNORECASE):
            return json.dumps({"error": "Disculpa, no tengo permisos para hacer eso."})

    conexion = get_connection()
    cursor = conexion.cursor()

    try:
        cursor.execute(sql_query)
        result = cursor.fetchall()

        # Convertir los objetos datetime.date a cadenas de texto
        result_list = [list(map(str, row)) for row in result]

        # Serializar la lista de diccionarios en formato JSON
        result_json = json.dumps(result_list, indent=4)

        return result_json

    except mysql.connector.Error as error:
        print(f"Error al ejecutar la consulta: {error}")
        return json.dumps({"error": str(error)})

# Funcion para crear una respuesta a la pregunta
def transform_response(question, result_json):
    # Parsear el objeto JSON
    result_dict = json.loads(result_json)

    # Verificar si el objeto JSON contiene un mensaje de error
    if "error" in result_dict:
        # Construir el mensaje de respuesta a partir del mensaje de error
        response = f"{result_dict['error']}"
    else:
        # Construir el prompt para la IA
        prompt = f"""Use the following information to provide a user-friendly response in spanish to the question:
                    '{question}'. {result_dict} in JSON format."""

        # Llama a la IA para que genere la respuesta
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": prompt}
            ],
            model="gpt-3.5-turbo",
        )

        # Extraer la respuesta generada por la IA
        response = chat_completion.choices[0].message.content.strip()

    return response
