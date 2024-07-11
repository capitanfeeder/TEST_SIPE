import os
from dotenv import load_dotenv
from pydub import AudioSegment
from openai import OpenAI

# Cargar las variables de entorno desde el archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'crede.env')
load_dotenv(dotenv_path=dotenv_path)

# Conexion a openai
client = OpenAI(api_key=os.environ.get("api_key"))


# Función para convertir un archivo de audio a formato WAV
def convert_to_wav(input_file: str) -> str:
    """
    Convierte un archivo de audio a formato WAV.

    Args:
        input_file (str): La ruta completa al archivo de audio de entrada.

    Returns:
        str: La ruta completa del archivo WAV convertido, o None si la conversión falla.
    """
    try:
        audio = AudioSegment.from_file(input_file)
        output_file = input_file.replace(os.path.splitext(input_file)[1], ".wav")
        audio.export(output_file, format="wav")
        return output_file
    except Exception as e:
        print(f"Error al convertir archivo: {e}")
        return None


# Función para transcribir un archivo de audio a texto
def transcribe_audio(input_file: str) -> str:
    """
    Transcribe un archivo de audio WAV a texto utilizando OpenAI.

    Args:
        input_file (str): La ruta completa al archivo de audio WAV que se desea transcribir.

    Returns:
        str: El texto transcrito del audio, o None si la transcripción falla.
    """
    try:
        with open(input_file, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )
        return transcription
    except Exception as e:
        print(f"Error al transcribir audio: {e}")
        return None


# Función para procesar un archivo de audio
def process_audio(input_file: str) -> str:
    """
    Procesa un archivo de audio, convirtiéndolo a formato WAV y luego transcribiéndolo a texto.

    Args:
        input_file (str): La ruta completa al archivo de audio de entrada.

    Returns:
        str: El texto transcrito del audio, o un mensaje de error si la transcripción falla.
    """
    try:
        # Convertir a WAV
        output_wav_file = convert_to_wav(input_file)
        if output_wav_file:
            print(f"Archivo convertido a WAV: {output_wav_file}")
            # Transcribir audio
            transcription = transcribe_audio(output_wav_file)
            if transcription:
                return transcription
            else:
                return "Error en la transcripción."
        else:
            return "Error en la conversión a WAV."
    finally:
        # Eliminar archivos de audio
        if os.path.exists(input_file):
            os.remove(input_file)
            print(f"Archivo eliminado: {input_file}")
        if output_wav_file and os.path.exists(output_wav_file):
            os.remove(output_wav_file)
            print(f"Archivo eliminado: {output_wav_file}")
