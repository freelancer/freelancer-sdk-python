from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import get_milestone_by_id
from freelancersdk.resources.projects.exceptions import \
    MilestonesNotFoundException
from freelancersdk.resources.users.helpers import (
    create_get_users_details_object
)

import os


def sample_get_specific_milestone(milestone_id):
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)
    user_details = create_get_users_details_object(
        country=True,
        profile_description=True
    )
    try:
        milestone = get_milestone_by_id(session, milestone_id, user_details)
    except MilestonesNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return milestone


milestone_id = 15323050
result = sample_get_specific_milestone(milestone_id)

if result:
    print('Found milestone: {}'.format(result['milestones'][str(milestone_id)]))
