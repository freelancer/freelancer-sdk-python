from freelancersdk.session import Session
from freelancersdk.resources.projects \
    import (create_local_project,
            create_budget_object,
            create_currency_object,
            create_job_object,
            create_location_object,
            create_country_object)
from freelancersdk.exceptions import ProjectNotCreatedException
import os


# https://www.freelancer.com/api/docs/cases/creating_a_project
def sample_create_local_project():
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    url = os.environ.get('FLN_URL')
    session = Session(oauth_token=oauth_token, url=url)

    project_data = {
        'title': 'My new local project',
        'description': 'description',
        'currency': create_currency_object(id=1),
        'budget': create_budget_object(minimum=10),
        'jobs': (create_job_object(id=649)),  # Must be a local job
        'location': create_location_object(create_country_object('Australia'),
                                           'Sydney', -33.875461, 151.201678)
    }

    try:
        p = create_local_project(session, **project_data)
    except ProjectNotCreatedException as e:
        print(('Error message: %s' % e.message))
        print(('Error code: %s' % e.error_code))
        return None
    else:
        return p


p = sample_create_local_project()
if p:
    print(("Project created: %s" % p.url))
