import os
import re
import json
import pandas as pd
import numpy as np
import mysql.connector
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
from ia_code.db_schema import defaultdb
from ia_code.config_cnx import get_connection
from openai import OpenAI

nltk.download('punkt')
nltk.download('stopwords')

# Cargar las variables de entorno desde el archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'crede.env')
load_dotenv(dotenv_path=dotenv_path)

# Conexion a openai
client = OpenAI(api_key=os.environ.get("api_key"))


# Función para obtener consultas predefinidas desde el archivo Excel
def get_predefined_queries_from_excel() -> dict:
    """
    Obtiene consultas predefinidas desde un archivo Excel.

    Returns:
        dict: Un diccionario donde las claves son preguntas y los valores son consultas SQL predefinidas.
    """
    archivo = os.path.join(os.path.dirname(__file__), '..', 'registro', 'consultas_correctas.xlsx')
    if not os.path.isfile(archivo):
        return {}

    df = pd.read_excel(archivo)
    predefined_queries = {row['Pregunta'].lower(): row['Consulta'] for _, row in df.iterrows()}
    return predefined_queries


# Función para preprocesar el texto
def preprocess_text(text: str) -> str:
    """
    Preprocesa el texto eliminando palabras muy cortas y puntuación.

    Args:
        text (str): El texto a preprocesar.

    Returns:
        str: El texto preprocesado.
    """
    text = text.lower()
    text = re.sub(r'\b\w{1,2}\b', '', text)  # Eliminar palabras muy cortas
    text = re.sub(r'[^\w\s]', '', text)  # Eliminar puntuación
    return text


# Función para encontrar la pregunta más similar
def find_most_similar_question(user_question: str, predefined_questions: dict) -> tuple:
    """
    Encuentra la pregunta más similar a la pregunta del usuario.

    Args:
        user_question (str): La pregunta del usuario.
        predefined_questions (dict): Un diccionario de preguntas predefinidas.

    Returns:
        tuple: La pregunta más similar y el valor de similitud.
    """
    if not predefined_questions:
        return "", 0

    preprocessed_questions = [preprocess_text(q) for q in predefined_questions.keys()]
    user_question_processed = preprocess_text(user_question)

    vectorizer = TfidfVectorizer().fit_transform(preprocessed_questions + [user_question_processed])
    vectors = vectorizer.toarray()

    cosine_similarities = cosine_similarity(vectors[-1].reshape(1, -1), vectors[:-1])
    most_similar_idx = np.argmax(cosine_similarities)

    return list(predefined_questions.keys())[most_similar_idx], cosine_similarities[0, most_similar_idx]


# Función para generar la consulta SQL
def generate_query(question: str, defaultdb: dict) -> str:
    """
    Genera una consulta SQL basada en una pregunta.

    Args:
        question (str): La pregunta del usuario.
        defaultdb (dict): El esquema de la base de datos SIPE.

    Returns:
        str: La consulta SQL generada.
    """
    predefined_queries = get_predefined_queries_from_excel()

    # Encuentra la pregunta más similar
    most_similar_question, similarity = find_most_similar_question(question, predefined_queries)

    # Si no hay preguntas predefinidas o la similitud es baja, generar la consulta con OpenAI
    if not most_similar_question or similarity < 0.95:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"""
                        Use the following database schema to generate an SQL query that answers the question:
                        {json.dumps(defaultdb)}.
                        The question is: {question}.

                        Important Instructions:
                        - ALWAYS return ONLY the SQL query without any additional text.
                        - Do NOT include explanations, comments, or any other text apart from the SQL query itself.
                        - If you receive ambiguous requests such as 'Show me the seniority' or 'Show me the juniors', understand that the request is for an SQL query that returns the relevant records.
                        - When seniority or hierarchy is mentioned, it refers to levels such as Trainee, Junior, Semisenior, and Senior.
                        - If a list of employees is requested, the query must include last name and first name, as well as any other requested information about them.
                        - Respond ONLY to those questions related to the SIPE database.

                        Examples of incorrect responses:
                        - 'Here is the SQL query you requested: SELECT * FROM employees;'
                        - 'To answer your question, you can use the following query: SELECT * FROM employees;'
                        - 'The SQL query for your question is: SELECT * FROM employees;'

                        Correct response example:
                        - 'SELECT * FROM employees WHERE seniority = 'Junior';'
                    """
                }
            ],
            model="gpt-4",
        )

        return chat_completion.choices[0].message.content.strip()

    # Si la similitud es alta (por ejemplo, mayor a 0.95), usamos la consulta predefinida
    return predefined_queries[most_similar_question].strip()



