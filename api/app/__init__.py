from flask import Flask

from app import models  # noqa
from app.extensions.database import db, migrate
from app.extensions.security import jwt
from flask_cors import CORS


def create_app(config_object='config.Config'):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(obj=config_object)

    db.init_app(app)
    migrate.init_app(app, db, directory='app/migrations')
    jwt.init_app(app)

    from app.routes.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.routes.score import bp as score_bp
    app.register_blueprint(score_bp)

    return app
