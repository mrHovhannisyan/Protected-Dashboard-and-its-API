from http import HTTPStatus

from tests import FunctionalTestCase
from tests.factories import UserFactory


class UserLoginTestCase(FunctionalTestCase):
    def setUp(self) -> None:
        super().setUp()
        UserFactory.create()

    def test_login_returns_success_with_valid_credentials(self):
        response = self.client.post('/auth/login', json={
            "email": "john@example.com",
            "password": "secret"
        })

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIn('access_token', response.json)

    def test_login_returns_error_with_invalid_request_body(self):
        response = self.client.post('/auth/login', json={
            'email': 'invalid-email',
            'password': None
        })

        self.assertEqual(HTTPStatus.UNPROCESSABLE_ENTITY, response.status_code)
        self.assertIn('email', response.json['errors'].keys())
        self.assertIn('password', response.json['errors'].keys())

    def test_login_returns_error_with_invalid_password(self):
        response = self.client.post('/auth/login', json={
            "email": "john@example.com",
            'password': 'wrong-password'
        })

        self.assertEqual(HTTPStatus.FORBIDDEN, response.status_code)
        self.assertIn('Invalid credentials', response.json['errors'])
