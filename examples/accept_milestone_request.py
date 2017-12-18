from freelancersdk.resources.projects import accept_milestone_request
from freelancersdk.session import Session
from freelancersdk.exceptions import MilestoneRequestNotAcceptedException
import os


# https://developers.freelancer.com/docs/use-cases/milestone-request-actions
def sample_accept_milestone_request():

    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')

    session = Session(oauth_token=oauth_token, url=url)
    milestone_request_data = {
        'milestone_request_id': 1,
    }
    try:
        m = accept_milestone_request(session, **milestone_request_data)
    except MilestoneRequestNotAcceptedException as e:
        print(('Error message: %s' % e.message))
        print(('Server response: %s' % e.error_code))
        return None
    else:
        return m


m = sample_accept_milestone_request()
if m:
    print(("Milestone request accepted: %s" % m))
