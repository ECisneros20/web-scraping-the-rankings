@echo off
REM Define la ruta del entorno virtual
set VENV_DIR=.\venv

REM Activa el entorno virtual
call %VENV_DIR%\Scripts\activate.bat

REM Compila el script en un ejecutable usando pyinstalle
pyinstaller --onefile web_scraping.py --name descargar_ranking_the

REM Mueve el ejecutable a la ruta raíz del proyecto
move dist\* .

REM Borra las carpetas irrelevantes
del descargar_ranking_the.spec
rmdir build /s /q
rmdir dist /s /q

echo Ejecutable completo.
pause
