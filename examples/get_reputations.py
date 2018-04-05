from freelancersdk.session import Session
from freelancersdk.resources.users.users import get_reputations
from freelancersdk.resources.users.exceptions import \
    ReputationsNotFoundException
import os

def sample_get_reputations():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    user_ids = [3112780, 7344704]
    role = 'employer'
    reputation_details = {
        'job_history': True,
        'project_stats': True,
        'rehire_rates': True
    }

    try:
        reputations = get_reputations(session, user_ids=user_ids, 
                                     role=role,
                                     reputation_details=reputation_details)
    except ReputationsNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server: response: {}'.format(e.error_code))
        return None
    else:
        return reputations

result = sample_get_reputations()

if result:
    print('Found reputations: {}'.format(len(result)))
