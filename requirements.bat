@echo off
REM Define la ruta del entorno virtual
set VENV_DIR=.\venv

REM Crea el entorno virtual
call py -3.10 -m venv %VENV_DIR%

REM Activa el entorno virtual
call %VENV_DIR%\Scripts\activate.bat

REM Actualiza la versión del pip
call python.exe -m pip install --upgrade pip

REM Instala los paquetes de requirements.txt
pip install --upgrade -r requirements.txt

echo Entorno virtual completo.
pause
