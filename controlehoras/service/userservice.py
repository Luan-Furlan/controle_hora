from controlehoras.model.user import User
import controlehoras.dao.userdao as userdao


def get_all_users():
    print("service - get all users")
    return userdao.get_all_users()


def get_user_by_id(id):
    user = None
    for item in users:
        if id == item.id:
            user = item
            pass
    return user


def create_user(user):
    print("service - create user")
    print ("id ", user.id)
    user_retornado = userdao.create_user(user)
    print ("id ", user.id)
    return user_retornado


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

