from flask import Flask, jsonify, request

from controlehoras.model.user import User, UserSchema
import controlehoras.service.userservice as userservice

app = Flask(__name__)
# app = Flask(__name__, instance_relative_config=True)
# app.config.from_mapping(
#     SECRET_KEY = "dev",
#     DATABASE = os.path.join(app.instance_path, "bancodedados.sqlite"),
# )


user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route("/api/v1/users", methods=["GET"])
def get_all_users():
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
    # recupera o objeto da requisição POST
    user = user_schema.load(request.get_json(), partial=True)
    user = userservice.create_user(user)
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
