import requests

from freelancersdk.exceptions import AuthTokenNotSuppliedException

class Session():
    """
    This class will manage a HTTP session to the freelancer.com API
    """

    def __init__(self, id=None, token=None, url='https://www.freelancer.com'):
        if not id or not token:
            raise AuthTokenNotSuppliedException('DeveloperID / Auth token not supplied')

        self.session = requests.Session()
        self.url = url

        # Set default headers
        default_headers = {'Freelancer-Developer-Auth-V1': '%s;%s' % (id, token),
                           'User-Agent': 'Freelancer.com SDK',
                           }
        self.session.headers.update(default_headers)
