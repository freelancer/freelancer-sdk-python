from freelancersdk.session import Session
from freelancersdk.resources.users.users import get_users, get_user_by_id
from freelancersdk.resources.users.helpers import (
    create_get_users_object, create_get_users_details_object,
)
from freelancersdk.resources.users.exceptions import \
    UsersNotFoundException
import os
import json


def sample_get_users():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    query = create_get_users_object(
        user_ids=[
            110013,
            221202,
            231203,
        ],
        user_details=create_get_users_details_object(
            basic=True,
            profile_description=True,
            reputation=True,
        ),
    )

    try:
        p = get_users(session, query)
    except UsersNotFoundException as e:
        print(('Error message: {}'.format(e.message)))
        print(('Server response: {}'.format(e.error_code)))
        return None
    else:
        return p


def sample_get_user_by_id():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    try:
        p = get_user_by_id(session, 110013)
    except UserNotFoundException as e:
        print(('Error message: {}'.format(e.message)))
        print(('Server response: {}'.format(e.error_code)))
        return None
    else:
        return p


print("Getting a list of users...")
p = sample_get_users()
if p:
    print('Users found!\n{}'.format(json.dumps(p)))


print("Getting just a single user...")
p = sample_get_user_by_id()
if p:
    print('User found!\n{}'.format(json.dumps(p)))




