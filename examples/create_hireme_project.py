from freelancersdk.session import Session
from freelancersdk.resources.projects \
    import (create_hireme_project,
            create_budget_object,
            create_currency_object,
            create_job_object,
            create_bid_object)
from freelancersdk.exceptions import ProjectNotCreatedException
import os


# https://www.freelancer.com/api/docs/cases/creating_a_project
def sample_create_hireme_project():
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    url = os.environ.get('FLN_URL')
    session = Session(oauth_token=oauth_token, url=url)

    project_data = {
        'title': 'My new hireme project',
        'description': 'description',
        'currency': create_currency_object(id=1),
        'budget': create_budget_object(minimum=10),
        'jobs': [create_job_object(id=7)],
        'hireme_initial_bid':
            create_bid_object(id=None,  # No bid id yet
                              bidder_id=2,  # Freelancer we want to hire
                              project_id=None,  # This project
                              retracted=None,
                              amount=100,
                              period=7,  # Days
                              description='Hello',
                              project_owner_id=1)
    }

    try:
        p = create_hireme_project(session, **project_data)
    except ProjectNotCreatedException as e:
        print(('Error message: %s' % e.message))
        print(('Error code: %s' % e.error_code))
        return None
    else:
        return p


p = sample_create_hireme_project()
if p:
    print(("Project created: %s" % p.url))
