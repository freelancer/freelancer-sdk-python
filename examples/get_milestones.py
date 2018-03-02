from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import get_milestones
from freelancersdk.resources.projects.exceptions import \
    MilestonesNotFoundException
from freelancersdk.resources.users.helpers import (
    create_get_users_details_object
)
import os


def sample_get_milestones():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    get_milestones_data = {
        'project_ids': [
            101,
            102,
        ],
        'limit': 10,
        'offset': 0,
        'user_details': create_get_users_details_object(
            country=True,
            profile_description=True
        )
    }

    try:
        milestones = get_milestones(session, **get_milestones_data)
    except MilestonesNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return milestones


result = sample_get_milestones()

if result:
    print('Found milestones: {}'.format(len(result['milestones'])))
