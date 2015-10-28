from freelancersdk.resources.users import make_get_request
from freelancersdk.resources.users.exceptions import (
    UserIdNotRetrievedException)

def get_self_user_id(session):
    """
    Get the currently authenticated user ID
    """
    response = make_get_request(session, 'self')
    if response.status_code == 200:
        return response.json()['result']['id']
    else:
        raise UserIdNotRetrievedException(
            'Error retrieving user id: %s' % response.text, response.text)
