from controlehoras.model.user import User
import controlehoras.db as db


def get_all_users():
    print("dao - get all users")
    users = db.get_db().execute('select * from USER').fetchall()
    print(users)
    print(type(users))
    for user in users:
        for item in dict(user):
            print (item)
        print(user["name"])
    return users


def create_user(user):
    print("dao - create user")
    print('name',     user.name)
    print('email',    user.email)
    print('login',    user.login)
    print('password', user.password)
    connection = db.get_db()
    try:
        connection.execute(
            'insert into USER (name, email, login, password)' +
            'values(?, ?, ?, ?)',
            (user.name, user.email, user.login, user.password)
        )
        user_db = connection.execute(
            'select id from USER where name = ?', [user.name]
        ).fetchone()
        connection.commit()
        user.id = user_db["id"]
    except Exception as e:
        print("Error", str(e))
        connection.rollback()
        raise (e)
    return user
