set FLASK_APP=./controlehoras/index.py
REM Essa variável permite que a aplicação recarregue toda vez que a aplicação mudar
set FLASK_ENV=development

source $(pipenv --venv)/bin/activate

flask run -h 0.0.0.0