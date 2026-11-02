@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Django API サーバーを起動します...
python manage.py runserver
pause
