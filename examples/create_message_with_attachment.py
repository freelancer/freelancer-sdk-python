from freelancersdk.resources.messages.messages import post_attachment
from freelancersdk.session import Session
from freelancersdk.resources.messages.exceptions import \
    MessageNotCreatedException
from freelancersdk.resources.messages.helpers import create_attachment
import os


# https://developers.freelancer.com/docs/use-cases/messaging#header-sending-a-message
def sample_post_attachment():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    file1 = open('/path/to/text.txt', 'rb')
    file2 = open('/path/to/image.jpg', 'rb')
    file3 = open('/path/to/code.c', 'rb')
    thread_data = {
        'thread_id': 401,
        'attachments': [
            create_attachment(file1, 'description.txt'),
            create_attachment(file2, 'screenshot.jpg'),
            create_attachment(file3, 'source.c'),
        ]
    }
    ret = None

    try:
        t = post_attachment(session, **thread_data)
    except MessageNotCreatedException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        ret = None
    else:
        ret = t
    finally:
        file1.close()
        file2.close()
        file3.close()

    return ret


t = sample_post_attachment()
if t:
    print('Message created: {} (message_id={})'.format(t, t.id))
