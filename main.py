import shutil
import os
import mysql.connector
import openai
import pandas as pd
import json
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks, Form
from fastapi.responses import FileResponse, JSONResponse
from ia_code.ia_sipe import generate_query, execute_query, transform_response
from ia_code.config_cnx import get_connection
from ia_code.db_schema import defaultdb
from ia_code.registro_query import guardar_consulta_correcta, guardar_consulta_error
from ia_code.load_old_eval import process_all_files_in_directory
from ia_code.voice_to_query import process_audio

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

# Configuración de la API de OpenAI
client = openai.OpenAI(api_key=os.environ.get("api_key"))

# Directorio donde se almacenarán los archivos cargados
UPLOAD_DIR = "import_xlsx"

# Crear el directorio si no existe
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Ruta raíz
@app.get("/")
async def root():
    return {"message": "Implementación de IA en SIPE"}

# Endpoint para manejar la consulta AI
@app.post("/sipe_ai_query")
async def sipe_ai_query(question: str = Form(None), audio_file: UploadFile = File(None)):
    """
    Este endpoint recibe una pregunta o un archivo de audio, lo convierte a consulta SQL y
    devuelve el resultado de la misma.

    ## Parámetros de entrada:
    - `question`: (Opcional) Pregunta de texto con temática de RR.HH.
    - `audio_file`: (Opcional) Archivo de audio con la pregunta en formato WAV.

    ## Respuesta:
    - Un diccionario con el resultado de la consulta SQL.
    """
    if question:
        # Lógica para manejar preguntas de texto
        print("Bienvenido al endpoint /sipe (texto)")
    elif audio_file:
        print("Bienvenido al endpoint /sipe (audio)")

        # Guardar el archivo de audio temporalmente
        audio_file_path = os.path.join(UPLOAD_DIR, audio_file.filename)
        with open(audio_file_path, "wb") as f:
            f.write(await audio_file.read())

        # Procesar el archivo de audio
        question = process_audio(audio_file_path)

        # Verificar si hubo un error en la transcripción
        if "error" in question:
            return JSONResponse(content={"result": question}, status_code=400)
    else:
        return JSONResponse(content={"error": "Debes proporcionar una pregunta o un archivo de audio"}, status_code=400)

    # Aquí continua tu lógica para generar y ejecutar la consulta SQL
    sql_query = generate_query(question, defaultdb)
    execute = execute_query(sql_query)

    if "error" in execute:
        guardar_consulta_error(question, sql_query, execute)
        return JSONResponse(content={"result": execute}, status_code=400)
    else:
        guardar_consulta_correcta(question, sql_query, execute)
        result = transform_response(question, execute)
        return JSONResponse(content={"result": result})


# Endpoint para subir archivos Excel
@app.post("/upload_excels/")
async def upload_excels(files: List[UploadFile]):
    """
    Este endpoint permite subir múltiples archivos Excel y guardarlos en una carpeta específica.

    ## Parámetros de entrada:
    - `files`: Una lista de los archivos Excel a subir.

    ## Respuesta:
    - Un diccionario con un mensaje indicando si los archivos se subieron correctamente o no.
    """

    uploaded_files = []
    for file in files:
        if file.filename.endswith(("xlsx", "xls")):
            file_path = os.path.join(UPLOAD_DIR, f"{file.filename}")
            shutil.copyfileobj(file.file, open(file_path, "wb"))
            uploaded_files.append(file.filename)
        else:
            return {"message": "Invalid file type. Please upload Excel files."}

    if uploaded_files:
        return {"message": f"Successfully uploaded {', '.join(uploaded_files)}"}
    else:
        return {"message": "No files were uploaded."}


