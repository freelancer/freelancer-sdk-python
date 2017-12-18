from freelancersdk.resources.users import set_user_jobs
from freelancersdk.session import Session
from freelancersdk.exceptions import UserJobsNotSetException
import os


def sample_set_user_jobs():

    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')

    session = Session(oauth_token=oauth_token, url=url)
    user_jobs_data = {
        'job_ids': [
            1,
            2,
            3
        ]
    }
    try:
        m = set_user_jobs(session, **user_jobs_data)
    except UserJobsNotSetException as e:
        print(('Error message: %s' % e.message))
        print(('Server response: %s' % e.error_code))
        return None
    else:
        return m


m = sample_set_user_jobs()
if m:
    print(("User jobs set: %s" % m))
