"""
This module contains functions for project operations
"""

import time

from freelancersdk.resources.projects.types import (
    Project, Bid, Milestone
)
from freelancersdk.resources.projects.exceptions import (
    ProjectNotCreatedException, BidNotPlacedException,
    MilestoneNotCreatedException,
)
from freelancersdk.resources.projects import (
    make_post_request,
)

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

def create_project(session, title, description,
                   currency, budget, jobs):
    """
    Create a project
    """
    project_data = {'title': title,
                    'description': description,
                    'currency': currency,
                    'budget': budget,
                    'jobs': jobs
                    }

    # POST /api/projects/0.1/projects/
    response = make_post_request(session, 'projects', json_data=project_data)
    json_data = response.json()
    if response.status_code == 200:
        project_data = json_data['result']
        p = Project(project_data)
        p.url = urljoin(session.url, 'projects/%s' % p.seo_url)
        return p
    else:
        raise ProjectNotCreatedException(message=json_data['message'],
                                         error_code=json_data['error_code'],
                                         )


def place_project_bid(session, project_id, bidder_id, description,
                      amount, period, milestone_percentage):
    """
    Place a bid on a project
    """
    bid_data = {'project_id': project_id,
                'bidder_id': bidder_id,
                'description': description,
                'amount': amount,
                'period': period,
                'milestone_percentage': milestone_percentage
                }
    # POST /api/projects/0.1/bids/
    response = make_post_request(session, 'bids', json_data=bid_data)
    json_data = response.json()
    if response.status_code == 200:
        bid_data = json_data['result']
        return Bid(bid_data)
    else:
        raise BidNotPlacedException(message=json_data['message'],
                                    error_code=json_data['error_code'],
                                    )

def create_milestone_payment(session, project_id, amount, bidder_id, description,
                             reason):
    """
    Create a milestone payment
    """
    milestone_data = {'project_id': project_id,
                      'bidder_id': bidder_id,
                      'description': description,
                      'amount': amount,
                      'reason': reason,
                     }
    session.session.headers['X-Freelancer-Time-V1'] = session.session.headers.get(
        'X-Freelancer-Time-V1', int(time.time()))
    # POST /api/projects/0.1/milestones/
    response = make_post_request(session, 'milestones', json_data=milestone_data)
    json_data = response.json()
    if response.status_code == 200:
        milestone_data = json_data['result']
        return Milestone(milestone_data)
    else:
        raise MilestoneNotCreatedException(message=json_data['message'],
                                           error_code=json_data['error_code'],
                                           )
