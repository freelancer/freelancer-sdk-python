"""
This module contains functions for project operations
"""

from freelancersdk.resources.projects.types import (
    Project, Bid, Milestone, MilestoneRequest
)
from freelancersdk.resources.projects.exceptions import (
    ProjectNotCreatedException, ProjectsNotFoundException,
    BidNotPlacedException, BidsNotFoundException, BidNotAwardedException,
    BidNotRevokedException, BidNotAcceptedException, BidNotRetractedException,
    BidNotHighlightedException,
    MilestoneNotCreatedException, MilestoneNotReleasedException,
    MilestoneNotRequestedReleaseException, MilestoneNotCancelledException,
    MilestoneRequestNotCreatedException, MilestoneRequestNotAcceptedException,
    MilestoneRequestNotRejectedException, MilestoneRequestNotDeletedException,
    MilestonesNotFoundException,
    ReviewNotPostedException,
    JobsNotFoundException
)

from freelancersdk.resources.projects.helpers import (
    create_get_projects_user_details_object
)
from freelancersdk.resources.projects import (
    make_get_request, make_post_request, make_put_request,
)

from freelancersdk.resources.projects import (
    create_job_object,
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


def create_hourly_project(session, title, description,
                          currency, budget, jobs, hourly_project_info):
    """
    Create a fixed project
    """
    project_data = {'title': title,
                    'description': description,
                    'currency': currency,
                    'budget': budget,
                    'jobs': jobs,
                    'type': 'HOURLY',
                    'hourly_project_info': hourly_project_info
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


def create_local_project(session, title, description,
                         currency, budget, jobs, location):
    """
    Create a fixed project
    """
    project_data = {'title': title,
                    'description': description,
                    'currency': currency,
                    'budget': budget,
                    'jobs': jobs,
                    'local': True,
                    'location': location
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


def create_hireme_project(session, title, description,
                          currency, budget, jobs, hireme_initial_bid):
    """
    Create a fixed project
    """
    jobs.append(create_job_object(id=417))  # Hire Me job, required

    project_data = {'title': title,
                    'description': description,
                    'currency': currency,
                    'budget': budget,
                    'jobs': jobs,
                    'hireme': True,
                    'hireme_initial_bid': hireme_initial_bid
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


def get_projects(session, query):
    """
    Get one or more projects
    """
    # GET /api/projects/0.1/projects
    response = make_get_request(session, 'projects', params_data=query)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['result']
    else:
        raise ProjectsNotFoundException(
            message=json_data['message'], error_code=json_data['error_code'])


def search_projects(session, query, project_types, limit, offset,
                    active_only=None):
    """
    Search for all projects
    """
    search_data = {
        'query': query,
        'project_types': project_types,
        'limit': limit,
        'offset': offset,
    }
    # GET /api/projects/0.1/projects/all/
    # GET /api/projects/0.1/projects/active/
    endpoint = 'projects/{}'.format('active' if active_only else 'all')
    response = make_get_request(session, endpoint, params_data=search_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['result']
    else:
        raise ProjectsNotFoundException(
            message=json_data['message'], error_code=json_data['error_code'])


def place_project_bid(session, project_id, bidder_id, description, amount,
                      period, milestone_percentage):
    """
    Place a bid on a project
    """
    bid_data = {
        'project_id': project_id,
        'bidder_id': bidder_id,
        'description': description,
        'amount': amount,
        'period': period,
        'milestone_percentage': milestone_percentage,
    }
    # POST /api/projects/0.1/bids/
    response = make_post_request(session, 'bids', json_data=bid_data)
    json_data = response.json()
    if response.status_code == 200:
        bid_data = json_data['result']
        return Bid(bid_data)
    else:
        raise BidNotPlacedException(message=json_data['message'],
                                    error_code=json_data['error_code'])


def get_bids(session, project_ids=[], bid_ids=[], limit=10, offset=0):
    """
    Get the list of bids
    """
    get_bids_data = {}
    if bid_ids:
        get_bids_data['bids[]'] = bid_ids
    if project_ids:
        get_bids_data['projects[]'] = project_ids
    get_bids_data['limit'] = limit
    get_bids_data['offset'] = offset
    # GET /api/projects/0.1/bids/
    response = make_get_request(session, 'bids', params_data=get_bids_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['result']
    else:
        raise BidsNotFoundException(
            message=json_data['message'], error_code=json_data['error_code']
        )


def get_milestones(session, project_ids=[], milestone_ids=[], user_details=None, limit=10, offset=0):
    """
    Get the list of milestones
    """
    get_milestones_data = {}
    if milestone_ids:
        get_milestones_data['milestones[]'] = milestone_ids
    if project_ids:
        get_milestones_data['projects[]'] = project_ids
    get_milestones_data['limit'] = limit
    get_milestones_data['offset'] = offset

    # Add projections if they exist
    if user_details:
        get_milestones_data.update(user_details)

    # GET /api/projects/0.1/milestones/

    response = make_get_request(session, 'milestones', params_data=get_milestones_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['result']
    else:
        raise MilestonesNotFoundException(
            message=json_data['message'], error_code=json_data['error_code']
        )


def get_milestone_by_id(session, milestone_id, user_details=None):
    """
    Get a specific milestone
    """
    # GET /api/projects/0.1/milestones/{milestone_id}/
    endpoint = 'milestones/{}'.format(milestone_id)

    response = make_get_request(session, endpoint, params_data=user_details)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['result']
    else:
        raise MilestonesNotFoundException(
            message=json_data['message'], error_code=json_data['error_code']
        )


def award_project_bid(session, bid_id):
    """
    Award a bid on a project
    """
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    bid_data = {
        'action': 'award'
    }
    # POST /api/projects/0.1/bids/{bid_id}/?action=award
    endpoint = 'bids/{}'.format(bid_id)
    response = make_put_request(session, endpoint, headers=headers,
                                params_data=bid_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['status']
    else:
        json_data = response.json()
        raise BidNotAwardedException(
            message=json_data['message'],
            error_code=json_data['error_code']
        )


def revoke_project_bid(session, bid_id):
    """
    Revoke a bid on a project
    """
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    bid_data = {
        'action': 'revoke'
    }
    # POST /api/projects/0.1/bids/{bid_id}/?action=revoke
    endpoint = 'bids/{}'.format(bid_id)
    response = make_put_request(session, endpoint, headers=headers,
                                params_data=bid_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['status']
    else:
        json_data = response.json()
        raise BidNotRevokedException(message=json_data['message'],
                                     error_code=json_data['error_code'])


def accept_project_bid(session, bid_id):
    """
    Accept a bid on a project
    """
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    bid_data = {
        'action': 'accept'
    }
    # POST /api/projects/0.1/bids/{bid_id}/?action=revoke
    endpoint = 'bids/{}'.format(bid_id)
    response = make_put_request(session, endpoint, headers=headers,
                                params_data=bid_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['status']
    else:
        json_data = response.json()
        raise BidNotAcceptedException(message=json_data['message'],
                                      error_code=json_data['error_code'])


def retract_project_bid(session, bid_id):
    """
    Retract a bid on a project
    """
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    bid_data = {
        'action': 'retract'
    }
    # POST /api/projects/0.1/bids/{bid_id}/?action=revoke
    endpoint = 'bids/{}'.format(bid_id)
    response = make_put_request(session, endpoint, headers=headers,
                                params_data=bid_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['status']
    else:
        json_data = response.json()
        raise BidNotRetractedException(message=json_data['message'],
                                       error_code=json_data['error_code'])


def highlight_project_bid(session, bid_id):
    """
    Highlight a bid on a project
    """
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    bid_data = {
        'action': 'highlight'
    }
    # POST /api/projects/0.1/bids/{bid_id}/?action=revoke
    endpoint = 'bids/{}'.format(bid_id)
    response = make_put_request(session, endpoint, headers=headers,
                                params_data=bid_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['status']
    else:
        json_data = response.json()
        raise BidNotHighlightedException(message=json_data['message'],
                                         error_code=json_data['error_code'])


def create_milestone_payment(session, project_id, bidder_id, amount,
                             reason, description):
    """
    Create a milestone payment
    """
    milestone_data = {
        'project_id': project_id,
        'bidder_id': bidder_id,
        'amount': amount,
        'reason': reason,
        'description': description
    }
    # POST /api/projects/0.1/milestones/
    response = make_post_request(session, 'milestones',
                                 json_data=milestone_data)
    json_data = response.json()
    if response.status_code == 200:
        milestone_data = json_data['result']
        return Milestone(milestone_data)
    else:
        raise MilestoneNotCreatedException(message=json_data['message'],
                                           error_code=json_data['error_code'])


def release_milestone_payment(session, milestone_id, amount):
    """
    Release a milestone payment
    """
    params_data = {
        'action': 'release',
    }
    milestone_data = {
        'amount': amount,
    }
    # PUT /api/projects/0.1/milestones/{milestone_id}/?action=release
    endpoint = 'milestones/{}'.format(milestone_id)
    response = make_put_request(session, endpoint, params_data=params_data,
                                json_data=milestone_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['status']
    else:
        raise MilestoneNotReleasedException(message=json_data['message'],
                                            error_code=json_data['error_code'])


def request_release_milestone_payment(session, milestone_id):
    """
    Release a milestone payment
    """
    params_data = {
        'action': 'request_release',
    }
    # PUT /api/projects/0.1/milestones/{milestone_id}/?action=release
    endpoint = 'milestones/{}'.format(milestone_id)
    response = make_put_request(session, endpoint, params_data=params_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['status']
    else:
        raise MilestoneNotRequestedReleaseException(
            message=json_data['message'], error_code=json_data['error_code'])


def cancel_milestone_payment(session, milestone_id):
    """
    Release a milestone payment
    """
    params_data = {
        'action': 'cancel',
    }
    # PUT /api/projects/0.1/milestones/{milestone_id}/?action=release
    endpoint = 'milestones/{}'.format(milestone_id)
    response = make_put_request(session, endpoint, params_data=params_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['status']
    else:
        raise MilestoneNotCancelledException(
            message=json_data['message'], error_code=json_data['error_code'])


def create_milestone_request(session, project_id, bid_id, description, amount):
    """
    Create a milestone request
    """
    milestone_request_data = {
        'project_id': project_id,
        'bid_id': bid_id,
        'description': description,
        'amount': amount,
    }
    # POST /api/projects/0.1/milestone_requests/
    response = make_post_request(session, 'milestone_requests',
                                 json_data=milestone_request_data)
    json_data = response.json()
    if response.status_code == 200:
        milestone_request_data = json_data['result']
        return MilestoneRequest(milestone_request_data)
    else:
        raise MilestoneRequestNotCreatedException(
            message=json_data['message'], error_code=json_data['error_code'])


def accept_milestone_request(session, milestone_request_id):
    """
    Accept a milestone request
    """
    params_data = {
        'action': 'accept',
    }
    # POST /api/projects/0.1/milestone_requests/{milestone_request_id}/?action=
    # accept
    endpoint = 'milestone_requests/{}'.format(milestone_request_id)
    response = make_put_request(session, endpoint, params_data=params_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['status']
    else:
        raise MilestoneRequestNotAcceptedException(
            message=json_data['message'], error_code=json_data['error_code'])


def reject_milestone_request(session, milestone_request_id):
    """
    Reject a milestone request
    """
    params_data = {
        'action': 'reject',
    }
    # POST /api/projects/0.1/milestone_requests/{milestone_request_id}/?action=
    # reject
    endpoint = 'milestone_requests/{}'.format(milestone_request_id)
    response = make_put_request(session, endpoint, params_data=params_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['status']
    else:
        raise MilestoneRequestNotRejectedException(
            message=json_data['message'], error_code=json_data['error_code'])


def delete_milestone_request(session, milestone_request_id):
    """
    Delete a milestone request
    """
    params_data = {
        'action': 'delete',
    }
    # POST /api/projects/0.1/milestone_requests/{milestone_request_id}/?action=
    # delete
    endpoint = 'milestone_requests/{}'.format(milestone_request_id)
    response = make_put_request(session, endpoint, params_data=params_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['status']
    else:
        raise MilestoneRequestNotDeletedException(
            message=json_data['message'], error_code=json_data['error_code'])


def post_review(session, review):
    """
    Post a review
    """
    # POST /api/projects/0.1/reviews/
    response = make_post_request(session, 'reviews', json_data=review)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['status']
    else:
        raise ReviewNotPostedException(
            message=json_data['message'], error_code=json_data['error_code'])


def get_jobs(session, job_ids, seo_details, lang):
    """
    Get a list of jobs
    """
    get_jobs_data = {
        'jobs[]': job_ids,
        'seo_details': seo_details,
        'lang': lang,
    }
    # GET /api/projects/0.1/jobs/
    response = make_get_request(session, 'jobs', params_data=get_jobs_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['result']
    else:
        raise JobsNotFoundException(
            message=json_data['message'], error_code=json_data['error_code'])
