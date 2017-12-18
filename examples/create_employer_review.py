from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import post_review
from freelancersdk.resources.projects.helpers import \
    create_review_employer_object
from freelancersdk.resources.projects.exceptions import \
    ReviewNotPostedException
import os


def sample_post_review():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    review = create_review_employer_object(
        project_id=201,
        employer_id=101,
        freelancer_id=102,
        clarity_spec=5,
        communication=5,
        payment_prom=5,
        professionalism=5,
        work_for_again=5,
        comment='Thanks for all the fish'
    )

    try:
        r = post_review(session, review)
    except ReviewNotPostedException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return r


r = sample_post_review()
if r:
    print('Review created: {}'.format(r))
