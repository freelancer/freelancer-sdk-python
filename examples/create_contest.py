from freelancersdk.resources.contests.contests import create_contest
from freelancersdk.session import Session
from freelancersdk.resources.contests.exceptions import \
    ContestNotCreatedException
import os


def sample_create_contest():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    contest_data = {
        'title': 'Design a logo',
        'description': 'I need a logo for my company',
        'type': 'freemium',
        'duration': 7,  # Days
        'job_ids': [
            1,
            2,
        ],
        'currency_id': 1,  # USD
        'prize': 100,
    }

    try:
        t = create_contest(session, **contest_data)
    except ContestNotCreatedException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return t


c = sample_create_contest()
if c:
    print('Contest created: {} (contest_id={})'.format(c, c.id))
