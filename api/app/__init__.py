from flask import Flask

from app import models  # noqa
from app.extensions.database import db, migrate
from app.extensions.security import jwt


def create_app(config_object='config.Config'):
    app = Flask(__name__)
    app.config.from_object(obj=config_object)

    db.init_app(app)
    migrate.init_app(app, db, directory='app/migrations')
    jwt.init_app(app)

    from app.routes.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app
