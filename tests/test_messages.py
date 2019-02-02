from freelancersdk.session import Session
from freelancersdk.resources.messages.messages import (
    create_project_thread, post_message, post_attachment, get_messages,
    get_threads, search_messages
)
from freelancersdk.resources.messages.helpers import (
    create_attachment, create_get_threads_object, create_get_threads_details_object,
    create_get_messages_object
)

from freelancersdk.resources.messages.exceptions import MessageNotCreatedException
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


class FakeGetMessagesGetResponse:
    status_code = 200

    def json(self):
        return {
            'status': 'success',
            'result': {
                'unfiltered_count': 2,
                'messages': [
                    {
                        'message_source': 'default_msg',
                        'attachments': [],
                        'thread_id': 1,
                        'message': 'Hello world!',
                        'id': 1,
                    },
                    {
                        'message_source': 'default_msg',
                        'attachments': [],
                        'thread_id': 1,
                        'message': 'Test message',
                        'id': 2,
                    }
                ]
            }
        }


class FakeSearchMessagesGetResponse:
    status_code = 200

    def json(self):
        return {
            'status': 'success',
            'result': {
                'unfiltered_count': 1,
                'messages': [
                    {
                        'message_source': 'default_msg',
                        'attachments': [],
                        'thread_id': 1,
                        'message': 'Hello world!',
                        'id': 1,
                    }
                ]
            }
        }


class FakeGetThreadsGetResponse:
    status_code = 200

    def json(self):
        return {
            'status': 'success',
            'result': {
                'threads': [
                    {
                        'time_updated': 1519826182,
                        'thread': {
                            'context': {
                                'type': 'project',
                                'id': 101
                            },
                            'thread_type': 'private_chat',
                            'write_privacy': 'members',
                            'time_created': 1519826180,
                            'id': 100,
                            'members': [
                                102,
                                103
                            ],
                            'owner': 103,
                            'owner_read_privacy': 'members',
                            'read_privacy': 'members'
                        },
                        'is_muted': False,
                        'is_read': True
                    }
                ]
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

    def test_get_messages(self):
        thread_ids = [1]

        query = create_get_messages_object(
            threads=thread_ids,
            thread_details=True
        )

        self.session.session.get = Mock()
        self.session.session.get.return_value = FakeGetMessagesGetResponse()

        response = get_messages(self.session, query)
        self.session.session.get.assert_called_once_with(
            'https://fake-fln.com/api/messages/0.1/messages/',
            params=query,
            verify=True
        )
        self.assertEquals(len(response['messages']), 2)

    def test_search_messages(self):
        query = {
            'thread_id': 1,
            'query': 'Hello world!',
            'offset': 0,
            'limit': 20
        }

        self.session.session.get = Mock()
        self.session.session.get.return_value = FakeSearchMessagesGetResponse()

        response = search_messages(self.session, **query)
        self.session.session.get.assert_called_once_with(
            'https://fake-fln.com/api/messages/0.1/messages/search/',
            params=query,
            verify=True
        )
        self.assertEquals(len(response['messages']), 1)

    def test_get_threads(self):
        query = create_get_threads_object(
            threads=[1],
            threads_details=create_get_threads_details_object(
                message_count=1,
                user_details=True
            )
        )

        self.session.session.get = Mock()
        self.session.session.get.return_value = FakeGetThreadsGetResponse()

        response = get_threads(self.session, query)
        self.session.session.get.assert_called_once_with(
            'https://fake-fln.com/api/messages/0.1/threads/',
            params=query,
            verify=True
        )
        self.assertEquals(len(response['threads']), 1)
        self.assertEquals(response['threads'][0]['thread']['id'], 100)

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

    def test_post_attachment_fail(self):
        file_object = {}
        message_data = {
            'thread_id': 301,
            'attachments': [
                create_attachment(file_object, 'file.txt'),
            ],
        }

        response = FakeErrorResponse()

        self.session.session.post = Mock()
        self.session.session.post.return_value = \
            response

        with self.assertRaises(MessageNotCreatedException) as cm:
            post_attachment(self.session, **message_data)

        e = cm.exception
        self.assertEqual(str(e), response.json()['message'])
        self.assertEqual(e.request_id, response.json()['request_id'])
        self.assertEqual(e.error_code, response.json()['error_code'])
