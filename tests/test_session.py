from freelancersdk.exceptions import AuthTokenNotSuppliedException
from freelancersdk.session import Session
import unittest


class TestSession(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_session_no_auth_token(self):
        with self.assertRaises(AuthTokenNotSuppliedException):
            Session()

    def test_create_session_has_default_auth_header(self):
        oauth_token = '$866somtoken'
        s = Session(oauth_token=oauth_token)
        self.assertEquals(oauth_token, s.session.headers['Freelancer-OAuth-V1'])

    def test_create_session_has_default_user_agent(self):
        oauth_token = '$866somtoken'
        s = Session(oauth_token=oauth_token)
        self.assertEquals('Freelancer.com SDK',
                          s.session.headers['User-Agent'])
