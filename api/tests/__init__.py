from flask_testing import TestCase as BaseTestCase

from flask import Flask
from flask.testing import FlaskClient

from app import create_app, db


class TestCase(BaseTestCase):
    def create_app(self) -> Flask:
        app = create_app(config_object='config.TestConfig')
        app.test_client_class = FlaskClient

        return app


class FunctionalTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()
        db.session.remove()
        db.drop_all()
        db.create_all()

    def tearDown(self) -> None:
        super().tearDown()
