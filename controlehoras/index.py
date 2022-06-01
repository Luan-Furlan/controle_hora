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


@app.route("/api/v1/users/<int:id>", methods=["GET"])
def get_user_by_id(id):
    user = None
    for item in users:
        if id == item["id"]:
            user = item
            pass
    if user:
        return jsonify(user)
    else:
        return 'usuário não encontrado', 404


@app.route("/api/v1/users", methods=["POST"])
def create_user():
    # recupera o objeto da requisição POST
    user = request.get_json()
    # imprime cada um dos valores
    for v in user.items():
        print (v)
    # gera um id sequencial
    id = len(users) + 1
    # atribui o id gerado
    user["id"] = id
    users.append(user)
    return jsonify(user), 201


@app.route("/api/v1/users/<int:id>", methods=["PUT"])
def update_user(id):
    # recupera o objeto da requisição PUT
    user_request = request.get_json()
    user_request["id"] = id
    i = 0
    achou = False
    while i < len(users):
        user = users[i]
        if (id == user["id"]):
            # Seta achou = True e o índice do array user que 
            # deverá ser atualizado é i
            achou = True
            break
        i += 1

    if (achou):
        users[i] = user_request
        return users[i]
    else:
        return 'usuário não encontrado', 404

