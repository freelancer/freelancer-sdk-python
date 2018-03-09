# This module will contain helper functions/classes for messages

from freelancersdk.resources.messages import messages_endpoint
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


# Make API calls
# /api/messages/0.1/<specific_endpoint>
def make_post_request(session, endpoint, headers=None, params_data=None,
                      form_data=None, json_data=None, files=None):
    url = urljoin(session.url, '{}/{}/'.format(messages_endpoint, endpoint))
    return session.session.post(url=url, headers=headers, params=params_data,
                                data=form_data, json=json_data, files=files,
                                verify=True)


def make_get_request(session, endpoint, params_data=None):
    url = urljoin(session.url, '{}/{}/'.format(messages_endpoint, endpoint))
    return session.session.get(url, params=params_data, verify=True)


# Helper functions for creating various objects
def create_attachment(file_object, file_name):
    a = {
        'file': ('files[]', (file_name, file_object)),
        'filename': file_name,
    }
    return a


def create_get_messages_object(threads=[], senders=[], messages=[], contexts=[],
                context_type=None,is_read=None, from_updated_time=None,
                to_updated_time=None,count=None, user_details=None,
                thread_details=None):

    m = {}

    if threads:
        m['threads[]'] = threads
    if senders:
        m['senders[]'] = senders
    if messages:
        m['messages'] = messages
    if contexts:
        m['contexts[]'] = contexts
    if context_type:
        m['context_type'] = context_type
    if is_read:
        m['is_read'] = is_read
    if from_updated_time:
        m['from_updated_time'] = from_updated_time
    if to_updated_time:
        m['to_updated_time'] = to_updated_time
    if count:
        m['count'] = count
    if user_details:
        m['user_details'] = user_details
    if thread_details:
        m['thread_details'] = thread_details
    
    return m


def create_get_threads_object(threads=[], folders=[], contexts=[], 
                members=[], owners=[], thread_types=[],
                is_read=None, is_muted=None, from_updated_time=None,
                to_updated_time=None, count=None,
                context_type=None, threads_details=None):
    t = {}
    if threads:
        t['threads[]'] = threads
    if folders:
        t['folders[]'] = folders
    if contexts:
        t['contexts[]'] = contexts
    if members:
        t['members[]'] = members
    if owners:
        t['owners[]'] = owners
    if thread_types:
        t['thread_types[]'] = thread_types
    if context_type:
        t['context_type'] = context_type
    if is_read:
        t['is_read'] = is_read
    if is_muted:
        t['is_muted'] = is_muted
    if from_updated_time:
        t['from_updated_time'] = from_updated_time
    if to_updated_time:
        t['to_updated_time'] = to_updated_time
    if count:
        t['count'] = count
    if threads_details:
        t.update(threads_details)
    
    return t


def create_get_threads_details_object(message_count=None, unread_count=None,
                                 last_message=None, unread_thread_count=None,
                                 user_details=None, context_details=None,
                                 thread_attachments=None):
    t = {}
    if message_count:
        t.update(message_count=message_count)
    if unread_count:
        t.update(unread_count=unread_count)
    if last_message:
        t.update(last_message=last_message)
    if unread_thread_count:
        t.update(unread_thread_count=unread_thread_count)
    if user_details:
        t.update(user_details=user_details)
    if context_details:
        t.update(context_details=context_details)
    if thread_attachments:
        t.update(thread_attachments=thread_attachments)
    
    return t
