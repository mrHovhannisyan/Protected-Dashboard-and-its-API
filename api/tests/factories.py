from factory.alchemy import SQLAlchemyModelFactory
from werkzeug.security import generate_password_hash

from app import db
from app.models import User, Score


class UserFactory(SQLAlchemyModelFactory):
    id = 1
    username = 'John Smith'
    email = 'john@example.com'
    password = generate_password_hash('secret')

    class Meta:
        model = User
        sqlalchemy_session = db.session


class ScoreFactory(SQLAlchemyModelFactory):
    id = 1
    result = 10
    user_id = 1

    class Meta:
        model = Score
        sqlalchemy_session = db.session
