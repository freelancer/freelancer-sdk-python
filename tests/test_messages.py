from freelancersdk.session import Session
from freelancersdk.resources.messages.messages import (
    create_project_thread, post_message, post_attachment
)
from freelancersdk.resources.messages.helpers import create_attachment
try:
    from unittest.mock import Mock
except ImportError:
    from mock import Mock

import unittest


class FakeCreateProjectThreadPostResponse:

    status_code = 200

    def json(self):
        return {
            'status': 'success',
            'result': {
                'id': 301,
                'thread': {
                    'thread_type': 'private_chat',
                    'time_created': 1483228800,
                    'members': [
                        101,
                        102,
                    ],
                    'context': {
                        'id': 201,
                        'type': 'project',
                    },
                    'owner': 101,
                },
            },
        }


class FakePostMessagePostResponse:

    status_code = 200

    def json(self):
        return {
            'status': 'success',
            'result': {
                'id': 401,
                'from_user_id': 101,
                'thread_id': 301,
                'message': "Let's talk",
            },
        }


class FakePostAttachmentPostResponse:

    status_code = 200

    def json(self):
        return {
            'status': 'success',
            'result': {
                'id': 401,
                'from_user_id': 101,
                'thread_id': 301,
                'message': "",
                'attachments': [
                    {
                        'key': 501,
                        'filename': 'file.txt',
                        'message_id': 401,
                    },
                ],
            },
        }


class TestMessages(unittest.TestCase):
    def setUp(self):
        self.session = Session(oauth_token='$sometoken',
                               url='https://fake-fln.com')

    def tearDown(self):
        pass

    def test_create_project_thread(self):
        thread_data = {
            'member_ids': [
                102,
            ],
            'project_id': 201,
            'message': "Let's talk",
        }

        self.session.session.post = Mock()
        self.session.session.post.return_value = \
            FakeCreateProjectThreadPostResponse()

        t = create_project_thread(self.session, **thread_data)

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        form_data = {
            'members[]': thread_data['member_ids'],
            'context_type': 'project',
            'context': thread_data['project_id'],
            'message': thread_data['message'],
        }
        self.session.session.post.assert_called_once_with(
            url='https://fake-fln.com/api/messages/0.1/threads/',
            headers=headers,
            params=None,
            data=form_data,
            json=None,
            files=None,
            verify=True)
        self.assertEquals(t.thread['context']['id'], thread_data['project_id'])
        self.assertEquals(t.thread['context']['type'], 'project')

    def test_post_message(self):
        message_data = {
            'thread_id': 301,
            'message': "Let's talk",
        }

        self.session.session.post = Mock()
        self.session.session.post.return_value = FakePostMessagePostResponse()

        m = post_message(self.session, **message_data)

        url = 'https://fake-fln.com/api/messages/0.1/threads/{}/messages/'\
              .format(message_data['thread_id'])
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        form_data = {
            'message': message_data['message'],
        }
        self.session.session.post.assert_called_once_with(
            url=url,
            headers=headers,
            params=None,
            data=form_data,
            json=None,
            files=None,
            verify=True)
        self.assertEquals(m.thread_id, message_data['thread_id'])
        self.assertEquals(m.message, message_data['message'])

    def test_post_attachment(self):
        file_object = {}
        message_data = {
            'thread_id': 301,
            'attachments': [
                create_attachment(file_object, 'file.txt'),
            ],
        }

        self.session.session.post = Mock()
        self.session.session.post.return_value = \
            FakePostAttachmentPostResponse()

        m = post_attachment(self.session, **message_data)

        url = 'https://fake-fln.com/api/messages/0.1/threads/{}/messages/'\
              .format(message_data['thread_id'])
        form_data = {
            'attachments[]': [
                'file.txt',
            ],
        }
        files = [
            ('files[]', ('file.txt', file_object)),
        ]
        self.session.session.post.assert_called_once_with(
            url=url,
            headers=None,
            params=None,
            data=form_data,
            json=None,
            files=files,
            verify=True)
        self.assertEquals(m.thread_id, message_data['thread_id'])
        self.assertTrue(getattr(m, 'attachments'))
