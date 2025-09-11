#!/bin/bash

# Define la ruta del entorno virtual
VENV_DIR="./venv"

# Crea el entorno virtual
python3.10 -m venv "$VENV_DIR"

# Activa el entorno virtual
source "$VENV_DIR/bin/activate"

# Actualiza la versión del pip
"$VENV_DIR/bin/python" -m pip install --upgrade pip

# Instala los paquetes de requirements.txt
"$VENV_DIR/bin/pip" install --upgrade -r requirements.txt

echo "Entorno virtual completo."
