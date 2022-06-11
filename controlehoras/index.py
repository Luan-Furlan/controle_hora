import os

from flask import Flask, jsonify, request

from controlehoras.model.user import UserSchema
import controlehoras.service.userservice as userservice

"""
configuracoes de banco de dados e de inicialização
"""

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY = "dev",
    DATABASE = os.path.join(app.instance_path, "bancodedados.sqlite"),
)

# if test_config is None:
#     # carrega a configuração da instancia, se existir, quando não estiver testando
#     app.config.from_pyfile("config.py", silent=True)
# else:
#     # carrega a configuração de teste se for passada
#     app.config.update(test_config)

# garante que a pasta da instância existe
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# registra os comandos do banco de dados
from controlehoras import db

db.init_app(app)




user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route("/api/v1/users", methods=["GET"])
def get_all_users():
    print("controller - get all users")
    users = userservice.get_all_users()
    return jsonify(users_schema.dump(users))


@app.route("/api/v1/users/<int:id>", methods=["GET"])
def get_user_by_id(id):
    user = userservice.get_user_by_id(id)
    if user:
        return jsonify(user_schema.dump(user))
    else:
        return 'usuário não encontrado', 404


@app.route("/api/v1/users", methods=["POST"])
def create_user():
    print("controller - create user")
    # recupera o objeto da requisição POST
    user = user_schema.load(request.get_json(), partial=True)
    # chama método do user_service
    user = userservice.create_user(user)
    # retorna objeto user convertido para json
    return jsonify(user_schema.dump(user))


@app.route("/api/v1/users/<int:id>", methods=["PUT"])
def update_user(id):
    # recupera o objeto da requisição PUT
    user = user_schema.load(request.get_json())
    try:
        user = userservice.update_user(id, user)
        return jsonify(user_schema.dump(user)), 200
    except Exception:
        return 'usuário não encontrado', 404
