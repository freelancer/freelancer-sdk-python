from freelancersdk.session import Session
from freelancersdk.resources.contests.contests import create_contest
from freelancersdk.resources.contests.exceptions import ContestNotCreatedException
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


class FakeErrorResponse:

    status_code = 500

    def json(self):
        return {
            'status': 'error',
            'message': 'An error has occurred.',
            'error_code': 'ExceptionCodes.UNKNOWN_ERROR',
            'request_id': '3ab35843fb99cde325d819a4'
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

    def test_create_contest_fail(self):
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

        response = FakeErrorResponse()
        self.session.session.post = Mock()
        self.session.session.post.return_value = response

        with self.assertRaises(ContestNotCreatedException) as cm:
            c = create_contest(self.session, **contest_data)
        e = cm.exception
        self.assertEqual(str(e), response.json()['message'])
        self.assertEqual(e.request_id, response.json()['request_id'])
        self.assertEqual(e.error_code, response.json()['error_code'])