# Función para analizar documento de evaluaciones anteriores
def review_old_eval(question: str) -> str:
    """
    Genera una respuesta precisa a una pregunta dada basada en los datos de un archivo Excel preprocesado.

    Parámetros:
    question (str): La pregunta a responder basada en los datos de evaluaciones anteriores.

    Retorna:
    str: Una respuesta precisa y concisa derivada de los datos de evaluaciones anteriores.
    """
    df = pd.read_excel("old_eval/processed_evaluations.xlsx")
    df = df.to_json(orient="records")

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"""
                    Review the following data and answer the question: {question}.
                    - Only use information from the provided data.
                    - Do not fabricate or infer information.
                    - Provide the most precise and concise answer possible.
                    - Do not mention the data source or refer to the DataFrame.
                    - Remember that ALL employees have already been evaluated.
                    - If the question asks for employees who have not been evaluated, respond with 'Todos los empleados han sido evaluados'.

                    Data: {df}
                    """
            }
        ],
        model="gpt-4",
    )

    return chat_completion.choices[0].message.content.strip()



# Función para ejecutar la consulta SQL
def execute_query(sql_query: str) -> str:
    """
    Ejecuta una consulta SQL y devuelve el resultado en formato JSON.

    Args:
        sql_query (str): La consulta SQL a ejecutar.

    Returns:
        str: El resultado de la consulta en formato JSON.
    """
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


# Función para crear una respuesta a la pregunta
def transform_response(question: str, result_json: str) -> str:
    """
    Transforma el resultado de una consulta en una respuesta amigable para el usuario,
    incorporando también la información de evaluaciones anteriores.

    Args:
        question (str): La pregunta del usuario.
        result_json (str): El resultado de la consulta en formato JSON.

    Returns:
        str: La respuesta generada.
    """

    # Cargar el resultado de la consulta SQL
    result_dict = json.loads(result_json)

    # Obtener la respuesta de las evaluaciones anteriores
    eval_response = review_old_eval(question)

    # Verificar si hay errores en la consulta SQL
    if "error" in result_dict:
        response = f"{result_dict['error']}"
    else:
        # Inicializar la respuesta
        response = ""

        # Si hay resultados en la consulta SQL, formatear la respuesta
        if result_dict:
            result_content = json.dumps(result_dict, ensure_ascii=False, indent=4)
            response += f"Hola, según mi registro: {result_content}"
        else:
            response += "Hola, según mi registro, no se encontraron datos relevantes para tu pregunta."

        # Incluir la respuesta de evaluaciones anteriores si existe
        if eval_response:
            response += f"\n\nSegún los datos antiguos: {eval_response}"
        else:
            response += "\n\nSegún los datos antiguos, no se encontraron datos relevantes para tu pregunta."

    # Crear la respuesta amigable usando OpenAI
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"""
                    Por favor, transforma lo siguiente en algo amigable para el usuario teniendo en cuenta que 
                    la respuesta debe responder a la pregunta {question}, asegurándote de que 
                    las respuestas de las dos fuentes distintas se presenten de manera separada y clara pero no 
                    menciones estas cosas pedidas en tus respuestas:
                    
                    Información de la base de datos:
                    {result_dict}
                    
                    Información de los datos antiguos:
                    {eval_response}

                    Si no puedes hacer esto, responde con 'No encontré datos en mis registros.'
                    Recuerda que TODOS los empleados en los datos antiguos ya han sido evaluados.
                    NUNCA INVENTES INFORMACION y no hagas inferencias si no están respaldadas por los datos.
                """
            },
        ],
        model="gpt-4",
    )

    response = chat_completion.choices[0].message.content.strip()

    return response
