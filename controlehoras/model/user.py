from signal import default_int_handler
from typing_extensions import Required

from marshmallow import Schema, fields, post_load

class User():
    def __init__(self, id, name, email, login, password):
        self.id = id
        self.name = name
        self.email = email
        self.login = login
        self.password = password

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)


class UserSchema(Schema):
    id = fields.Integer(allow_none=True, missing=True, default=None)
    name = fields.Str()
    email = fields.Str()
    login = fields.Str(allow_none=True, missing=True)
    password = fields.Str()

    @post_load
    def make_user(self, data, **kwargs):
        data["id"] = None
        return User(**data)
