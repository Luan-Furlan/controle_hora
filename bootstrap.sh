#!/bin/bash

export FLASK_APP=./controlehoras/index.py
# Essa variável permite que a aplicação recarregue toda vez que a aplicação mudar 
export FLASK_ENV=development

source $(pipenv --venv)/bin/activate

flask run -h 0.0.0.0
