@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist "..\.venv\Scripts\python.exe" (
    echo READMEに従って仮想環境とパッケージを準備してください。
    pause
    exit /b 1
)
echo Django API サーバーを起動します...
"..\.venv\Scripts\python.exe" manage.py runserver 8001
pause
