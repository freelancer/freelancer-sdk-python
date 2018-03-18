from freelancersdk.session import Session
from freelancersdk.resources.messages.messages import search_messages
from freelancersdk.resources.messages.exceptions import \
    MessagesNotFoundException
import os

def sample_search_messages():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    thread_id = 80034553
    query = "hello"

    try:
        messages = search_messages(session, thread_id, query)
    except MessagesNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server: response: {}'.format(e.error_code))
        return None
    else:
        return messages

result = sample_search_messages()

if result:
    print('Found messages: {}'.format(len(result['messages'])))