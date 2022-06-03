from controlehoras.model.user import User

# variável global
users = [
    User(1, "Alex de Moraes","alexdemoraes@gmail.com","alexdemoraes","123456")
]


def get_all_users():
    return users


def get_user_by_id(id):
    user = None
    for item in users:
        if id == item.id:
            user = item
            pass
    return user


def create_user(user):
    # gera um id sequencial
    id = len(users) + 1
    # atribui o id gerado
    user.id = id
    users.append(user)
    return user


def update_user(id, user):
    # sobrescrevendo a propried id do usuario com o id do parametro
    user.id = id
    # buscando no array por um usuário com o mesmo id do parametro
    i = 0
    achou = False
    while i < len(users):
        item = users[i]
        if (id == item.id):
            # Atribui True para achou e o índice do array user que 
            # deverá ser atualizado é i
            achou = True
            break
        i += 1

    if (achou):
        users[i] = user
        return users[i]
    else:
        raise "não encontrado"

