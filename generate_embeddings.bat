@echo off
cd /d "%~dp0"

REM Activate uv virtual environment
call .venv\Scripts\activate.bat

REM Run embedding generation
python face_hash.py

REM Optional: pause so you can see errors
pause
