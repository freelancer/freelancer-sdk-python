from freelancersdk.session import Session
from freelancersdk.resources.users.helpers import (
    create_get_users_object, create_get_users_details_object
)
from freelancersdk.resources.users import (
    add_user_jobs, set_user_jobs, delete_user_jobs,
    get_users, get_self_user_id, get_self, search_freelancers,
    get_user_by_id, get_reputations, get_portfolios
)
from freelancersdk.resources.users.exceptions import PortfoliosNotFoundException
try:
    from unittest.mock import Mock
except ImportError:
    from mock import Mock

import unittest


class FakeAddUserJobsPostResponse:

    status_code = 200

    def json(self):
        return {
            'status': 'success'
        }


class FakeSetUserJobsPutResponse:

    status_code = 200

    def json(self):
        return {
            'status': 'success'
        }


class FakeDeleteUserJobsPutResponse:

    status_code = 200

    def json(self):
        return {
            'status': 'success'
        }


class FakeGetUsersGetResponse:

    status_code = 200

    def json(self):
        return {
            'status': 'success',
            'result': {
                'users': {
                    '100': {
                        'status': None,
                        'id': 100,
                    },
                    '200': {
                        'status': None,
                        'id': 200,
                    }
                }
            }
        }


class FakeSearchFreelancersGetResponse:

    status_code = 200

    def json(self):
        return {
            'status': 'success',
            'result': {
                'users': {
                    '100': {
                        'status': None,
                        'id': 100,
                        'username': 'creativedesign'
                    }
                }
            }
        }


class FakeGetUserByIdGetResponse:

    status_code = 200

    def json(self):
        return {
            'status': 'success',
            'result': {
                'id': 100,
                'username': 'creativedesign'
            }
        }


class FakeGetSelfUserIdGetResponse:

    status_code = 200

    def json(self):
        return {
            'status': 'success',
            'result': {
                'id': 100,
            }
        }


class FakeGetSelfGetResponse:

    status_code = 200

    def json(self):
        return {
            'status': 'success',
            'result': {
                'id': 100,
            }
        }


class FakeGetReputationsGetResponse:

    status_code = 200

    def json(self):
        return {
            'status': 'success',
            'result': {
                '1': {
                    'user_id': 1,
                    'last3months': {
                        'completion_rate': 0.75,
                        'all': 4
                    }
                },
                '2': {
                    'user_id': 2,
                    'last3months': {
                        'completion_rate': 0.99,
                        'all': 7
                    }
                },
                '3': {
                    'user_id': 3,
                    'last3months': {
                        'completion_rate': 0.88,
                        'all': 10
                    }
                }
            }
        }


