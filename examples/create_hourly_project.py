from freelancersdk.session import Session
from freelancersdk.resources.projects \
    import (create_hourly_project,
            create_budget_object,
            create_currency_object,
            create_job_object,
            create_hourly_project_info_object)
from freelancersdk.exceptions import ProjectNotCreatedException
import os


# https://www.freelancer.com/api/docs/cases/creating_a_project
def sample_create_hourly_project():
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    url = os.environ.get('FLN_URL')
    session = Session(oauth_token=oauth_token, url=url)

    project_data = {
        'title': 'My new hourly project',
        'description': 'description',
        'currency': create_currency_object(id=1),
        'budget': create_budget_object(minimum=10),
        'jobs': [create_job_object(id=7)],
        'hourly_project_info':
            create_hourly_project_info_object(40, 'WEEK', 'ONE_TO_FOUR_WEEKS')
    }

    try:
        p = create_hourly_project(session, **project_data)
    except ProjectNotCreatedException as e:
        print(('Error message: %s' % e.message))
        print(('Error code: %s' % e.error_code))
        return None
    else:
        return p


p = sample_create_hourly_project()
if p:
    print(("Project created: %s" % p.url))
