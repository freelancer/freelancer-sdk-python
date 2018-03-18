from freelancersdk.session import Session
from freelancersdk.resources.messages.messages import get_threads
from freelancersdk.resources.messages.exceptions import \
    ThreadsNotFoundException
from freelancersdk.resources.messages.helpers import (
    create_get_threads_object, create_get_threads_details_object
)
import os


def sample_get_threads():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    get_threads_data = create_get_threads_object(
        threads=80034553,
        is_read=True,
        threads_details = create_get_threads_details_object(
            last_message=True,
            user_details=True
        )
    )

    try:
        threads = get_threads(session, get_threads_data)
    except ThreadsNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return threads


result = sample_get_threads()

if result:
    print('Found threads: {}'.format(len(result['threads'])))