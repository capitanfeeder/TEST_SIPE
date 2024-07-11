import streamlit as st
import requests
import pandas as pd
import json
import re
import os
from pydub import AudioSegment
from io import BytesIO


st.title("IA en SIPE")

# Configuración para subir archivos Excel
st.header("Subir Archivos Excel")
uploaded_files = st.file_uploader("Sube tus archivos Excel", type=["xlsx", "xls"], accept_multiple_files=True)

if st.button("Subir Archivos"):
    for file in uploaded_files:
        files = {"files": (file.name, file.getvalue(), file.type)}
        response = requests.post("http://127.0.0.1:8000/upload_excels/", files=files)
        if response.status_code == 200:
            st.success(f"Archivo {file.name} subido correctamente")
        else:
            st.error(f"Error subiendo el archivo {file.name}")

# Procesar archivos Excel
st.header("Procesar Archivos Excel")
if st.button("Procesar Archivos"):
    response = requests.get("http://127.0.0.1:8000/process_excel/")
    if response.status_code == 200:
        st.success("Archivos procesados correctamente")
        data = response.json()

        # Convertir el JSON en un DataFrame de Pandas
        try:
            # El JSON retornado tiene un diccionario con una clave "result"
            if 'result' in data:
                df = pd.DataFrame(data['result'])
                st.dataframe(df)

                # Crear una visualización de ejemplo (si los datos lo permiten)
                if 'final_grade' in df.columns:
                    st.line_chart(df['final_grade'])
            else:
                st.error("El formato de los datos retornados no es el esperado.")
        except Exception as e:
            st.error(f"Error al convertir los datos: {str(e)}")
    else:
        st.error(f"Error al procesar los archivos: {response.status_code}")


# Descargar evaluaciones procesadas
st.header("Descargar Evaluaciones Procesadas")
if st.button("Descargar"):
    try:
        response = requests.get("http://127.0.0.1:8000/download_processed_excel/")
        if response.status_code == 200:
            # Obtener la carpeta de descargas del usuario
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
            if not os.path.exists(downloads_path):
                os.makedirs(downloads_path)
                
            # Guardar el archivo en la carpeta de descargas
            file_path = os.path.join(downloads_path, "evaluaciones_procesadas.xlsx")
            with open(file_path, "wb") as f:
                f.write(response.content)
                
            st.success(f"Archivo descargado correctamente: {file_path}")
        else:
            st.error(f"Error al descargar el archivo: {response.status_code}")
    except Exception as e:
        st.error(f"Error al descargar el archivo: {str(e)}")


# Consultar a la IA
st.title("IA en SIPE")
endpoint_url = "http://127.0.0.1:8000/sipe_ai_query"

st.header("Realizar Consulta SQL")

# Entrada de texto para la pregunta
question = st.text_input("Ingresa tu pregunta:")

# Botón para enviar la pregunta escrita
if st.button("Consultar pregunta escrita"):
    try:
        response = requests.post(endpoint_url, data={"question": question})
        if response.status_code == 200:
            result = response.json()
            result_str = result.get("result", "")

            # Dividir el resultado en dos partes usando la frase "Según los registros pasados"
            partes = result_str.split("Según los registros pasados")

            # Mostrar las partes en bloques separados en Streamlit
            if len(partes) > 0:
                st.markdown(partes[0])

            if len(partes) > 1:
                st.markdown("Según los registros pasados" + partes[1])
        else:
            st.error("Error realizando la consulta")
    except Exception as e:
        st.error(f"Error realizando la consulta: {str(e)}")

# Carga de archivo de audio
uploaded_file = st.file_uploader("Carga un archivo de audio", type=["wav", "mp3", "aac", "m4a", "ogg"])

# Botón para enviar el archivo de audio cargado
if uploaded_file is not None:
    if st.button("Enviar audio"):
        try:
            # Leer el archivo cargado
            audio_bytes = BytesIO(uploaded_file.read())
            
            # Enviar el archivo de audio al endpoint
            files = {'audio_file': (uploaded_file.name, audio_bytes, uploaded_file.type)}
            response = requests.post(endpoint_url, files=files)
            if response.status_code == 200:
                result = response.json()
                result_str = result.get("result", "")

                # Dividir el resultado en dos partes usando la frase "Según los registros pasados"
                partes = result_str.split("Según los registros pasados")

                # Mostrar las partes en bloques separados en Streamlit
                if len(partes) > 0:
                    st.markdown(partes[0])

                if len(partes) > 1:
                    st.markdown("Según los registros pasados" + partes[1])
            else:
                st.error("Error realizando la consulta")
        except Exception as e:
            st.error(f"Error realizando la consulta: {str(e)}")
