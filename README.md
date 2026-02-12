# Generador Fake Data

Este proyecto es una herramienta diseñada para generar datos falsos de usuarios (Personas Naturales y Jurídicas) en Colombia, útil para ambientes de pruebas y desarrollo. La aplicación genera información detallada como nombres, documentos de identidad (con dígito de verificación DIAN real), direcciones, vehículos, y más, exportando todo a un archivo de Excel.

## Características

- **Generación de Usuarios**: Crea perfiles completos de personas naturales y jurídicas.
- **Datos Colombianos Reales**: Utiliza formatos válidos para NIT, cédulas, direcciones y teléfonos.
- **Validación DIAN**: Incluye un algoritmo real para calcular el Dígito de Verificación (DV) según la DIAN.
- **Vehículos**: Asigna una cantidad configurable de vehículos a cada usuario con placas válidas.
- **Exportación Múltiple**: Genera archivos `.xlsx` y `.csv` simultáneamente.
- **Doble Interfaz**:
    -   **Escritorio (Tkinter)**: Aplicación nativa con mejoras visuales.
    -   **Web (Flask)**: Nueva interfaz web local para generar y descargar datos en un ZIP.

## Dependencias

El proyecto utiliza las siguientes librerías de Python:
- `pandas`: Para la manipulación de datos y exportación a Excel.
- `Faker`: Para la generación de datos aleatorios realistas.
- `Unidecode`: Para el manejo de caracteres especiales.
- `openpyxl`: Motor para escribir archivos Excel.
- `pyinstaller`: Para generar el ejecutable de la aplicación.
- `flask`: Para la interfaz web.

## Requisitos Previos

- Python 3.8 o superior.
- pip (gestor de paquetes de Python).

## Instalación

1.  **Clonar el repositorio** (o descargar el código fuente):
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd GeneradorFakeData
    ```

2.  **Crear un entorno virtual** (Recomendado):
    ```bash
    # En Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # En macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

### Ejecutar desde código fuente

1.  Asegúrate de tener el entorno virtual activado.
2.  Ejecuta el script principal:
    ```bash
    python generadorData.py
    ```
3.  En la interfaz gráfica:
    -   Ingresa la cantidad de usuarios a generar.
    -   Define el rango mínimo y máximo de vehículos por usuario.
    -   Haz clic en "Generar Datos (Excel y CSV)".
    -   Haz clic en "Generar Datos (Excel y CSV)".
4.  Los archivos `datos.xlsx` y `datos.csv` se crearán en el mismo directorio.

### Interfaz Web (Flask)

Si prefieres usar una interfaz web local:

1.  Ejecuta la aplicación web:
    ```bash
    python web_app.py
    ```
2.  Abre tu navegador y ve a `http://127.0.0.1:5000`.
3.  Ingresa los parámetros y haz clic en "Generar y Descargar (ZIP)".
4.  Se descargará un archivo ZIP conteniendo ambos formatos (.xlsx y .csv).


### Generar Ejecutable (.exe)

Si deseas distribuir la aplicación sin necesidad de instalar Python en otros equipos:

1.  Ejecuta el siguiente comando para construir el ejecutable usando el archivo de especificación incluido:
    ```bash
    pyinstaller generadorData.spec
    ```
2.  Al finalizar, encontrarás el ejecutable `generadorData.exe` en la carpeta `dist/`.

## Estructura del Proyecto

- `generadorData.py`: Script principal e interfaz gráfica.
- `datosUsuario1.py`: Lógica de generación de personas y vehículos.
- `digitoDIAN.py`: Módulo para el cálculo del dígito de verificación DIAN.
- `paises.py`, `dep_mun_dian.py`: Diccionarios de datos geográficos.
- `generadorData.spec`: Archivo de configuración para PyInstaller.
- `requirements.txt`: Lista de dependencias del proyecto.
