import pandas as pd
import os
import json
import warnings
import calendar
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

warnings.filterwarnings("ignore", message="The behavior of DataFrame concatenation with empty or all-NA entries is deprecated")
warnings.filterwarnings("ignore", message="The behavior of 'to_datetime' with 'unit' when parsing strings is deprecated. In a future version, strings will be parsed as datetime strings, matching the behavior without a 'unit'. To retain the old behavior, explicitly cast ints or floats to numeric type before calling to_datetime.")

# Cargar las variables de entorno desde el archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'cred.env')
load_dotenv(dotenv_path=dotenv_path)

client = OpenAI(api_key=os.environ.get("api_key"))


def create_empty_dataframe() -> pd.DataFrame:
    """
    Crea un DataFrame vacío con columnas predefinidas.

    Returns:
        pd.DataFrame: DataFrame vacío con columnas predefinidas.
    """
    columns = [
        "evaluated_name", "entry_date", "evaluation_date", "category", 
        "programming_language", "seniority", "client_project", "evaluator", 
        "avg_soft_skills", "avg_hard_skills", "final_grade", 
        "previous_observations", "observations"
    ]
    return pd.DataFrame(columns=columns)


def process_skills(file_path: str, sheet_name: str) -> (pd.DataFrame, pd.DataFrame):
    """
    Procesa las habilidades blandas y duras desde una hoja de cálculo.

    Args:
        file_path (str): Ruta del archivo Excel.
        sheet_name (str): Nombre de la hoja de cálculo.

    Returns:
        (pd.DataFrame, pd.DataFrame): DataFrames de habilidades blandas y duras.
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
    
    # Procesamiento de soft skills
    df_soft = df.drop(index=df.index[-5:])
    filas_especificas = df_soft.iloc[[9, 10, 11, 13, 14, 15, 16, 17]]
    ultimas_filas = df_soft.iloc[-3:]
    soft_skills = pd.concat([filas_especificas, ultimas_filas])
    
    # Procesamiento de hard skills
    df_hard = df.drop(index=df.index[0:19])
    hard_skills = df_hard.drop(index=df_hard.index[-9:])
    
    return soft_skills, hard_skills


def process_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Procesa un DataFrame transformando y seleccionando filas específicas.

    Args:
        df (pd.DataFrame): DataFrame original.

    Returns:
        pd.DataFrame: DataFrame procesado.
    
    Raises:
        ValueError: Si el DataFrame tiene menos de 5 filas.
    """
    if df.shape[0] < 5:
        raise ValueError("El DataFrame debe tener al menos 5 filas.")
    
    transposed_df = df.transpose()
    selected_rows = transposed_df.iloc[[0, 2, 3, 4, 5, 6]]
    selected_rows.reset_index(drop=True, inplace=True)
    column_names = ['Categoria', '0', '0.25', '0.5', '0.75', '1']
    processed_df = selected_rows.transpose()
    processed_df.columns = column_names
    
    return processed_df


def calculate_average_score(df: pd.DataFrame) -> float:
    """
    Calcula el puntaje promedio de un DataFrame basado en valores booleanos en columnas específicas.

    Args:
        df (pd.DataFrame): DataFrame con datos para calcular el puntaje.

    Returns:
        float: Puntaje promedio.
    
    Raises:
        ValueError: Si faltan columnas esperadas en el DataFrame.
    """
    expected_columns = ['Categoria', '0', '0.25', '0.5', '0.75', '1']
    for col in expected_columns:
        if col not in df.columns:
            raise ValueError(f"El DataFrame debe contener la columna {col}")

    score_columns = ['0', '0.25', '0.5', '0.75', '1']
    total_score = 0
    valid_rows = 0

    for index, row in df.iterrows():
        row_score = None
        boolean_found = False
        for col in score_columns:
            if isinstance(row[col], bool):
                boolean_found = True
                if row[col] == True:
                    row_score = float(col)
                    break
        if boolean_found and row_score is not None:
            total_score += row_score
            valid_rows += 1

    if valid_rows == 0:
        return 0.0

    average_score = total_score / valid_rows
    return average_score


def process_and_transform_skills(file_path: str, sheet_name: str) -> dict:
    """
    Procesa y transforma habilidades blandas y duras de una hoja de cálculo y calcula sus puntajes promedio.

    Args:
        file_path (str): Ruta del archivo Excel.
        sheet_name (str): Nombre de la hoja de cálculo.

    Returns:
        dict: Diccionario con puntajes promedio de habilidades blandas y duras.
    """
    soft_skills, hard_skills = process_skills(file_path, sheet_name)
    
    processed_soft_skills = process_dataframe(soft_skills)
    processed_hard_skills = process_dataframe(hard_skills)
    
    average_soft_skills = calculate_average_score(processed_soft_skills)
    average_hard_skills = calculate_average_score(processed_hard_skills)
    
    return {
        'avg_soft_skills': average_soft_skills,
        'avg_hard_skills': average_hard_skills
    }


