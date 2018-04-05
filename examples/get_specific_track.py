from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import get_track_by_id
from freelancersdk.resources.projects.exceptions import \
    TrackNotFoundException

import os


def sample_get_track(track_id):
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    try:
        track = get_track_by_id(session, track_id)
    except TrackNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return track


track_id = 82
result = sample_get_track(track_id)

if result:
    print('Found a track: {}'.format(result))
