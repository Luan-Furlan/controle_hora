from flask import Flask, jsonify, request

app = Flask(__name__)

# variável global
users = [
    {
        "id" : 1,
        "name" : "Alex de Moraes",
        "email" : "alexdemoraes@gmail.com",
        "login" : "alexdemoraes",
        "password" : "123456",
    }
]


@app.route("/api/v1/users", methods=["GET"])
def get_all_users():
    return jsonify(users)

@app.route("/api/v1/users", methods=["POST"])
def create_user():
    # recupera o objeto da requisição POST
    user = request.get_json()
    # imprime cada um dos valores
    for v in user:
        print (v)
    # gera um id sequencial
    id = len(users) + 1
    # atribui o id gerado
    user["id"] = id
    users.append(user)
    return '', 204
    return jsonify(users)

