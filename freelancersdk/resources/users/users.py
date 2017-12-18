from freelancersdk.resources.users import (
    make_get_request, make_post_request, make_put_request, make_delete_request)
from freelancersdk.resources.users.exceptions import (
    UserIdNotRetrievedException,
    UserJobsNotAddedException, UserJobsNotSetException,
    UserJobsNotDeletedException, UsersNotFoundException,
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
            message=json_data['message'], error_code=json_data['error_code'])


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
            message=json_data['message'], error_code=json_data['error_code'])


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
            message=json_data['message'], error_code=json_data['error_code'])

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
            message=json_data['message'], error_code=json_data['error_code'])
