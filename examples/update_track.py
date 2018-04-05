from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import update_track
from freelancersdk.resources.projects.exceptions import \
    TrackNotUpdatedException

import os


def sample_update_track(track_id, latitude, longitude, stop_tracking):
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    try:
        track = update_track(session, track_id, latitude, longitude, stop_tracking)
    except TrackNotUpdatedException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return track



track_id = 82
latitude = 14.5
longitude = 15.5
stop_tracking = False
result = sample_update_track(track_id, latitude, longitude, stop_tracking)

if result:
    print('Updated track number {}! Details: {}'.format(track_id, result))
