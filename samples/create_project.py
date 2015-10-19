from freelancersdk.session import Session
from freelancersdk.resources.projects \
    import (create_project,
            create_budget_object,
            create_currency_object,
            create_job_object)
from freelancersdk.exceptions import ProjectNotCreatedException
import os

# https://www.freelancer.com/api/docs/cases/creating_a_project
def sample_create_project():
    id = os.environ['FLN_DEVELOPER_ID']
    token = os.environ['FLN_DEVELOPER_TOKEN']
    url = os.environ['FLN_URL']
    session = Session(id=id, token=token, url=url)

    project_data = {
        'title': 'My new project',
        'description': 'description',
        'currency': create_currency_object(id=1),
        'budget': create_budget_object(minimum=10),
        'jobs': [create_job_object(id=7)],
    }

    try:
        p = create_project(session, **project_data)
    except ProjectNotCreatedException as e:
        print('Error message: %s' % e.message)
        print('Error code: %s' % e.error_code)
        return None
    else:
        return p

p = sample_create_project()
if p:
    print("Project created: %s" % p.url)
