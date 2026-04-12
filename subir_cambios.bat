@echo off
cd /d "d:\ESCUELA\Primer Examenes EEUA\ESCUELA"
echo.
set /p mensaje="Descripcion del cambio: "
git add .
git commit -m "%mensaje%"
git push
echo.
echo Listo! Los cambios ya estan en GitHub y Streamlit se actualiza solo.
pause
