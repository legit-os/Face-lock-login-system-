@echo off
set LOGFILE=%~dp0detection_bat.log

echo ============================== >> "%LOGFILE%"
echo Started at %DATE% %TIME% >> "%LOGFILE%"
cd /d "%~dp0" >> "%LOGFILE%" 2>&1

if not exist "emb.pt" (
    echo emb.pt NOT FOUND >> "%LOGFILE%"
    exit /b
)

echo emb.pt FOUND >> "%LOGFILE%"

call .venv\Scripts\activate.bat >> "%LOGFILE%" 2>&1
echo venv activated >> "%LOGFILE%"

where python >> "%LOGFILE%" 2>&1
python --version >> "%LOGFILE%" 2>&1

python detection.py >> "%LOGFILE%" 2>&1

echo Finished at %DATE% %TIME% >> "%LOGFILE%"
