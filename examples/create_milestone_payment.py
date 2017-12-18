from freelancersdk.resources.projects import create_milestone_payment
from freelancersdk.resources.projects.types import MilestoneReason
from freelancersdk.session import Session
from freelancersdk.exceptions import MilestoneNotCreatedException
import os


# https://www.freelancer.com/api/docs/cases/creating_a_milestone
def sample_create_milestone_payment():

    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')

    project_id = os.environ.get('PROJECT_ID')
    bidder_id = os.environ.get('BIDDER_ID')

    session = Session(oauth_token=oauth_token, url=url)
    milestone_data = {
        'project_id': int(project_id),
        'bidder_id': int(bidder_id),
        'amount': 10,
        'reason': MilestoneReason.PARTIAL_PAYMENT.value,
        'description': 'This is a milestone',
    }
    try:
        m = create_milestone_payment(session, **milestone_data)
    except MilestoneNotCreatedException as e:
        print(('Error message: %s' % e.message))
        print(('Server response: %s' % e.error_code))
        return None
    else:
        return m


m = sample_create_milestone_payment()
if m:
    print(("Milestone created: %s" % m))
