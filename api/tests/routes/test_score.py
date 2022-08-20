from http import HTTPStatus

from tests import FunctionalTestCase
from tests.factories import UserFactory, ScoreFactory


class UserScoreTestCase(FunctionalTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.user = UserFactory.create()
        ScoreFactory.create()

    def test_get_user_score_should_fail_when_not_authorized(self):
        response = self.client.get('/score/my')

        self.assertEqual(HTTPStatus.UNAUTHORIZED, response.status_code)

    def test_get_user_score_should_return_score(self):
        self.client.authenticate(user=self.user)
        response = self.client.get('/score/my')

        self.assertEqual(HTTPStatus.OK, response.status_code)

