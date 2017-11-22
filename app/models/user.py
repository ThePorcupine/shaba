
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from . import Base
from .. import db


class User(UserMixin, Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.Text())

    def __init__(self, email, password, **kwargs):
        # Hash into method$salt$hash
        passHash = generate_password_hash(password=password,
                                          method='sha256',
                                          salt_length=18)

        self.password = passHash
        self.email = email
