# Importamos las librerias
import os
from pathlib import Path

# Definimos el nombre del proyecto y la lista de archivos a crear
project_name = "us_visa"

# Creamos la lista de archivos a crear
"""
Todas las rutas van a contener __init__.py para que se puedan importar los modulos sin problemas,
hay que tener en cuenta que se va crear una nueva carpeta en nuestro ROOT "US_VISA_PROJECT" con el nombre del proyecto y dentro de esta carpeta se van a crear las siguientes carpetas y rutas
"""

list_of_files = [
    # Carpetas y archivos segun sea necesario dentro de la carpeta "us_visa" practicamente le estamos dando la ruta
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediccion_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    # Creamos archivos en el ROOT del proyecto osea en US_VISA_PROJECT
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml"
]

# Creamos los archivos y carpetas segun la lista de archivos a crear
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")