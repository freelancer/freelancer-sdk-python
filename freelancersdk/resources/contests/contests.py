"""
This module contains functions for contest operations
"""

from freelancersdk.resources.contests.types import Contest
from freelancersdk.resources.contests.helpers import make_post_request
from freelancersdk.resources.contests.exceptions import \
    ContestNotCreatedException


def create_contest(session, title, description, type, duration, job_ids, currency_id,
                   prize):
    """
    Create a contest
    """
    contest_data = {
        'title': title,
        'description': description,
        'type': type,
        'duration': duration,
        'job_ids': job_ids,
        'currency_id': currency_id,
        'prize': prize,
    }

    # POST /api/contests/0.1/contests/
    response = make_post_request(session, 'contests', json_data=contest_data)
    json_data = response.json()
    if response.status_code == 200:
        return Contest(json_data['result'])
    else:
        raise ContestNotCreatedException(message=json_data['message'],
                                         error_code=json_data['error_code'])
