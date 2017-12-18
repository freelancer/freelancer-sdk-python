from freelancersdk.resources.messages.messages import post_message
from freelancersdk.session import Session
from freelancersdk.resources.messages.exceptions import \
    MessageNotCreatedException
import os


# https://developers.freelancer.com/docs/use-cases/messaging#header-sending-a-message
def sample_post_message():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    thread_data = {
        'thread_id': 401,
        'message': "Let's talk",
    }

    try:
        t = post_message(session, **thread_data)
    except MessageNotCreatedException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return t


t = sample_post_message()
if t:
    print('Message created: {} (message_id={})'.format(t, t.id))
