# **Implementacion de IA en `SIPE`**

## **Introducción**

### El presente documento tiene como objetivo describir el proceso de implementación de inteligencia artificial en el sistema de gestión de personal `SIPE`.

## **Requerimientos**

### Para replicar el proceso de implementación de IA en `SIPE`, se requiere de los siguientes elementos:

### 1. **Configurar un entorno siguiendo los siguientes pasos:**

**a) Crear un entorno virtual**: colocando el siguiente comando en terminal, reemplazando "your-env-name" por el nombre que desees darle al entorno virtual:

`python -m venv "your-env-name"`

**b) Activar el entorno virtual**: colocando el siguiente comando en terminal:

Desde windows:

`.\your-env-name\Scripts\Activate`

Desde linux:

`source your-env-name/bin/activate`

**c) Ubicarse dentro del entorno y clonar el repositorio**

### 2. **Clave API de OpenAI**: Para obtener la clave API de OpenAI, se debe seguir el siguiente enlace: [OpenAI](https://platform.openai.com/signup). Una vez obtenida la clave API, se debe establecer como variable de entorno en el sistema operativo siguiendo los pasos:

**a) Abrir el Símbolo del sistema:** Puedes encontrarlo buscando "cmd" en el menú de inicio.

**b) Establecer variable de entorno en la sesión actual:** Para establecer la variable de entorno en la sesión actual, usa el siguiente comando, reemplazando your-api-key-here con tu clave API real:

`setx OPENAI_API_KEY "your-api-key-here"`

### 3. **Instalar las librerías necesarias:** mediante el comando:

`pip install -r requirements.txt`

### 4. **Configurar el archivo `cred.env`**: se debe incorporar las credenciales de acceso a la base de datos de `Sipe` en el archivo `cred.env`.

### 5. **Levantar la API de `Sipe`**: mediante el comando:

`python main.py`


## **Descripción General de la Funcionalidad:**

### El proyecto ofrece dos funcionalidades principales:

### 1. Responder preguntas relacionadas con RRHH convirtiéndolas en consultas SQL y consultando la base de datos SIPE (implementado en main.py).

### 2. Procesar archivos Excel cargados que contienen datos de evaluación de empleados y transformarlos en un formato JSON estructurado (implementado en ia_code/load_old_eval.py).


## **Análisis del Código:**

### 1. `main.py`:
Maneja la configuración y los puntos finales de la API.
Brinda funcionalidades para:
- Responder preguntas de los usuarios utilizando el punto final sql_query (llama a ia_code.ia_sipe.generate_query para generar SQL).
- Cargar archivos Excel utilizando el punto final upload_excels.
- Procesar archivos Excel cargados utilizando el punto final process_excel (llama a ia_code.load_old_eval.process_all_files_in_directory).

### 2. `config_cnx.py`: 
Establece conexión a la base de datos MySQL utilizando las credenciales de cred.env.

### 3. `ia_sipe.py`:
Contiene funciones para:
- Encontrar consultas predefinidas a partir de una hoja de Excel (get_predefined_queries_from_excel).
- Preprocesar el texto del usuario (preprocess_text).
- Encontrar la pregunta más similar entre las predefinidas (find_most_similar_question).
- Generar consultas SQL basadas en las preguntas del usuario (generate_query).
- Ejecutar consultas SQL y transformar los resultados (execute_query, transform_response).

### 4. `load_old_eval.py`:
Procesa archivos Excel cargados que contienen datos de evaluación.
Las funciones incluyen:
- Crear un DataFrame vacío con columnas predefinidas (create_empty_dataframe).
- Procesar datos de habilidades blandas y duras (process_skills).
- Transformar y seleccionar filas específicas de DataFrames (process_dataframe).
- Calcular puntajes promedio (calculate_average_score).
- Procesar y transformar datos de habilidades, calculando sus puntajes promedio (process_and_transform_skills).
- Procesar una hoja de Excel específica y transformar datos (process_excel_file).
- Procesar todas las hojas en un archivo de Excel (process_all_sheets).
- Procesar todos los archivos de Excel en un directorio (process_all_files_in_directory).

### 5. `registro_query.py`:
Administra el registro de consultas en archivos de Excel separados según el éxito o error (guardar_consulta_correcta, guardar_consulta_error).


## **Autores:**
- González Nehuén (Analista de Datos Jr.)
- Sosa Gabriel (Analista de Datos Jr.)