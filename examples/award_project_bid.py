from freelancersdk.session import Session
from freelancersdk.resources.projects import award_project_bid
from freelancersdk.exceptions import BidNotAwaredException
import os


# https://developers.freelancer.com/docs/use-cases/performing-a-bid-action
def sample_award_project_bid():
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    url = os.environ.get('FLN_URL')
    session = Session(oauth_token=oauth_token, url=url)

    bid_data = {
        'bid_id': 1
    }

    try:
        return award_project_bid(session, **bid_data)
    except BidNotAwaredException as e:
        print(('Error message: %s' % e.message))
        print(('Error code: %s' % e.error_code))
        return None


b = sample_award_project_bid()
if b:
    print(("Bid awarded: %s" % b))
