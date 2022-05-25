@echo off
set FLASK_APP=./controlehoras/index.py
REM Essa variável permite que a aplicação recarregue toda vez que a aplicação mudar
set FLASK_ENV=development

for /f usebackq %%V in (`pipenv --venv`) do set VENV=%%V
call %VENV%\scripts\activate.bat

flask run -h 0.0.0.0
