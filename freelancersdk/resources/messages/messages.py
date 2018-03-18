"""
This module contains functions for message operations
"""

from freelancersdk.resources.messages.types import (
    Thread, Message
)
from freelancersdk.resources.messages.helpers import (
    make_post_request, make_get_request
)
from freelancersdk.resources.messages.exceptions import (
    ThreadNotCreatedException, MessageNotCreatedException,
    MessagesNotFoundException, ThreadsNotFoundException
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


def get_messages(session, query, limit=10, offset=0):
    """
    Get one or more messages
    """
    query['limit'] = limit
    query['offset'] = offset
    
    # GET /api/messages/0.1/messages
    response = make_get_request(session, 'messages', params_data=query)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['result']
    else:
        raise MessagesNotFoundException(
            message=json_data['message'],
            error_code=json_data['error_code']
        )


def search_messages(session, thread_id, query, limit=20,
                    offset=0, message_context_details=None,
                    window_above=None, window_below=None):
    """
    Search for messages
    """
    query = {
        'thread_id': thread_id,
        'query': query,
        'limit': limit,
        'offset': offset
    }
    if message_context_details:
        query['message_context_details'] = message_context_details
    if window_above:
        query['window_above'] = window_above
    if window_below:
        query['window_below'] = window_below

    # GET /api/messages/0.1/messages/search
    response = make_get_request(session, 'messages/search', params_data=query)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['result']
    else:
        raise MessagesNotFoundException(
            message=json_data['message'],
            error_code=json_data['error_code']
        )


def get_threads(session, query):
    """
    Get one or more threads
    """
    # GET /api/messages/0.1/threads
    response = make_get_request(session, 'threads', params_data=query)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['result']
    else:
        raise ThreadsNotFoundException(
            message=json_data['message'],
            error_code=json_data['error_code']
        )
