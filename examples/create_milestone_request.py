from freelancersdk.resources.projects import create_milestone_request
from freelancersdk.session import Session
from freelancersdk.exceptions import MilestoneRequestNotCreatedException
import os


# https://developers.freelancer.com/docs/use-cases/requesting-a-milestone
def sample_create_milestone_request():

    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')

    session = Session(oauth_token=oauth_token, url=url)
    milestone_request_data = {
        'project_id': 1,
        'bid_id': 1,
        'description': 'This is a milestone request',
        'amount': 10,
    }
    try:
        m = create_milestone_request(session, **milestone_request_data)
    except MilestoneRequestNotCreatedException as e:
        print(('Error message: %s' % e.message))
        print(('Server response: %s' % e.error_code))
        return None
    else:
        return m


m = sample_create_milestone_request()
if m:
    print(("Milestone request created: %s" % m))
