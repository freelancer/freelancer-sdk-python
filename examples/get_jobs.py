from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import get_jobs
from freelancersdk.resources.projects.exceptions import \
    JobsNotFoundException
import os


def sample_get_jobs():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    get_jobs_data = {
        'job_ids': [
            20,
            32,
        ],
        'seo_details': True,
        'lang': 'en',
    }

    try:
        j = get_jobs(session, **get_jobs_data)
    except JobsNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return j


j = sample_get_jobs()
if j:
    print('Found jobs: {}'.format(len(j)))
