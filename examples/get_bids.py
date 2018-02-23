from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import get_bids
from freelancersdk.resources.projects.exceptions import \
    BidsNotFoundException
import os


def sample_get_bids():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    get_bids_data = {
        'project_ids': [
            101,
            102,
        ],
        'limit': 10,
        'offset': 0,
    }

    try:
        b = get_bids(session, **get_bids_data)
    except BidsNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return b


b = sample_get_bids()
if b:
    print('Found bids: {}'.format(len(b['bids'])))
