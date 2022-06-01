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

