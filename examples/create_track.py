from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import post_track
from freelancersdk.resources.projects.exceptions import \
    TrackNotCreatedException

import os


def sample_create_track(user_id, project_id, latitude, longitude):
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    try:
        track = post_track(session, user_id, project_id, latitude, longitude)
    except TrackNotCreatedException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return track



user_id = 7344704
project_id = 15387836
latitude = 14.5
longitude = 15.5
result = sample_create_track(user_id, project_id, latitude, longitude)

if result:
    print('Created a new track! Details: {}'.format(result))
