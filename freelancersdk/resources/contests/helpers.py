# This module will contain helper functions/classes for contests

from freelancersdk.resources.contests import contests_endpoint
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


# Make API calls
# /api/contests/0.1/<specific_endpoint>
def make_post_request(session, endpoint, headers=None, params_data=None,
                      form_data=None, json_data=None, files=None):
    url = urljoin(session.url, '{}/{}/'.format(contests_endpoint, endpoint))
    return session.session.post(url=url, headers=headers, params=params_data,
                                data=form_data, json=json_data, files=files,
                                verify=True)
