from freelancersdk.session import Session
from freelancersdk.resources.users.users import get_self
from freelancersdk.resources.users.exceptions import \
    SelfNotRetrievedException
from freelancersdk.resources.users.helpers import (
    create_get_users_details_object
)

import os


def sample_get_self():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)
    user_details = create_get_users_details_object(
        country=True,
        profile_description=True
    )
    try:
        result = get_self(session, user_details)
    except SelfNotRetrievedException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return result

result = sample_get_self()

if result:
    print('Found self user: {}'.format(result))