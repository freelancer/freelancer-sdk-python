from freelancersdk.resources.users import (
    make_get_request, make_post_request, make_put_request, make_delete_request)
from freelancersdk.resources.users.exceptions import (
    UserIdNotRetrievedException,
    UserJobsNotAddedException, UserJobsNotSetException,
    UserJobsNotDeletedException, UsersNotFoundException,
    SelfNotRetrievedException, UserNotFoundException,
    ReputationsNotFoundException, PortfoliosNotFoundException
)


def get_self(session, user_details=None):
    """
    Get details about the currently authenticated user
    """
    # Set compact to true
    if user_details:
        user_details['compact'] = True
    response = make_get_request(session, 'self', params_data=user_details)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['result']
    else:
        raise SelfNotRetrievedException(
            message=json_data['message'],
            error_code=json_data['error_code'],
            request_id=json_data['request_id']
        )


def get_user_by_id(session, user_id, user_details=None):
    """
    Get details about specific user
    """
    if user_details:
        user_details['compact'] = True
    response = make_get_request(
        session, 'users/{}'.format(user_id), params_data=user_details)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['result']
    else:
        raise UserNotFoundException(
            message=json_data['message'],
            error_code=json_data['error_code'],
            request_id=json_data['request_id']
        )


def get_self_user_id(session):
    """
    Get the currently authenticated user ID
    """
    response = make_get_request(session, 'self')
    if response.status_code == 200:
        return response.json()['result']['id']
    else:
        raise UserIdNotRetrievedException(
            'Error retrieving user id: %s' % response.text, response.text)


def add_user_jobs(session, job_ids):
    """
    Add a list of jobs to the currently authenticated user
    """
    jobs_data = {
        'jobs[]': job_ids
    }
    response = make_post_request(session, 'self/jobs', json_data=jobs_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['status']
    else:
        raise UserJobsNotAddedException(
            message=json_data['message'],
            error_code=json_data['error_code'],
            request_id=json_data['request_id'])


def set_user_jobs(session, job_ids):
    """
    Replace the currently authenticated user's list of jobs with a new list of
    jobs
    """
    jobs_data = {
        'jobs[]': job_ids
    }
    response = make_put_request(session, 'self/jobs', json_data=jobs_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['status']
    else:
        raise UserJobsNotSetException(
            message=json_data['message'],
            error_code=json_data['error_code'],
            request_id=json_data['request_id'])


def delete_user_jobs(session, job_ids):
    """
    Remove a list of jobs from the currently authenticated user
    """
    jobs_data = {
        'jobs[]': job_ids
    }
    response = make_delete_request(session, 'self/jobs', json_data=jobs_data)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['status']
    else:
        raise UserJobsNotDeletedException(
            message=json_data['message'],
            error_code=json_data['error_code'],
            request_id=json_data['request_id'])


def get_users(session, query):
    """
    Get one or more users
    """
    # GET /api/users/0.1/users
    response = make_get_request(session, 'users', params_data=query)
    json_data = response.json()
    if response.status_code == 200:
        return json_data['result']
    else:
        raise UsersNotFoundException(
            message=json_data['message'],
            error_code=json_data['error_code'],
            request_id=json_data['request_id'])


def search_freelancers(
        session,
        jobs=None,
        countries=None,
        query=None,
        hourly_rate_min=None,
        hourly_rate_max=None,
        online_only=None,
        location_latitude=None,
        location_longitude=None,
        insignias=None,
        ratings=None,
        limit=10,
        offset=0,
        compact=True,
        user_details=None):
    search_freelancers_data = {}
    if jobs:
        search_freelancers_data['jobs[]'] = jobs
    if countries:
        search_freelancers_data['countries[]'] = countries
    if query:
        search_freelancers_data['query'] = query
    if hourly_rate_min:
        search_freelancers_data['hourly_rate_min'] = hourly_rate_min
    if hourly_rate_max:
        search_freelancers_data['hourly_rate_max'] = hourly_rate_max
    if online_only:
        search_freelancers_data['online_only'] = online_only
    if location_latitude:
        search_freelancers_data['location_latitude'] = location_latitude
    if location_longitude:
        search_freelancers_data['location_longitude'] = location_longitude
    if insignias:
        search_freelancers_data['insignias[]'] = insignias
    if ratings:
        search_freelancers_data['ratings'] = ratings
    if user_details:
        search_freelancers_data.update(user_details)
    if compact:
        search_freelancers_data['compact'] = compact

    search_freelancers_data['limit'] = limit
    search_freelancers_data['offset'] = offset
    response = make_get_request(
        session, 'users/directory',
        params_data=search_freelancers_data
    )
    json_data = response.json()
    if response.status_code == 200:
        return json_data['result']
    else:
        raise UsersNotFoundException(
            message=json_data['message'],
            error_code=json_data['error_code'],
            request_id=json_data['request_id']
        )


def get_reputations(session, user_ids, job_ids=[], role=None,
                    reputation_details=None):
    query = {}
    query['users[]'] = user_ids
    query['jobs[]'] = job_ids
    query['role'] = role
    if reputation_details:
        query.update(reputation_details)

    response = make_get_request(
        session, 'reputations',
        params_data=query
    )
    json_data = response.json()
    if response.status_code == 200:
        return json_data['result']
    else:
        raise ReputationsNotFoundException(
            message=json_data['message'],
            error_code=json_data['error_code'],
            request_id=json_data['request_id']
        )


def get_portfolios(session, user_ids, limit=10, offset=0):
    query = {'users[]': user_ids}

    # Portfolio limits are counted per user. e.a. having
    # a limit of 10 gives a max of 20 entries for 2 users

    query['limit'] = limit
    query['offset'] = offset
    response = make_get_request(
        session, 'portfolios',
        params_data=query
    )
    json_data = response.json()
    if response.status_code == 200:
        return json_data['result']
    else:
        raise PortfoliosNotFoundException(
            message=json_data['message'],
            error_code=json_data['error_code'],
            request_id=json_data['request_id']
        )
