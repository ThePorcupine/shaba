
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from . import Base
from .. import db


class User(UserMixin, Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    salt = db.Column(db.String(18))

    def __init__(self, email, password, **kwargs):
        # Hash into method$salt$hash
        passHash = generate_password_hash(password=password,
                                          method='sha256',
                                          salt_length=18)

        splitPass = passHash.split("$")

        self.password = splitPass[2]
        self.salt = splitPass[1]

        self.email = email
