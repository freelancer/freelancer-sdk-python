"""
This module contains functions for message operations
"""

from freelancersdk.resources.messages.types import (
    Thread, Message
)
from freelancersdk.resources.messages.helpers import make_post_request
from freelancersdk.resources.messages.exceptions import (
    ThreadNotCreatedException, MessageNotCreatedException
)


def create_thread(session, member_ids, context_type, context, message):
    """
    Create a thread
    """
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    thread_data = {
        'members[]': member_ids,
        'context_type': context_type,
        'context': context,
        'message': message,
    }

    # POST /api/messages/0.1/threads/
    response = make_post_request(session, 'threads', headers,
                                 form_data=thread_data)
    json_data = response.json()
    if response.status_code == 200:
        return Thread(json_data['result'])
    else:
        raise ThreadNotCreatedException(message=json_data['message'],
                                        error_code=json_data['error_code'])


def create_project_thread(session, member_ids, project_id, message):
    """
    Create a project thread
    """
    return create_thread(session, member_ids, 'project', project_id, message)


def post_message(session, thread_id, message):
    """
    Add a message to a thread
    """
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    message_data = {
        'message': message,
    }

    # POST /api/messages/0.1/threads/{thread_id}/messages/
    endpoint = 'threads/{}/messages'.format(thread_id)
    response = make_post_request(session, endpoint, headers,
                                 form_data=message_data)
    json_data = response.json()
    if response.status_code == 200:
        return Message(json_data['result'])
    else:
        raise MessageNotCreatedException(message=json_data['message'],
                                         error_code=json_data['error_code'])


def post_attachment(session, thread_id, attachments):
    """
    Add a message to a thread
    """
    files = []
    filenames = []
    for attachment in attachments:
        files.append(attachment['file'])
        filenames.append(attachment['filename'])
    message_data = {
        'attachments[]': filenames,
    }

    # POST /api/messages/0.1/threads/{thread_id}/messages/
    endpoint = 'threads/{}/messages'.format(thread_id)
    response = make_post_request(session, endpoint,
                                 form_data=message_data, files=files)
    json_data = response.json()
    if response.status_code == 200:
        return Message(json_data['result'])
    else:
        raise MessageNotCreatedException(message=json_data['message'],
                                         error_code=json_data['error_code'])
