from freelancersdk.resources.projects import cancel_milestone_payment
from freelancersdk.session import Session
from freelancersdk.exceptions import MilestoneNotCancelledException
import os


# https://developers.freelancer.com/docs/projects/milestones#milestones-put
def sample_cancel_milestone_payment():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')

    session = Session(oauth_token=oauth_token, url=url)
    milestone_data = {
        'milestone_id': 15295214,
    }
    try:
        m = cancel_milestone_payment(session, **milestone_data)
    except MilestoneNotCancelledException as e:
        print(('Error message: %s' % e.message))
        print(('Server response: %s' % e.error_code))
        return None
    else:
        return m


m = sample_cancel_milestone_payment()
if m:
    print(("Milestone requested release: %s" % m))
