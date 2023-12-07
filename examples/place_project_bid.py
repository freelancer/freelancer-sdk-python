from freelancersdk.resources.projects import place_project_bid
from freelancersdk.session import Session
from freelancersdk.resources.users \
    import get_self_user_id
from freelancersdk.exceptions import BidNotPlacedException
import os


# https://developers.freelancer.com/docs/projects/bids#bids-post
def sample_place_project_bid():

    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    project_id = os.environ.get('PROJECT_ID')

    session = Session(oauth_token=oauth_token, url=url)
    my_user_id = get_self_user_id(session)
    bid_data = {
        'project_id': int(project_id),
        'bidder_id': my_user_id,
        'amount': 10,
        'period': 2,
        'milestone_percentage': 100,
        'description': 'This is my bid',
    }
    try:
        return place_project_bid(session, **bid_data)
    except BidNotPlacedException as e:
        print(('Error message: %s' % e.message))
        print(('Error code: %s' % e.error_code))
        return None


b = sample_place_project_bid()
if b:
    print(("Bid placed: %s" % b))
