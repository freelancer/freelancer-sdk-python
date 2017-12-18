from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import search_projects
from freelancersdk.resources.projects.exceptions import \
    ProjectsNotFoundException
import os


def sample_search_projects():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    search_data = {
        'query': 'logo',
        'project_types': 'fixed',
        'limit': 10,
        'offset': 0,
        'active_only': True,
    }

    try:
        p = search_projects(session, **search_data)
    except ProjectsNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return p


p = sample_search_projects()
if p:
    print('Found projects: {}'.format(p('total_count')))
