# This module will contain helper functions/classes for users
# Reference: https://www.freelancer.com/api/docs/structs/index

from freelancersdk.resources.users import users_endpoint
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

# Make API calls
# /api/users/0.1/<specific_endpoint>
def make_post_request(session, endpoint, json_data):
    return session.session.post(urljoin(session.url,
                                        '%s/%s/' % (users_endpoint, endpoint)),
                                json=json_data,
                                verify=True)
def make_get_request(session, endpoint):
    return session.session.get(urljoin(session.url,
                                       '%s/%s/' % (users_endpoint, endpoint)),
                               verify=True)
