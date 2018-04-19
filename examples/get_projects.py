from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import (
    get_projects, get_project_by_id
)
from freelancersdk.resources.projects.helpers import (
    create_get_projects_object, create_get_projects_project_details_object,
    create_get_projects_user_details_object
)
from freelancersdk.resources.projects.exceptions import \
    ProjectsNotFoundException
import os
import json


def sample_get_projects():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    query = create_get_projects_object(
        project_ids=[
            201,
            202,
            203,
        ],
        project_details=create_get_projects_project_details_object(
            full_description=True,
            jobs=True,
            qualifications=True,
        ),
        user_details=create_get_projects_user_details_object(
            basic=True,
            profile_description=True,
            reputation=True,
        ),
    )

    try:
        p = get_projects(session, query)
    except ProjectsNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return p

def sample_get_project_by_id():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    project_id = 15389177
    project_details = create_get_projects_project_details_object(
        full_description=True
    )
    user_details = create_get_projects_user_details_object(
        basic=True
    )

    try:
        p = get_project_by_id(session, project_id, project_details, user_details)
    except ProjectsNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return p


print('Getting multiple projects...')
p = sample_get_projects()
if p:
    print('Found projects: {}'.format(json.dumps(p)))
print('Getting a single project by ID...')

p = sample_get_project_by_id()
if p:
    print('Found a single project: {}'.format(json.dumps(p)))


