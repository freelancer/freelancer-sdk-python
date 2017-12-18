from freelancersdk.resources.messages.messages import create_project_thread
from freelancersdk.session import Session
from freelancersdk.resources.messages.exceptions import \
    ThreadNotCreatedException
import os


# https://developers.freelancer.com/docs/use-cases/messaging#header-creating-a-thread
def sample_create_project_thread():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    thread_data = {
        'member_ids': [
            102,
        ],
        'project_id': 301,
        'message': "Let's talk",
    }

    try:
        t = create_project_thread(session, **thread_data)
    except ThreadNotCreatedException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return t


t = sample_create_project_thread()
if t:
    print('Project message thread created: {} (thread_id={})'.format(t, t.id))
