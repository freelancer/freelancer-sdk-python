from freelancersdk.session import Session
from freelancersdk.resources.contests.contests import create_contest
try:
    from unittest.mock import Mock
except ImportError:
    from mock import Mock

import unittest


class FakeCreateContestPostResponse:

    status_code = 200

    def json(self):
        return {
            'status': 'success',
            'result': {
                'id': 201,
                'owner_id': 101,
                'title': 'Design a logo',
                'description': 'I need a logo for my company',
                'type': 'freemium',
                'duration': 7,
                'jobs': [
                    {
                        'id': 1,
                        'name': 'Graphic Design',
                    },
                    {
                        'id': 2,
                        'name': 'Logo Design',
                    },
                ],
                'currency': {
                    'id': 1,
                    'code': 'USD',
                    'sign': '$',
                    'name': 'US Dollar',
                    'exchange_rate': 1,
                    'country': 'US',
                },
                'prize': 100,
            },
        }


class TestContest(unittest.TestCase):
    def setUp(self):
        self.session = Session(oauth_token='$sometoken',
                               url='https://fake-fln.com')

    def tearDown(self):
        pass

    def test_create_contest(self):
        contest_data = {
            'title': 'Design a logo',
            'description': 'I need a logo for my company',
            'type': 'freemium',
            'duration': 7,
            'job_ids': [
                1,
                2,
            ],
            'currency_id': 1,
            'prize': 100,
        }

        self.session.session.post = Mock()
        self.session.session.post.return_value = FakeCreateContestPostResponse()

        c = create_contest(self.session, **contest_data)

        self.session.session.post.assert_called_once_with(
            url='https://fake-fln.com/api/contests/0.1/contests/',
            headers=None,
            params=None,
            data=None,
            json=contest_data,
            files=None,
            verify=True)

        self.assertEquals(c.title, contest_data['title'])
        self.assertEquals(c.description, contest_data['description'])
        self.assertEquals(c.type, contest_data['type'])
        self.assertEquals(c.duration, contest_data['duration'])
        self.assertEquals(c.prize, contest_data['prize'])
