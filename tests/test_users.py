from freelancersdk.session import Session
from freelancersdk.resources.users.helpers import (
    create_get_users_object,
)
from freelancersdk.resources.users import (
    add_user_jobs, set_user_jobs, delete_user_jobs,
    get_users,
)
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


class TestUsers(unittest.TestCase):
    def setUp(self):
        self.session = Session(oauth_token='$sometoken', url='https://fake-fln.com')

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