# Endpoint para procesar los archivos Excel en el directorio
@app.get("/process_excel/")
async def process_excel():
    """
    Endpoint para procesar todos los archivos Excel en un directorio especificado y retornar los resultados.

    Este endpoint recorre todos los archivos Excel en el directorio definido por `UPLOAD_DIR`, 
    procesa cada hoja de cada archivo y devuelve un JSON con los datos combinados de todas las 
    hojas procesadas. El procesamiento de cada hoja se realiza a través de la API de OpenAI, 
    que estructura los datos en un formato específico.

    Además, agrega las nuevas evaluaciones al archivo Excel existente en la carpeta 'old_eval'.

    Respuesta:
        str: Una cadena JSON que contiene los datos procesados de todas las hojas de todos los archivos Excel en el directorio.
    """
    try:
        final_df = process_all_files_in_directory(UPLOAD_DIR)
        final_df["entry_date"] = final_df["entry_date"].dt.strftime("%Y-%m-%d")
        final_df["evaluation_date"] = final_df["evaluation_date"].dt.strftime("%Y-%m-%d")

        # Reemplazar NaN y valores infinitos
        final_df = final_df.fillna("null").replace([float("inf"), float("-inf")], "null")

        # Guardar o agregar al archivo Excel existente en la carpeta 'old_eval'
        old_eval_dir = os.path.join(os.getcwd(), "old_eval")
        os.makedirs(old_eval_dir, exist_ok=True)  # Crear directorio si no existe
        excel_filename = os.path.join(old_eval_dir, "processed_evaluations.xlsx")

        if os.path.exists(excel_filename):
            # Si el archivo existe, cargar los datos existentes y concatenar
            existing_df = pd.read_excel(excel_filename)
            final_df = pd.concat([existing_df, final_df], ignore_index=True)

        final_df.to_excel(excel_filename, index=False)

        # Convertir el DataFrame a un formato JSON seguro
        result_json = final_df.to_json(orient="records", date_format="iso")
        result_dict = json.loads(result_json)
        return {"result": result_dict}
    except Exception as e:
        print(f"Error processing files in directory {UPLOAD_DIR}: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing files in directory {UPLOAD_DIR}: {e}")


# Endpoint para descargar el archivo Excel de evaluaciones procesadas
@app.get("/download_processed_excel/")
async def download_processed_excel(background_tasks: BackgroundTasks):
    """
    Endpoint para descargar el archivo Excel de evaluaciones procesadas con las columnas traducidas al español.
    """
    try:
        excel_filename = os.path.join(os.getcwd(), "old_eval", "processed_evaluations.xlsx")

        if not os.path.exists(excel_filename):
            raise HTTPException(status_code=404, detail="No se encontraron evaluaciones procesadas.")

        # Cargar el DataFrame y traducir las columnas
        df = pd.read_excel(excel_filename)

        column_translations = {
            "evaluated_name": "Nombre del Evaluado",
            "entry_date": "Fecha de Ingreso",
            "evaluation_date": "Fecha de Evaluación",
            "category": "Categoría",
            "programming_language": "Lenguaje de Programación",
            "seniority": "Seniority",
            "client_project": "Proyecto o Cliente",
            "evaluator": "Evaluador",
            "avg_soft_skills": "Promedio Soft Skills",
            "avg_hard_skills": "Promedio Hard Skills",
            "final_grade": "Calificación Final",
            "previous_observations": "Observaciones Previas",
            "observations": "Observaciones",
        }

        df.rename(columns=column_translations, inplace=True)

        # Guardar el DataFrame traducido en un archivo temporal
        temp_filename = "temp_evaluations_es.xlsx"
        df.to_excel(temp_filename, index=False)

        # Enviar el archivo temporal como respuesta
        response = FileResponse(
            temp_filename,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename="evaluaciones_procesadas.xlsx",
        )

        # Definir la función de limpieza
        def cleanup():
            if os.path.exists(temp_filename):
                os.remove(temp_filename)

        # Agregar la tarea de limpieza a las tareas en segundo plano
        background_tasks.add_task(cleanup)

        return response

    except Exception as e:
        print(f"Error al descargar el archivo Excel: {e}")
        raise HTTPException(status_code=500, detail="Error al descargar el archivo Excel.")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
