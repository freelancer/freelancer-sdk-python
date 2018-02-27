from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import get_milestones
from freelancersdk.resources.projects.exceptions import \
    MilestoneNotFoundException
import os


def sample_get_milestones():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    get_milestones_data = {
        'project_ids' : [
            101,
            102,
        ],
        'limit': 10,
        'offset': 0,
    }

    try:
        milestones = get_milestones(session, **get_milestones_data)
    except MilestoneNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return milestones
