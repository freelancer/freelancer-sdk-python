from freelancersdk.resources.users import add_user_jobs
from freelancersdk.session import Session
from freelancersdk.exceptions import UserJobsNotAddedException
import os


def sample_add_user_jobs():

    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')

    session = Session(oauth_token=oauth_token, url=url)
    user_jobs_data = {
        'job_ids': [
            20, 32
        ]
    }
    try:
        m = add_user_jobs(session, **user_jobs_data)
    except UserJobsNotAddedException as e:
        print(('Error message: %s' % e.message))
        print(('Server response: %s' % e.error_code))
        return None
    else:
        return m


m = sample_add_user_jobs()
if m:
    print(("User jobs added: %s" % m))
