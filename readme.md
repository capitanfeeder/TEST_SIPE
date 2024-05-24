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



## **Continuará...**