class FakeGetPortfoliosGetResponse:

    status_code = 200

    def json(self):
        return {
            'status': 'success',
            'result': {
                'portfolios': {
                    '1': [
                        {
                            'files': [{
                                'description': 'hello',
                                'filename': 'Hello.flv',
                                'id': 2000
                            }],
                            'articles': [],
                            'user_id': 1,
                            'description': 'hello!'
                        },
                        {
                            'files': [{
                                'description': 'hi',
                                'filename': 'Hi.jpg',
                                'id': 2001
                            }],
                            'articles': [],
                            'user_id': 1,
                            'description': 'hi!'
                        }
                    ]
                }
            }
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


class TestUsers(unittest.TestCase):
    def setUp(self):
        self.session = Session(
            oauth_token='$sometoken',
            url='https://fake-fln.com'
        )

    def tearDown(self):
        pass

    def test_add_user_jobs(self):
        user_jobs_data = {
            'job_ids': [
                1,
                2,
                3
            ]
        }

        self.session.session.post = Mock()
        self.session.session.post.return_value = FakeAddUserJobsPostResponse()
        p = add_user_jobs(self.session, **user_jobs_data)
        user_jobs_data.update({'jobs[]': user_jobs_data['job_ids']})
        del user_jobs_data['job_ids']
        self.session.session.post.assert_called_once_with(
            'https://fake-fln.com/api/users/0.1/self/jobs/',
            json=user_jobs_data,
            verify=True)
        self.assertEquals(p, 'success')

    def test_get_self(self):
        self.session.session.get = Mock()
        self.session.session.get.return_value = FakeGetSelfGetResponse()

        user_details = create_get_users_details_object(
            country=True,
            status=True
        )

        result = get_self(self.session, user_details)
        self.session.session.get.assert_called_once_with(
            'https://fake-fln.com/api/users/0.1/self/',
            params=user_details,
            verify=True
        )

    def test_get_self_user_id(self):
        self.session.session.get = Mock()
        self.session.session.get.return_value = FakeGetSelfUserIdGetResponse()

        result = get_self_user_id(self.session)
        self.assertTrue(self.session.session.get.called)

        self.assertEqual(100, result)

    def test_get_user_by_id(self):
        self.session.session.get = Mock()
        self.session.session.get.return_value = FakeGetUserByIdGetResponse()
        user_id = 100
        user_details = create_get_users_details_object(
            country=True,
            status=True
        )
        result = get_user_by_id(self.session, user_id, user_details)
        self.session.session.get.assert_called_once_with(
            'https://fake-fln.com/api/users/0.1/users/{}/'.format(user_id),
            params=user_details,
            verify=True
        )

    def test_set_user_jobs(self):
        user_jobs_data = {
            'job_ids': [
                1,
                2,
                3
            ]
        }

        self.session.session.put = Mock()
        self.session.session.put.return_value = FakeSetUserJobsPutResponse()
        p = set_user_jobs(self.session, **user_jobs_data)
        user_jobs_data.update({'jobs[]': user_jobs_data['job_ids']})
        del user_jobs_data['job_ids']
        self.session.session.put.assert_called_once_with(
            'https://fake-fln.com/api/users/0.1/self/jobs/',
            headers=None,
            params=None,
            data=None,
            json=user_jobs_data,
            verify=True)
        self.assertEquals(p, 'success')

    def test_delete_user_jobs(self):
        user_jobs_data = {
            'job_ids': [
                1,
                2,
                3
            ]
        }

        self.session.session.delete = Mock()
        self.session.session.delete.return_value = FakeDeleteUserJobsPutResponse()
        p = delete_user_jobs(self.session, **user_jobs_data)
        user_jobs_data.update({'jobs[]': user_jobs_data['job_ids']})
        del user_jobs_data['job_ids']
        self.session.session.delete.assert_called_once_with(
            'https://fake-fln.com/api/users/0.1/self/jobs/',
            headers=None,
            params=None,
            data=None,
            json=user_jobs_data,
            verify=True)
        self.assertEquals(p, 'success')

    def test_get_users(self):
        user_get_data = {'user_ids': [100, 200]}
        query = create_get_users_object(
            user_ids=user_get_data['user_ids']
        )
        self.session.session.get = Mock()
        self.session.session.get.return_value = FakeGetUsersGetResponse()

        get_users(self.session, query)
        self.assertTrue(self.session.session.get.called)

        query_params = self.session.session.get.call_args[1]
        self.assertIn(('users[]', [100, 200]), query_params['params'].items())

    def test_search_freelancers(self):
        self.session.session.get = Mock()
        self.session.session.get.return_value = FakeSearchFreelancersGetResponse()

        search_freelancers_data = {
            'query': 'designer',
            'limit': 10,
            'offset': 0,
            'compact': True,
        }
        user_details = create_get_users_details_object(
            country=True,
            status=True
        )
        search_freelancers_data.update(user_details)

        result = search_freelancers(
            self.session,
            query='designer',
            user_details=user_details
        )

        self.session.session.get.assert_called_once_with(
            'https://fake-fln.com/api/users/0.1/users/directory/',
            params=search_freelancers_data,
            verify=True
        )

    def test_get_reputations(self):
        self.session.session.get = Mock()
        self.session.session.get.return_value = FakeGetReputationsGetResponse()

        user_ids = [1, 2, 3]
        role = 'freelancer'
        reputation_details = {
            'job_history': True,
            'project_stats': True,
            'rehire_rates': True
        }

        get_reputations_data = {
            'users[]': user_ids,
            'jobs[]': [],
            'role': role,
        }
        get_reputations_data.update(reputation_details)
        result = get_reputations(
            self.session,
            user_ids=user_ids,
            role=role,
            reputation_details=reputation_details
        )

        self.session.session.get.assert_called_once_with(
            'https://fake-fln.com/api/users/0.1/reputations/',
            params=get_reputations_data,
            verify=True
        )
        self.assertEqual(len(result), len(user_ids))

    def test_get_portfolios(self):
        self.session.session.get = Mock()
        self.session.session.get.return_value = FakeGetPortfoliosGetResponse()
        user_ids = [1]
        limit = 10

        get_reputations_data = {
            'users[]': user_ids,
            'limit': limit,
            'offset': 0
        }

        result = get_portfolios(self.session, user_ids, limit)
        self.session.session.get.assert_called_once_with(
            'https://fake-fln.com/api/users/0.1/portfolios/',
            params=get_reputations_data,
            verify=True
        )
        self.assertEqual(len(result['portfolios']), 1)
        self.assertEqual(len(result['portfolios']['1']), 2)

    def test_get_portfolios_failure(self):
        self.session.session.get = Mock()
        response = FakeErrorResponse()
        self.session.session.get.return_value = response
        user_ids = [1]
        limit = 10

        get_reputations_data = {
            'users[]': user_ids,
            'limit': limit,
            'offset': 0
        }

        with self.assertRaises(PortfoliosNotFoundException) as cm:
            result = get_portfolios(self.session, user_ids, limit)
        e = cm.exception
        self.assertEqual(str(e), response.json()['message'])
        self.assertEqual(e.request_id, response.json()['request_id'])
        self.assertEqual(e.error_code, response.json()['error_code'])
