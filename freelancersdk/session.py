import requests

from freelancersdk.exceptions import AuthTokenNotSuppliedException


class Session():
    """
    This class will manage a HTTP session to the freelancer.com API
    """

    def __init__(self, oauth_token=None, url='https://www.freelancer.com'):
        if not oauth_token:
            raise AuthTokenNotSuppliedException('OAuth token not supplied')

        self.session = requests.Session()
        if url:
            self.url = url
        else:
            self.url = 'https://www.freelancer.com'

        # Set default headers
        default_headers = {'Freelancer-OAuth-V1': oauth_token,
                           'User-Agent': 'Freelancer.com SDK',
                           }
        self.session.headers.update(default_headers)