def process_excel_file(file_path: str, sheet_name: str) -> pd.DataFrame:
    """
    Procesa un archivo Excel específico y transforma los datos en un DataFrame.

    Args:
        file_path (str): Ruta del archivo Excel.
        sheet_name (str): Nombre de la hoja de cálculo.

    Returns:
        pd.DataFrame: DataFrame con los datos procesados.
    """
    try:
        excel = pd.read_excel(file_path, sheet_name=sheet_name)
        
        skills = process_and_transform_skills(file_path, sheet_name)
        
        message_content = (
            f"You are an assistant and you need to review this file: {excel.to_json(orient='records')} to do the following: "
            "Return a spreadsheet with the columns: evaluated_name, entry_date, evaluation_date, category, "
            "programming_language, seniority, client_project, evaluator, final_grade, previous_observations, observations. "
            "Only include the columns that have been explicitly instructed or requested. "
            "Please fill in the programming_language column using only the programming language mentioned in the CATEGORY field. Do not include any additional information."
            "Please fill in the seniority column using only the seniority level (e.g., Trainee, Junior, Ssr, Senior) mentioned in the CATEGORY field. Do not include any additional information."
            "Return only the complete final values, excluding formulas or code, and do it in JSON format without any extra comments."
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": message_content}
            ],
            model="gpt-3.5-turbo",
        )

        result = chat_completion.choices[0].message.content
        json_obj = json.loads(result)
        result_df = pd.json_normalize(json_obj)
        result_df["entry_date"] = pd.to_datetime(result_df["entry_date"], unit="ms")

        def convert_evaluation_date(date) -> pd.Timestamp:
            """
            Convierte una fecha de evaluación a un objeto pd.Timestamp.

            Args:
                date: La fecha de evaluación, que puede ser un entero (timestamp en milisegundos)
                    o una cadena (nombre del mes en español).

            Returns:
                pd.Timestamp: La fecha de evaluación convertida.

            Raises:
                ValueError: Si el nombre del mes es inválido o el formato de la fecha no es compatible.
            """
            if isinstance(date, int):
                return pd.to_datetime(date, unit="ms")
            elif isinstance(date, str):
                month = date.capitalize()
                current_year = datetime.now().year
                month_mapping = {
                    "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
                    "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
                    "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
                }
                month_number = month_mapping.get(month)
                if month_number is None:
                    raise ValueError(f"Invalid month name: {month}")
                return pd.Timestamp(datetime(current_year, month_number, 1))
            else:
                raise ValueError(f"Unsupported date format: {date}")

        result_df["evaluation_date"] = result_df["evaluation_date"].apply(convert_evaluation_date)
        
        result_df["avg_soft_skills"] = skills['avg_soft_skills']
        result_df["avg_hard_skills"] = skills['avg_hard_skills']
        
        column_order = [
            "evaluated_name", "entry_date", "evaluation_date", "category", 
            "programming_language", "seniority", "client_project", "evaluator", 
            "avg_soft_skills", "avg_hard_skills", "final_grade", 
            "previous_observations", "observations"
        ]
        result_df = result_df[column_order]

    except Exception as e:
        print(f"Error processing sheet {sheet_name} in file {file_path}: {e}")
        result_df = create_empty_dataframe()

    return result_df


def process_all_sheets(file_path: str) -> pd.DataFrame:
    """
    Procesa todas las hojas de un archivo Excel y concatena los resultados en un DataFrame final.

    Args:
        file_path (str): Ruta del archivo Excel.

    Returns:
        pd.DataFrame: DataFrame final con los datos de todas las hojas procesadas.
    """
    final_df = create_empty_dataframe()
    try:
        with pd.ExcelFile(file_path) as excel_file:
            sheet_names = excel_file.sheet_names

        for sheet_name in sheet_names:
            sheet_df = process_excel_file(file_path, sheet_name)
            final_df = pd.concat([final_df, sheet_df], ignore_index=True)
        
        # Eliminar el archivo después de procesar todas las hojas
        try:
            os.remove(file_path)
            print(f"Archivo eliminado: {file_path}")
        except Exception as e:
            print(f"Error eliminando el archivo {file_path}: {e}")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

    return final_df


def process_all_files_in_directory(directory_path: str) -> pd.DataFrame:
    """
    Procesa todos los archivos Excel en un directorio y concatena los resultados en un DataFrame final.

    Args:
        directory_path (str): Ruta del directorio que contiene los archivos Excel.

    Returns:
        pd.DataFrame: DataFrame final con los datos de todos los archivos procesados.
    """
    final_df = create_empty_dataframe()

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".xlsx") or file.endswith(".xls"):
                file_path = os.path.join(root, file)
                file_df = process_all_sheets(file_path)
                final_df = pd.concat([final_df, file_df], ignore_index=True)
        
    return final_df
