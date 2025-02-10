OurTemixInData

Este proyecto tiene como objetivo analizar los datos climatológicos de las estaciones meteorológicas RUOA y ESOLMET. A continuación, se describe la estructura del repositorio:

📂 Estructura del Proyecto

📁 data/

001_raw/: Contiene los datos sin modificar.

002_limpios/: Datos con estructura deseada (columnas adecuadas, nombres correctos, datos faltantes como NaN, etc.).

003_finales/: Datos completos después de modificaciones mediante regresiones lineales y/o combinación con otras fuentes; sin anomalías.

📁 docs/

Contiene la documentación relacionada con la instalación, uso y desarrollo del proyecto.

📁 notebooks/

Guarda notebooks de pruebas, análisis exploratorio y prototipado.

📁 tests/

Carpeta para pruebas unitarias, garantizando la estabilidad del código.

📜 Archivos Principales

app.py: Código ejecutable para la aplicación.

README.md: Introducción y guía de uso del proyecto.

requirements.txt: Lista de dependencias del proyecto.

📂 Otros archivos y directorios

.gitignore: Archivo que especifica qué elementos deben ser ignorados por Git.

venv/: Contiene el ambiente virtual utilizado.

img/: Almacena gráficas e imágenes de salida.

Este repositorio está diseñado para ser colaborativo y escalable, permitiendo un análisis eficiente de los datos climatológicos. 🚀

