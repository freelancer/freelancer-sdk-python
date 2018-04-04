from freelancersdk.session import Session
from freelancersdk.resources.users.users import get_portfolios
from freelancersdk.resources.users.exceptions import \
    PortfoliosNotFoundException
import os

def sample_get_portfolios():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    user_ids = [ 7344704]
    # 3112780
    try:
        portfolios = get_portfolios(session, user_ids=user_ids)
    except PortfoliosNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server: response: {}'.format(e.error_code))
        return None
    else:
        return portfolios

result = sample_get_portfolios()

if result:
    portfolios = []
    users = result['users'].keys()
    for k in users:
        portfolios+=(result['portfolios'][k])
    print('Got {} portfolios from {} users.'.format(len(portfolios), len(users)))
    print('Portfolios:\n {}'.format(portfolios))
    