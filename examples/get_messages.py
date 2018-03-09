from freelancersdk.session import Session
from freelancersdk.resources.messages.messages import get_messages
from freelancersdk.resources.messages.exceptions import \
    MessagesNotFoundException
import os

def sample_get_messages():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    get_messages_data = {
        'threads': [
            80034553,
            102,
        ],
        'limit': 10,
        'offset': 0,
    }

    try:
        messages = get_messages(session, **get_messages_data)
    except MessagesNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server: response: {}'.format(e.error_code))
        return None
    else:
        return messages

result = sample_get_messages()

if result:
    print('Found messages: {}'.format(len(result['messages'])))
