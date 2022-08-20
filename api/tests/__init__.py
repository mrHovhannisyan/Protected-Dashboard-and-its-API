from flask_jwt_extended import create_access_token
from flask_testing import TestCase as BaseTestCase

from flask import Flask
from flask.testing import FlaskClient
from werkzeug.datastructures import Headers

from app import create_app, db


class TestClient(FlaskClient):
    access_token = None

    def authenticate(self, user):
        self.access_token = create_access_token(identity=str(user.id))

    def open(self, *args, **kwargs):
        additional_headers = Headers()

        if self.access_token is not None:
            additional_headers.add('Authorization', f'Bearer {self.access_token}')

        headers = kwargs.pop('headers', Headers())
        headers.extend(additional_headers)
        kwargs['headers'] = headers

        return super().open(*args, **kwargs)


class TestCase(BaseTestCase):
    def create_app(self) -> Flask:
        app = create_app(config_object='config.TestConfig')
        app.test_client_class = TestClient

        return app


class FunctionalTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()
        db.session.remove()
        db.drop_all()
        db.create_all()

    def tearDown(self) -> None:
        super().tearDown()
