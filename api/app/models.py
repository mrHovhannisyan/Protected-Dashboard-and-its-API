from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions.database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def hash_password(self):
        self.password = generate_password_hash(password=self.password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
